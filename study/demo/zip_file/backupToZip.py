import os
import zipfile
from pathlib import Path


def backup_to_zip(folder):
    # 获取文件的绝对路径
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFileName):
            break
        number += 1

    # 创建ZIP文件.
    print(f'创建 {zipFileName}...')
    backupZip = zipfile.ZipFile(zipFileName, 'w')

    # 遍历文件目录.
    for folder_name, sub_folders, filenames in os.walk(folder):
        print(f'添加文件 {folder_name}...')
        #  添加当前文件到ZIP文件.
        backupZip.write(folder_name)
        #  添加所有文件到文件夹，然后压缩.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            # 判断如何是备份压缩文件，不添加到备份文件
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # 如果存在备份，则不压缩
            backupZip.write(os.path.join(folder_name, filename))
    backupZip.close()
    print('完成')


# 调用函数
backup_to_zip(Path.cwd())
