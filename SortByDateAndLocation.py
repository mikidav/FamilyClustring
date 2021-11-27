import os
import shutil
import cv2
import exifread
import PIL.Image as Image



def get_minimum_creation_time(file_name_full_path):
    with open(file_name_full_path, 'rb') as image:  # file path and name
        exif_data = exifread.process_file(image)
        mtime = "?"
        if 306 in exif_data and exif_data[306] < mtime: # 306 = DateTime
            mtime = exif_data[306]
        if 36867 in exif_data and exif_data[36867] < mtime: # 36867 = DateTimeOriginal
            mtime = exif_data[36867]
        if 36868 in exif_data and exif_data[36868] < mtime: # 36868 = DateTimeDigitized
            mtime = exif_data[36868]
        return mtime



def find_infile(file_name_full_path):
    print(file_name_full_path)
    img = Image.open(file_name_full_path)
    exif = img._getexif()
    if exif is None:
        return
    print(exif.items)
    return ""


root = "C:/Users/mikid/PycharmProjects/pythonProject1/1/2018/unknown_city"
for filename in os.listdir(root):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        try:
            file_name_full_path = os.path.join(root, filename)
            dt=find_infile(file_name_full_path)
            print(dt)
        except Exception as e:
            print(e)
    else:
        continue
