import logging

# Configuring the logging module
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

# '5 default levels of logging'
# logging.debug('this is a debug message.')
# logging.info('this is an info message.')
logging.warning('this is a warning message.')
# logging.error('this is an error message.')
# logging.critical('this is a critical message.')
