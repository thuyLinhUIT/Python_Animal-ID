import os
from PIL import Image, ImageOps, ImageEnhance
import random
import numpy as np

# Specify the input directory containing the images and the output directory
input_dir = r'D:\linh\PYTHON\data_animal'
output_dir = r'D:\linh\PYTHON\processed_images'
os.makedirs(output_dir, exist_ok=True)

# Hàm để thay đổi màu ngẫu nhiên
def random_color(image):
    # Chuyển đổi ảnh thành chế độ RGB nếu chưa phải là RGB
    image = image.convert("RGB")

    # Tách các kênh màu
    r, g, b = image.split()

    # Tăng kênh màu xanh
    enhancer = ImageEnhance.Brightness(b)
    factor = random.uniform(0.30, 1.5)  # Điều chỉnh khoảng giới hạn tăng độ sáng của kênh màu xanh
    r = enhancer.enhance(factor)
    factor = random.uniform(0.30, 1.50)
    g = enhancer.enhance(factor)
    factor = random.uniform(0.30, 1.50)
    b = enhancer.enhance(factor)
    # Ghép lại các kênh màu thành ảnh hoàn chỉnh
    new_image = Image.merge("RGB", (r, g, b))
    return new_image

# Process each image in the input directory
for idx, filename in enumerate(os.listdir(input_dir)):
    if filename.endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif')):  # Filter image files
        image_path = os.path.join(input_dir, filename)

        # Open the image
        image = Image.open(image_path)

        # Resize the image to 224x224
        image = image.resize((224, 224))

        # Define base name for new images
        base_name = f"mouse_{idx+1}"

        # Save the original resized image
        new_filename = f"{base_name}_1.jpg"
        image.save(os.path.join(output_dir, new_filename))

        # Create and save the image with a black rectangle
        enhancer = ImageEnhance.Brightness(image)
        black_rect_image = enhancer.enhance(0.2)
        black_rect_filename = f"{base_name}_3.jpg"
        black_rect_image.save(os.path.join(output_dir, black_rect_filename))

        # Create and save the rotated image (90 degrees)
        rotated_image = image.rotate(90, expand=True)
        rotated_filename = f"{base_name}_4.jpg"
        rotated_image.save(os.path.join(output_dir, rotated_filename))

        # Create and save the rotated image (180 degrees)
        rotated_image = image.rotate(180, expand=True)
        rotated_filename = f"{base_name}_2.jpg"
        rotated_image.save(os.path.join(output_dir, rotated_filename))

        # Tạo thêm 3 bức ảnh xoay và đổi màu ngẫu nhiên
        for i in range(6):
            random_angle = random.uniform(0, 360)
            random_rotated_image = image.rotate(random_angle, expand=True)
            random_rotated_image = random_rotated_image.resize((224, 224))  # Resize lại về 224x224
            colored_image = random_color(random_rotated_image)  # Thay đổi màu ngẫu nhiên
            colored_filename = f"{base_name}_{5 + i}.jpg"
            colored_image.save(os.path.join(output_dir, colored_filename))

print("Image processing complete4.")
