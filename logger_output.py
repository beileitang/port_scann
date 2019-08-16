import logging


""" initial the logger """
logger = logging.getLogger()
""" initial the handler save on testing.log file  """
fh_handler = logging.FileHandler("testing.log")
ch_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s","%Y-%m-%d,%H:%M:%S")


""" set the formatter """
fh_handler.setFormatter(formatter)
ch_handler.setFormatter(formatter)
""" adding handler to logger """
logger.addHandler(fh_handler)
logger.addHandler(ch_handler)
""" set the the security level for log """
fh_handler.setLevel(logging.DEBUG)
ch_handler.setLevel(logging.DEBUG)


"""  save on logger.log file  """
logging.basicConfig(filename='logger.log', level=logging.INFO)

logging.getLogger().info("Beilei's logging info message")
logging.getLogger().debug("Beilei's logging debug message")
logging.getLogger().warning("Beilei's logging warning message")
logging.getLogger().error("Beilei's logging error message")
logging.getLogger().critical("Beilei's logging critical message")




