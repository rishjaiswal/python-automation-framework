import logging
import os
from configs import config


def get_logger():
    log = logging.getLogger('mainlgr')
    os.chdir(os.path.join(config.PROJECT_PATH, config.LOGS_PATH))
    logging.basicConfig(filename='automation.log',
                        format='[%(levelname)s] %(asctime)s %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO, filemode='w')
    os.chdir(config.PROJECT_PATH)
    return log
