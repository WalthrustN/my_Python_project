import logging
# from logging.handlers import RotatingFileHandler\
from logging.handlers import TimedRotatingFileHandler  ##timed
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# s, m, h, d, midnight, w0= monday,
handler = TimedRotatingFileHandler('timed test log', when='s', interval=5, backupCount=5)

# roll over after 2KB, and keep back up logs - app.log.1, app.log.2, etc, to app.log.5.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount= 5)
logger.addHandler(handler)

for _ in range(5):
    logger.info('hello world')
    time.sleep(300)
