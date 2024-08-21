import logging
import os
import inspect

class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.logger = logging.getLogger('SingletonLogger')
        self.logger.setLevel(logging.DEBUG)
        self._file_handler()
        self._console_handler()
    
    def _file_handler(self):
        file_handler = logging.FileHandler('app.log', mode='a')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)

    def _console_handler(self):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
    
    def log(self, message):
        pass
        # frame = inspect.currentframe().f_back
        # class_name = frame.f_locals.get('self', None).__class__.__name__ if frame.f_locals.get('self', None) else 'UnknownClass'
        # function_name = frame.f_code.co_name
        # self.logger.debug(message, extra={'class': class_name, 'function': function_name})

    @staticmethod
    def get_instance():
        return Logger()
