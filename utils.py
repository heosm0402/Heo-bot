import logging
from logging import handlers


def get_log_handler(logger_name, logging_level, log_file_path):
    formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(name)s [%(filename)s:%(lineno)d] %(message)s")

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging_level)

    # file handler
    fileMaxByte = 1024 * 1024 * 10  # 10MB
    fileRotatingHandler = handlers.RotatingFileHandler(log_file_path, maxBytes=fileMaxByte, backupCount=10)
    fileRotatingHandler.setFormatter(formatter)
    logger.addHandler(fileRotatingHandler)

    # stream handler
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)

    return logger


def return_interval_to_seconds(itv):
    unit: str = itv[-1].lower()
    interval = int(itv[:-1])
    if unit == "s":
        return interval
    elif unit == "m":
        return interval * 60
    elif unit == "h":
        return interval * 60 * 60
