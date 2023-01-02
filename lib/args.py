from os import path
from argparse import ArgumentParser

def parse_args():
    root_path = path.realpath(".")
    config_path = path.realpath(f"{path.dirname(__file__)}/../config.yml")
    parser = ArgumentParser(__file__, description="Description")
    parser.add_argument("-v", action="store_true", dest="verbose", help="Enable verbose logging")
    parser.add_argument("-c", "--config", default=config_path)
    args = parser.parse_args()

    return args
