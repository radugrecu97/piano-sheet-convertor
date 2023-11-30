from watchdog.events import FileSystemEventHandler


class FolderObserver(FileSystemEventHandler):
    path = ""
    command = None

    def __init__(self, pathToObserve, command) -> None:
        super().__init__()
        self.path = pathToObserve
        self.command = command

    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            self.command.execute()
        elif event.event_type == 'modified':
            self.command.execute()
        elif event.event_type == 'deleted':
            # print(f"File {event.src_path} has been deleted.")
            pass
