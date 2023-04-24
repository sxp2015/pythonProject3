import os
from PIL import Image


def is_photo_file(file_path):
    """
    判断指定的文件是否是照片文件。
    """
    if not os.path.isfile(file_path):
        return False
    filename = os.path.basename(file_path)
    if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
        return False
    try:
        with Image.open(file_path) as im:
            width, height = im.size
            return width >= 500 and height >= 500
    except:
        return False


def is_photo_folder(folder_path):
    """
    判断指定的文件夹是否是照片文件夹。
    """
    # 统计当前文件夹下所有文件的信息
    files_info = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if is_photo_file(file_path):
            files_info.append((filename, file_path))

    # 如果文件数超过 10 个，且照片文件数量占比超过一半，则判定为照片文件夹。
    total_count = len(os.listdir(folder_path))
    photo_count = len(files_info)
    return total_count > 0 and photo_count >= 10 and photo_count >= total_count / 2, photo_count


def find_photo_folders(root, output_file):
    """
    遍历指定根目录下的所有文件夹，查找可能的照片文件夹，并将结果保存到指定的文件中。
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for foldername, subfolders, filenames in os.walk(root):
            is_photo, photo_count = is_photo_folder(foldername)
            if is_photo:
                f.write('{}\t{}\n'.format(foldername, photo_count))
                print('发现照片文件夹：{}（{}张照片）'.format(foldername, photo_count))


# 示例代码，从 C 盘根目录开始查找可能的照片文件夹，并将找到的结果保存到 photo_folders.txt 文件中
find_photo_folders(r'C:\Users\admin\Pictures', 'photo_folders.txt')
