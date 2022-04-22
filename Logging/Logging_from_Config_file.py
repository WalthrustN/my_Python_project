# This file used to use a logger created in another file, but it doesnt work properly now. It used to work fine.
# This method is an older way to do it. instead of logging.config.fileConfig, now there is logging.config.dictConfig
import logging
import logging.config

logging.config.fileConfig("logging.conf")

logger = logging.getLogger('simpleExample')

logger.error('this is a waring message')
