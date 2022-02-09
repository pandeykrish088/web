import numbers
from tracemalloc import start
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():

    number = random.randint(1, 100)

    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        result = False
    
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.BBbmR23SODjkZhuh_zkeZF1fvNEJu3Jd5ggUsJgeTDhNrdYAzw4rRkOBDzPJVTMZTF11_82ZLSJjw25sgXBtEduElngADeSqgN81NvFhj5v5sy-mfqX4TsACK_cu9Z4aBMHbsAc"
    file = img_name
    file_from = file
    file_to = "/newFolder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)

def main():

    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
