from config import *
import logging
import shutil
import os
import re


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename="logs/log.txt")


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
 
def moved(formats, movies_file):
        shutil.move(formats, movies_file)
        return logging.info(f"{formats.split('/')[-1]} Moved in {movies_file} ")



if __name__=="__main__":

    if not os.listdir(download_path):
        logging.warning(f"Directory {download_path} is empty")

    else:
        try:

            mp4_count = 0
            mkv_count = 0
            pdf_count = 0
            mp3_count = 0

            extension = check_extenstion(download_path)

            if "mp4" in extension:
                for mp4 in extension["mp4"]:
                    mp4name = mp4.split("/")[-1]
                    if re.search("S0.E0.", mp4name):
                        index = re.search("S0.E0.", mp4name)
                        mk_pattern = mp4name[0:index.start()-1]
                        if os.path.exists(os.path.join(serial_path, mk_pattern)):
                            moved(mp4, os.path.join(serial_path, mk_pattern))
                        else:
                            os.mkdir(os.path.join(serial_path, mk_pattern))
                            moved(mp4, os.path.join(serial_path, mk_pattern))
                            mp4_count += 1
                    else:
                        moved(mp4 ,movies_path)
                        mp4_count += 1
            else:
                 logging.warning("mp4 file not exists")

            if "mkv" in extension:
                 for mkv in extension["mkv"]:
                    mkvname = mkv.split("/")[-1]
                    if re.search("S0.E0.", mkvname):
                        index = re.search("S0.E0.", mkvname)
                        mk_pattern = mkvname[0:index.start()-1]
                        if os.path.exists(os.path.join(serial_path, mk_pattern)):
                            moved(mkv, os.path.join(serial_path, mk_pattern))

                        else:
                            os.mkdir(os.path.join(serial_path, mk_pattern))
                            moved(mkv, os.path.join(serial_path, mk_pattern))
                            mkv_count += 1
                    else:
                        moved(mkv ,movies_path)
                        mkv_count += 1
            else:
                 logging.warning("mkv file not exists")

            if "pdf" in extension:
                 for pdf in extension["pdf"]:
                     moved(pdf, pdf_path)
                     pdf_count += 1
            else:
                 logging.warning("pdf file not exists")

            if "mp3" in extension:
                 for mp3 in extension["mp3"]:
                     moved(mp3, audio_path)
                     mp3_count += 1
            else:
                 logging.warning("mp3 file not exists")

        except:
            logging.debug("Please check download file")

        finally:
            total = mp4_count+mkv_count+pdf_count+mp3_count
            logging.info(f'total moved file : {total} | mp4 : {mp4_count} - mkv : {mkv_count} - pdf : {pdf_count} - mp3 : {mp3_count}')
