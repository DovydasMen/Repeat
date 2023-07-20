import logging

from logging import FileHandler, StreamHandler
from logging import Formatter

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.INFO

# console loger

console_logger = logging.getLogger("Console Logger")
console_logger.setLevel(LOG_LEVEL)
console_file_handler = StreamHandler()
console_formatter = Formatter(LOG_FORMAT)
console_file_handler.setFormatter(console_formatter)
console_logger.addHandler(console_file_handler)

# file logger

LOG_TO_FILE = "data.log"
file_logger = logging.getLogger("File logger")

file_logger.setLevel(LOG_LEVEL)
file_handler = FileHandler(LOG_TO_FILE)
file_formatter = Formatter(LOG_FORMAT)
file_handler.setFormatter(file_formatter)
file_logger.addHandler(file_handler)

if __name__ == "__main__":
    file_logger.info("Ar veikia?")
    console_logger.info("Manau, kad taip!")
