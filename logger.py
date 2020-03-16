import logging


def init_logger(module_name, lvl):
    # Instantiate the logger
    logging.basicConfig(level=lvl)
    log = logging.getLogger(module_name)
    return log
