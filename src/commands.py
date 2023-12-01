from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, event):
        pass


class pianoSheetCommand(Command):

    def execute(self, event):
        if event.dir:
            return

        modified_file = event.pathname
        print(f"File modification complete: {modified_file}")