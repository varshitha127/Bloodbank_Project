import os
import requests

# Create webfonts directory if it doesn't exist
os.makedirs('static/webfonts', exist_ok=True)

# Font Awesome CDN base URL
base_url = 'https://use.fontawesome.com/releases/v5.15.4/webfonts/'

# List of font files to download
font_files = [
    'fa-brands-400.eot',
    'fa-regular-400.eot',
    'fa-solid-900.eot'
]

def download_font(url, filename):
    """Download a font file and save it to the webfonts directory."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        filepath = os.path.join('static/webfonts', filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded {filename}')
    except requests.exceptions.RequestException as e:
        print(f'Error downloading {filename}: {e}')

# Download each font file
for font_file in font_files:
    url = base_url + font_file
    download_font(url, font_file)

print('Font download complete!') 