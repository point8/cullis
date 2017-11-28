"""Encapsules the logger configuration
"""

import logging


def configure_logger(logfile=None):
    '''Configure logger ;)'''
    logger = logging.getLogger('p8.cullis')
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("werkzeug").setLevel(logging.WARNING)
    logging.getLogger("schedule").setLevel(logging.WARNING)

    # reduce debug output from third-party modules
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("werkzeug").setLevel(logging.WARNING)

    # terminal stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    sh_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)-8s - %(message)s '
        '[%(name)s/%(funcName)s | %(threadName)s (PID:%(process)d)]',
        datefmt='%H:%M:%S')
    stream_handler.setFormatter(sh_formatter)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)

    # logfile handler
    if logfile:
        # create file handler which logs even debug messages
        file_handler = logging.FileHandler(logfile)
        file_handler.setLevel(logging.DEBUG)
        fh_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)-8s - %(message)s '
            '[%(name)s/%(funcName)s | %(threadName)s (%(process)d)]',
            datefmt='%Y-%m-%dT%H:%M:%S')
        file_handler.setFormatter(fh_formatter)
        logger.addHandler(file_handler)

    return logger