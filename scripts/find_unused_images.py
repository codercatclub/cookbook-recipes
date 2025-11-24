import os
import json

# Path to the recipes and images directories
recipes_dir = '/home/snay/cookbook-recipes/recipes'
images_dir = '/home/snay/cookbook-recipes/images'

# Get list of all image files
images = set(os.listdir(images_dir))

# Set to hold used images
used_images = set()

# Iterate through all JSON files in recipes
for filename in os.listdir(recipes_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(recipes_dir, filename)
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
                if '__cookbookMeta' in data and 'systemfields' in data['__cookbookMeta'] and 'image' in data['__cookbookMeta']['systemfields']:
                    image = data['__cookbookMeta']['systemfields']['image']
                    used_images.add(image)
            except json.JSONDecodeError:
                print(f"Error reading {filename}")

# Find unused images
unused_images = images - used_images

# Print unused images
if unused_images:
    print("Unused images:")
    for img in sorted(unused_images):
        print(img)
else:
    print("All images are used.")