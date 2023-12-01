# logger_config.py
import logging.config
import consts
import colorlog

logging.config.fileConfig(f"{consts.DIR_ASSETS}/logging_config.ini")


def getLogger(logger_name="main"):
    return colorlog.getLogger(logger_name)

logger = getLogger()
