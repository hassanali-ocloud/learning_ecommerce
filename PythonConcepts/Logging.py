import logging

logging.basicConfig(level=logging.DEBUG)
logging.info("App Started")

logger = logging.getLogger("MyAppLogger")
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("MyAppLogFile.log")
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical("App Break down because of failed api call")
logger.debug("Now reverting back to backup cloud")
