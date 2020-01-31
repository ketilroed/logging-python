import logging.config
import json
import os
# load my module
import my_module


# Levels can be found here: https://docs.python.org/3/library/logging.html#levels
#Order of verbosity: NOTSET,DEBUG,INFO,WARNING,ERROR,CRITICAL
def setup_logging(default_path='logging.json',default_level=logging.DEBUG,env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value: #Check if LOG_CFG is provided as part of execution line, see *
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()

# load the logging configuration
#logging.config.fileConfig('logging.ini')
logger = logging.getLogger(__name__)

my_module.foo()
bar = my_module.Bar()
bar.bar()
#logger.info("info-test")
#logger.error("error-test")
logger.debug("debug-test")

# * LOG_CFG=my_logging.json python3 main.py
