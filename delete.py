import os
import shutil

root_folder = "./"

for folder in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder)
    if os.path.isdir(folder_path) and folder != "origin_image":
        has_images = False
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg')):
                has_images = True
                break
        
        if has_images:
            origin_image_folder = os.path.join(root_folder, "origin_image")
            if not os.path.exists(origin_image_folder):
                os.makedirs(origin_image_folder)
            for filename in os.listdir(folder_path):
                if filename.lower().endswith(('.png', '.jpg')):
                    source_path = os.path.join(folder_path, filename)
                    output_path = os.path.join(origin_image_folder, filename)
                    shutil.move(source_path, output_path)
            os.rmdir(folder_path)
        