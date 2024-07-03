
import os
import shutil
import random

# Đường dẫn tới thư mục chứa 100 tấm ảnh
source_folder = r'D:\linh\PYTHON\Train_Augmented_500_old'
# Đường dẫn tới thư mục lưu ảnh theo tỷ lệ 20% (tạm gọi là folder1)
folder1 = r'D:\linh\PYTHON\Train_Augmented_500\test'
# Đường dẫn tới thư mục lưu ảnh theo tỷ lệ 80% (tạm gọi là folder2)
folder2 = r'D:\linh\PYTHON\Train_Augmented_500\train'

# Tạo thư mục nếu chưa tồn tại
os.makedirs(folder1, exist_ok=True)
os.makedirs(folder2, exist_ok=True)

# Duyệt qua tất cả các thư mục con trong source_folder
for root, dirs, files in os.walk(source_folder):
    for dir in dirs:
        current_folder = os.path.join(root, dir)
        all_files = os.listdir(current_folder)
        all_images = [file for file in all_files if file.endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif'))]

        # Xáo trộn danh sách ảnh
        random.shuffle(all_images)

        # Tính toán số lượng ảnh cho từng thư mục
        total_images = len(all_images)
        num_images_folder1 = total_images // 10  # 1 phần của 10
        num_images_folder2 = total_images - num_images_folder1  # 9 phần còn lại

        # Tạo các thư mục con tương ứng trong folder1 và folder2
        subfolder1 = os.path.join(folder1, dir)
        subfolder2 = os.path.join(folder2, dir)
        os.makedirs(subfolder1, exist_ok=True)
        os.makedirs(subfolder2, exist_ok=True)

        # Phân chia ảnh vào các thư mục
        for i, image in enumerate(all_images):
            if i < num_images_folder1:
                shutil.copy(os.path.join(current_folder, image), os.path.join(subfolder1, image))
            else:
                shutil.copy(os.path.join(current_folder, image), os.path.join(subfolder2, image))

        print(
            f"Đã tách {total_images} ảnh từ thư mục {dir} thành {num_images_folder1} ảnh trong {subfolder1} và {num_images_folder2} ảnh trong {subfolder2}.")
