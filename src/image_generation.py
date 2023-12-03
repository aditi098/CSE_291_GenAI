import torch
from PIL import Image
from io import BytesIO
import os
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler, StableDiffusionImg2ImgPipeline
import matplotlib.pyplot as plt

model_id = "stabilityai/stable-diffusion-2"
device = "cuda:0"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
text2img_pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16).to(device)
img2img_pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to(device)


def generate_images(df, out_dir):
    for index, row in df.iterrows():
        prompts = row["summarized_story"]
        if len(prompts)>0:
            init_prompt = prompts[0]
            init_image = text2img_pipe(init_prompt).images[0]
            final_index = row["story_name"]+"_segment_0"
            save_path = os.path.join(out_dir,str(final_index) +'.jpg')
            init_image.save(save_path)
            
            for idx, prompt in enumerate(prompts[1:]):    
                images = img2img_pipe(prompt=prompt, image=init_image, strength=0.90, guidance_scale=5.5).images
                final_index = row["story_name"]+"_segment_"+ str(idx+1)
                save_path = os.path.join(out_dir,str(final_index) +'.jpg')
                images[0].save(save_path)





