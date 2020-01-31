import logging

def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')

class Bar(object):
    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')
        self.logger.log(20,'Hi, sdfsdf')
        self.logger.debug("Debug, bar")
        self.logger.warning("Warning,bar")
        self.logger.error("Error, bar")
        self.logger.critical("Critical, bar")
