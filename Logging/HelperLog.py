# ? .info logs not reporting
import logging

# create own internal logger (not the root logger)
logger = logging.getLogger(__name__)

logger.propagate = False

logging.basicConfig(level=logging.DEBUG,
                    format='function name%(funcName)s- level number %(levelno)s- line %(lineno)s- date%(asctime)s-'
                           ' logger %(name)s-'
                           '\nfilename %(filename)s-module %(module)s-''%(levelname)s-%(message)s-pathname %(pathname)s-',
                    # '\nprocess %(process)d-process name %(processName)s- thread %(thread)d- thread name %(threadName)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

logger.warning('this is a warning')
logger.info('hello from helper')

# Propagate: Decides whether a log should be propagated to the logger's parent
