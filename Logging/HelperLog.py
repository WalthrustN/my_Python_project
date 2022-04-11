import logging

# create own internal logger (not the root logger)
logger = logging.getLogger(__name__)
logger.propagate = False

logger.info('hello from helper')

# Propagate: Decides whether a log should be propagated to the logger's parent
