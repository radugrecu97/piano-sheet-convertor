import pyinotify

from logger import logger


class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, pathActionMap):
        super().__init__()
        self.pathActionMap = pathActionMap

    def process_default(self, event):
        logger.info(f"Event attributes: {vars(event)}")

        action = self.pathActionMap.get(event.path)

        if action:
            logger.info(f"FN = {action}")
            action.execute(event)


class DirectoryMonitor():
    dirCommandMap = dict()
    notifer = None
    watchManager = None
    eventHandler = None

    def __init__(self, pathActionMap):
        # Log a debug message
        logger.debug("Started monitor")

        super().__init__()
        self.watchManager = pyinotify.WatchManager()
        self.handler = EventHandler(pathActionMap)
        self.notifier = pyinotify.Notifier(self.watchManager, self.handler)

    def addDirectory(self, path):
        if path == "":
            logger.error("Missing path argument")
            exit(-1)
        self.watchManager.add_watch(path, pyinotify.IN_CLOSE_WRITE)
        logger.info(f"Monitoring path '{path}'.")

    # Run this in a while loop
    def watchPaths(self):
        self.notifier.process_events()
        if self.notifier.check_events():
            self.notifier.read_events()
