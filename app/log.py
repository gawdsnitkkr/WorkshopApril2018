import logging

def setup_custom_logger(name):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    file_handler = logging.FileHandler('main.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger