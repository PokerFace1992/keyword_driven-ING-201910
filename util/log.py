#encoding=utf-8
import logging.config
import logging
from proj_var.var import ProjDirPath
print(ProjDirPath+"\\conf\\"+"logger.conf")
logging.config.fileConfig(ProjDirPath+"\\conf\\"+"logger.conf")
logger = logging.getLogger("example01")


def debug(message):
    print ("debug")
    logger.debug(message)


def warning(message):
    logger.warning(message)


def info(message):
    logger.info(message)

def error(message):
    logger.error(message)

if __name__=="__main__":
    debug("hi")
    info("hello,world")
    warning("hello")