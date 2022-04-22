# using a try , except to log an error message
import logging
import traceback

try:
    a = [1, 2, 3]
    val = a[4]

# except IndexError as e:
#   logging.error(e, exc_info=True)  # this shows the traceback and the line number in the log.

# logging any error and using trackback for more info
except:
    logging.error('the error is %s', traceback.format_exc())
