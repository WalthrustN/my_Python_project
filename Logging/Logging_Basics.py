import logging
import HelperLog

# Configuring the logging module
logging.basicConfig(level=logging.DEBUG,
                    format='function name%(funcName)s- level number %(levelno)s- line %(lineno)s- date%(asctime)s-'
                           ' logger %(name)s-'
                           '\nfilename %(filename)s-module %(module)s-''%(levelname)s-%(message)s-pathname %(pathname)s-'
                           '\nprocess %(process)d-process name %(processName)s- thread %(thread)d- thread name %(threadName)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

# '5 default levels of logging'
# logging.debug('this is a debug message.')
# logging.info('this is an info message.')
# logging.warning('this is a warning message.')
# logging.error('this is an error message.')
# logging.critical('this is a critical message.')

# using %s as placeholders
logging.warning('%s before you %s', 'Look', 'leap!')

HelperLog.logger.warning('This is a warning for my Helper Log')
