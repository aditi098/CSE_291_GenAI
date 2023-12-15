while IFS= read -r line || [[ -n "$line" ]]; do
    # Extract only the package name, ignore version
    package=$(echo "$line" | awk -F'==' '{print $1}')
    echo "Attempting to install the latest version of $package..."
    pip install "$package" || echo "Failed to install $package, skipping..."
done < "requirements.txt"
