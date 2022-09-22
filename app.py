#!/usr/bin/env python3

import sys
import logging
from argparse import ArgumentParser

log = None

def init_logging(log_level):
    formatter = logging.Formatter(fmt='%(levelname)s - %(filename)s:%(lineno)s - %(msg)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    handler.setLevel(log_level)

    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    logger.addHandler(handler)

    logger.debug('Logging initialized')
    return logger

def main():
    global log
    parser = ArgumentParser(__file__, description="Description")
    parser.add_argument("-v", action="store_true", dest="verbose", help="Enable verbose logging")
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.WARNING
    log = init_logging(log_level)

    # Do the thing 

    return 0

if __name__ == "__main__":
    sys.exit(main())
