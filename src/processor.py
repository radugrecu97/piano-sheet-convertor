import subprocess
from logger import logger


def processFile(path):
    try:
        subprocess.run(['pianoplayer', path])
    except subprocess.CalledProcessError as e:
        logger.info(f"Error: {e}")
