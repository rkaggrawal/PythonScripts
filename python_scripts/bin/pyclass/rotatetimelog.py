import logging
import time

from logging.handlers import TimedRotatingFileHandler


# ----------------------------------------------------------------------
def create_timed_rotating_log(path):
    """"""
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(path,
                                       when="s",
                                       interval=5,
                                       backupCount=5)
    logger.addHandler(handler)

    for i in range(6):
        logger.info("This is a test!")
        time.sleep(7)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    log_file = "logs/timed.log"
    create_timed_rotating_log(log_file)



# second (s)
# minute (m)
# hour (h)
# day (d)
# w0-w6 (weekday, 0=Monday)