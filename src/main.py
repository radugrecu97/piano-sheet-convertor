import time

from uvicorn import run
#from api import app

import monitor
import consts
import commands


if __name__ == "__main__":
    # run("main:app", host="127.0.0.1", port=8000, reload=True)
    dirActionMap = { consts.DIR_PIANO_SHEETS_IN: commands.pianoSheetCommand()
    }

    dirMonitor = monitor.DirectoryMonitor(dirActionMap)
    dirMonitor.addDirectory(consts.DIR_PIANO_SHEETS_IN)

    while (True):
        dirMonitor.watchPaths()
        time.sleep(1)
