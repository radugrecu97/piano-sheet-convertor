import yaml
from logger import logger

def getYamlDict(path):
    # Open and read the YAML file
    with open(path, 'r') as file:
        try:
            # Use the safe_load function to load the YAML content
            data = yaml.safe_load(file)

            # 'data' now contains the Python representation of the YAML content
            logger.info(data)
            return data
        except yaml.YAMLError as e:
            logger.info(f"Error reading YAML file: {e}")
