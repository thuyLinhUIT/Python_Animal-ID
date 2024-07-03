import os

#sửa lại tên theo nhu cầu
def rename_images(folder_path, prefix='mimi'):
    # Lấy danh sách tất cả các file trong thư mục
    files = os.listdir(folder_path)

    # Lọc ra những file có đuôi là ảnh (jpg, jpeg, png, gif, bmp, tiff)
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'))]

    # Sắp xếp các file để đổi tên theo thứ tự
    image_files.sort()

    # Đổi tên từng file
    for index, filename in enumerate(image_files):
        # Lấy phần mở rộng của file
        file_extension = os.path.splitext(filename)[1]

        # Tạo tên mới 1:02 là minh_02.jpg; 1:03 là minh_003.jpg
        new_name = f"{prefix}_{index + 1:03}{file_extension}"

        # Đường dẫn đầy đủ của file cũ và file mới
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        # Đổi tên file
        os.rename(old_path, new_path)
        print(f"Renamed '{filename}' to '{new_name}'")


# Sử dụng hàm với đường dẫn đến folder chứa ảnh
folder_path = r"D:\linh\PYTHON\data_animal"
rename_images(folder_path)
