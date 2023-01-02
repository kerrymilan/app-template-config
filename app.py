#!/usr/bin/env python3

import sys
import logging
from pathlib import Path

from lib.args import parse_args
from lib.config import init_config
from lib.logging import init_logging

log = None

def main():
    global log
    
    args = parse_args()
    conf = init_config(args.config)

    log_level = logging.DEBUG if args.verbose else logging.INFO
    log = init_logging(log_level)


    return 0

if __name__ == "__main__":
    sys.exit(main())
