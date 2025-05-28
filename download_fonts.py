import os
import requests

# Create webfonts directory if it doesn't exist
os.makedirs('static/webfonts', exist_ok=True)

# Font Awesome CDN base URLs
base_urls = {
    'webfonts/': 'https://use.fontawesome.com/releases/v5.15.4/webfonts/',
    'js/': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.8/umd/'
}

# List of files to download (renamed from font_files for clarity)
files_to_download = [
    'fa-brands-400.eot',
    'fa-regular-400.eot',
    'fa-solid-900.eot',
    'fa-brands-400.svg',
    'fa-regular-400.svg',
    'fa-solid-900.svg',
    'js/popper.min.js',
    'js/popper.min.js.map'
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
for file in files_to_download:
    # Choose the appropriate base URL (or fallback) for the file.
    prefix = 'webfonts/' if file.startswith('fa') else 'js/'
    base_url = base_urls.get(prefix, 'https://use.fontawesome.com/releases/v5.15.4/webfonts/')
    url = base_url + file
    download_font(url, file)

print('Font download complete!') 