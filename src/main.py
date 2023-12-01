import time
# from uvicorn import run
# from api import app

import consts
import commands
import monitor

from logger import logger


def main():
    # run("main:app", host="127.0.0.1", port=8000, reload=True)

    # Define directory action map
    dirActionMap = {
        consts.DIR_PIANO_SHEETS_IN: commands.pianoSheetCommand()
    }

    # Create and configure directory monitor
    dirMonitor = monitor.DirectoryMonitor(dirActionMap)
    dirMonitor.addDirectory(consts.DIR_PIANO_SHEETS_IN)

    # Watch directories in a loop
    logger.info("Start monitoring.")
    while True:
        dirMonitor.watchPaths()
        time.sleep(1)


if __name__ == "__main__":
    main()