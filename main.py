from config import *
import shutil
import os


info_logger = Loggers(logging.INFO, ('%(asctime)s, %(name)s, %(message)s'), "logs/info.log")

warning_logger = Loggers(logging.WARNING, ('%(asctime)s, %(name)s, %(message)s'), "logs/warning.log")

debug_logger = Loggers(logging.DEBUG, ('%(asctime)s, %(name)s, %(message)s'), "logs/debug.log")

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


def moved(extension, format_type, movies_file):
    for format_type in extension[str(format_type)]:
        sutill.move(format_type, movies_file)
        return info_logger.info(f"{format_type} Moved in {movies_file}")



if __name__=="__main__":

    if not os.listdir(download_path):
        warning_logger.warning(f"Directory {download_path} is empty")

    else:
        try:

            mp4_count = 0
            mkv_count = 0
            pdf_count = 0

            extension = check_extenstion(download_path)
            if extension["mp4"] in extension:
                moved(extension, mp4 ,movies_path)
                mp4_count += 1
            else:
                warning_logger.warning("mp4 file not exists")

            if extension["mkv"] in extension:
                moved(extension, mkv,movies_path)
                mkv_count += 1
            else:
                warning_logger.warning("mkv file not exists")

            if extension["pdf"] in extension:
                moved(extension, pdf, pdf_path)
                pdf_count += 1
            else:
                warning_logger.warning("pdf file not exists")

        except:
            debug_logger.debug("Please check download file")




