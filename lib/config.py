import logging
from omegaconf import OmegaConf

log = logging.getLogger('app-template')

def init_config(conf_path):
    conf = OmegaConf.load(conf_path)
    log.debug(conf)
    return conf
