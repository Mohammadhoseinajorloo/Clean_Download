import logging


class Loggers:

    def __init__(self, level, formatter, file_handler):
        self.logger = logging.getLogger(__name__) 
        self.level = level
        self.logger.setLevel(self.level)
        self.formatter = logging.Formatter(formatter)
        self.file_handler = logging.FileHandler(file_handler)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def display (self):
        print(f'logger : {self.logger}\nformatter : {self.formatter}\nfile_handler : {self.file_handler}\nlevel : {self.level}')
        

info_logger = Loggers(logging.INFO, ('%(asctime)s, %(name)s, %(message)s'), "logs/info.log")

warning_logger = Loggers(logging.WARNING, ('%(asctime)s, %(name)s, %(message)s'), "logs/warning.log")

debug_logger = Loggers(logging.DEBUG, ('%(asctime)s, %(name)s, %(message)s'), "logs/debug.log")





info_logger.display()
print( "#############################")
warning_logger.display()
print( "#############################")
debug_logger.display()
