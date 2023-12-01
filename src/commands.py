from abc import ABC, abstractmethod
from logger import logger


class Command(ABC):
    @abstractmethod
    def execute(self, event):
        pass


class pianoSheetCommand(Command):

    def execute(self, event):
        if event.dir:
            return

        modified_file = event.pathname
        logger.info(f"File modification complete: {modified_file}")