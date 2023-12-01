import pyinotify


class EventHandler(pyinotify.ProcessEvent):
    def __init__(self, pathActionMap):
        super().__init__()
        self.pathActionMap = pathActionMap

    def process_default(self, event):
        print(f"Event attributes: {vars(event)}")

        action = self.pathActionMap.get(event.path)

        if action:
            print(f"FN = {action}")
            action.execute(event)


class DirectoryMonitor():
    dirCommandMap = dict()
    notifer = None
    watchManager = None
    eventHandler = None

    def __init__(self, pathActionMap) -> None:
        super().__init__()
        self.watchManager = pyinotify.WatchManager()
        self.handler = EventHandler(pathActionMap)
        self.notifier = pyinotify.Notifier(self.watchManager, self.handler)

    def addDirectory(self, path):
        self.watchManager.add_watch(path, pyinotify.IN_CLOSE_WRITE)

    # Run this in a while loop
    def watchPaths(self):
        self.notifier.process_events()
        if self.notifier.check_events():
            self.notifier.read_events()
