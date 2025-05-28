import os
import requests

font_files = [
    "fa-brands-400.woff2",
    "fa-brands-400.woff",
    "fa-brands-400.ttf",
    "fa-regular-400.woff2",
    "fa-regular-400.woff",
    "fa-regular-400.ttf",
    "fa-solid-900.woff2",
    "fa-solid-900.woff",
    "fa-solid-900.ttf"
]

base_url = "https://use.fontawesome.com/releases/v5.15.3/webfonts/"
output_dir = "static/webfonts"

# Create directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for file in font_files:
    url = base_url + file
    output_path = os.path.join(output_dir, file)
    print(f"Downloading {file}...")
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Successfully downloaded {file}")
    else:
        print(f"Failed to download {file}")

print("All font files downloaded successfully!") 