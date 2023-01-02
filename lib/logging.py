import logging


def init_logging(log_level, log_name='app-template'):
    formatter = logging.Formatter(fmt='%(levelname)s - %(filename)s:%(lineno)s - %(msg)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(log_level)

    logger = logging.getLogger(log_name)
    logger.setLevel(log_level)
    logger.addHandler(handler)

    logger.debug('Logging initialized')
    return logger
