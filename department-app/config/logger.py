"""Logger init and config"""

import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("app.log", 'w+')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)
