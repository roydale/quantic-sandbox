import os
from PIL import Image

def create_thumbnails(image_dir, size=(50, 50)):
    # Create a 'thumbnails' subfolder inside the given image directory
    thumbnails_dir = os.path.join(image_dir, "thumbnails")
    os.makedirs(thumbnails_dir, exist_ok=True)

    for filename in os.listdir(image_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_path = os.path.join(image_dir, filename)
            thumbnail_path = os.path.join(thumbnails_dir, filename)

            try:
                with Image.open(image_path) as img:
                    img.thumbnail(size)
                    img.save(thumbnail_path)
                    print(f"Thumbnail saved: {thumbnail_path}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

# Example usage
# Replace this with your actual image folder path
image_folder = 'images'
create_thumbnails(image_folder)
