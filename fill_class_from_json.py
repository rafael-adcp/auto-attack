import json

from log import get_logger

logger = get_logger(__name__)

def fill_class_from_json(cls, file_name) -> object:
    try:
        
        with open(file_name, 'r') as fp:
            json_data = json.load(fp)
        
            genericConfig = cls.parse_obj(json_data)
            return genericConfig
    except Exception as e:
        logger.error("failed to load json file ({})".format(file_name))
        logger.error(e)
        exit(1)