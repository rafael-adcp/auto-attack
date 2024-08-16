import logging

def get_logger(name):
    logger = logging.getLogger(name)
    logging.basicConfig(format='[%(asctime)s] - (%(levelname)s):: %(message)s', level=logging.INFO)
    
    logger.setLevel(logging.INFO)
    
    return logger