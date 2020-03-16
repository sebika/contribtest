import logging


# Instantiate the logger
def init_logger(module_name, lvl):
    logging.basicConfig(level=lvl)
    log = logging.getLogger(module_name)
    return log
