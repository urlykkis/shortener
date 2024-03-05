import logging

from loguru import logger

log_format = "{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}"
log_levels = ["INFO", "ERROR", "DEBUG"]

for l_level in log_levels:
    logger.add(
        f"./logs/{l_level.lower()}.log",
        level=l_level,
        colorize=False,
        format=log_format,
        rotation="10 MB",
        compression="zip",
    )


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_logger(level="", ignored=""):
    logging.basicConfig(handlers=[InterceptHandler()], level=logging.getLevelName(level))

    for ignore in ignored:
        logger.disable(ignore)
