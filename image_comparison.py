import os
import shutil
import cv2
import face_recognition


def load_encoding_images(images_path):
    img = cv2.imread(images_path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_encoding = face_recognition.face_encodings(rgb_img)[0]
    return img_encoding

def find_infile():
    global t
    print(filename)
    original_file_path = os.path.join(root, filename)
    img2 = cv2.imread(original_file_path)
    rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    for img_encoding2 in face_recognition.face_encodings(rgb_img2):
        s = False
        for t in f:
            result = face_recognition.compare_faces([t], img_encoding2)
            if True in result:
                print("find miki Move file to directory")
                newfolder = os.path.join(root, "family")
                newfilePath = os.path.join(newfolder, filename)
                try:
                    shutil.move(original_file_path, newfilePath)
                except Exception as e:
                    print(e)
                s = True
                break
        if s:
            continue

f = []


def GetPersons(f):
    person_folder = "C:/Users/mikid/PycharmProjects/pythonProject1/images"
    for file_name in os.listdir(person_folder):
        if file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
            file_name_full_path = os.path.join(person_folder, file_name)
            r = load_encoding_images(file_name_full_path)
            f.append(r)


GetPersons()

root="C:/Users/mikid/PycharmProjects/pythonProject1/1/2018/unknown_city"
for filename in os.listdir(root):
    if filename.endswith(".jpg") or filename.endswith(".jpeg"):
        try:
            find_infile()
        except Exception as e: print(e)
    else:
        continue

# cv2.imshow("Img", img)
# cv2.imshow("Img 2", img2)
cv2.waitKey(0)
