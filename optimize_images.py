from PIL import Image
import os
from pathlib import Path

def optimize_image(input_path, output_path=None, max_size=(1920, 1080), quality=85):
    """
    Optimize an image by resizing if too large and compressing
    Args:
        input_path: Path to input image
        output_path: Path to save optimized image (if None, overwrites input)
        max_size: Maximum dimensions (width, height)
        quality: JPEG quality (1-100)
    """
    if output_path is None:
        output_path = input_path

    try:
        # Open image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Calculate new size while maintaining aspect ratio
            ratio = min(max_size[0]/img.size[0], max_size[1]/img.size[1])
            if ratio < 1:  # Only resize if image is larger than max_size
                new_size = tuple(int(dim * ratio) for dim in img.size)
                img = img.resize(new_size, Image.LANCZOS)
            
            # Save optimized image
            img.save(output_path, 'JPEG', quality=quality, optimize=True)
            
            # Get file sizes
            original_size = os.path.getsize(input_path)
            optimized_size = os.path.getsize(output_path)
            savings = (original_size - optimized_size) / original_size * 100
            
            print(f"Optimized {input_path}")
            print(f"Original size: {original_size/1024:.1f}KB")
            print(f"Optimized size: {optimized_size/1024:.1f}KB")
            print(f"Savings: {savings:.1f}%")
            print("-" * 50)
            
    except Exception as e:
        print(f"Error optimizing {input_path}: {str(e)}")

def optimize_directory(directory, extensions=('.jpg', '.jpeg', '.png')):
    """Optimize all images in a directory"""
    directory = Path(directory)
    
    # Create optimized directory
    optimized_dir = directory / 'optimized'
    optimized_dir.mkdir(exist_ok=True)
    
    # Process each image
    for ext in extensions:
        for img_path in directory.glob(f'*{ext}'):
            if 'optimized' not in str(img_path):
                output_path = optimized_dir / img_path.name
                optimize_image(str(img_path), str(output_path))

if __name__ == '__main__':
    # Optimize images in static/images directory
    image_dir = 'static/images'
    print("Starting image optimization...")
    optimize_directory(image_dir)
    print("Image optimization complete!") 