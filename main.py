from config import *
import shutil
import os

def check_extenstion(directory):

    extenstion = {}

    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = file.split(".")[-1]
            if ext in extenstion:
                extenstion[ext].append(os.path.join(root, file))
            else:
                extenstion[ext]=[os.path.join(root, file)]
    return extenstion



if __name__=="__main__":
    if not os.listdir(download_path):
        print (f"Directory {download_path} is empty")
    else:
        pass


