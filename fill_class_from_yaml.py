import json
import yaml

from log import get_logger

logger = get_logger(__name__)

def fill_class_from_yaml(cls, file_name) -> object:
    try:
        
        with open(file_name, 'r') as fp:
            yaml_data = yaml.load(fp, Loader=yaml.FullLoader)
        
            genericConfig = cls.parse_obj(yaml_data)
            return genericConfig
    except Exception as e:
        logger.error("failed to load yaml file ({})".format(file_name))
        logger.error(e)
        exit(1)