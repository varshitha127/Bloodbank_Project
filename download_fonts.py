import os
import requests

# Create webfonts directory if it doesn't exist
os.makedirs('static/webfonts', exist_ok=True)

# Font Awesome CDN base URLs
base_urls = {
    'webfonts/': 'https://use.fontawesome.com/releases/v5.15.4/webfonts/',
    'popper/': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.8/umd/',
    'bootstrap/': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/'
}

# List of files to download (renamed from font_files for clarity)
files_to_download = [
    'webfonts/fa-brands-400.eot',
    'webfonts/fa-regular-400.eot',
    'webfonts/fa-solid-900.eot',
    'webfonts/fa-brands-400.svg',
    'webfonts/fa-regular-400.svg',
    'webfonts/fa-solid-900.svg',
    'popper/popper.min.js',
    'popper/popper.min.js.map',
    'bootstrap/bootstrap.bundle.min.js',
    'bootstrap/bootstrap.bundle.min.js.map',
    'bootstrap/bootstrap.js',
    'bootstrap/bootstrap.js.map',
    'bootstrap/bootstrap.min.js',
    'bootstrap/bootstrap.min.js.map'
]

def download_font(url, filename):
    """Download a font file and save it to the appropriate directory."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Determine the target directory based on the file type
        if filename.startswith('webfonts/'):
            target_dir = 'static/webfonts'
            filename = filename.replace('webfonts/', '')
        elif filename.startswith('popper/'):
            target_dir = 'static/js'
            filename = filename.replace('popper/', '')
        elif filename.startswith('bootstrap/'):
            target_dir = 'static/js'
            filename = filename.replace('bootstrap/', '')
        else:
            target_dir = 'static/js'
            
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f'Successfully downloaded {filename}')
    except requests.exceptions.RequestException as e:
        print(f'Error downloading {filename}: {e}')

# Download each file
for file in files_to_download:
    # Choose the appropriate base URL for the file
    prefix = file.split('/')[0] + '/'
    base_url = base_urls.get(prefix, 'https://use.fontawesome.com/releases/v5.15.4/webfonts/')
    url = base_url + file.split('/')[-1]
    download_font(url, file)

print('Download complete!') 