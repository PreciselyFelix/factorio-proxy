import atexit
import json
import logging.config
import os

FACTORIO_LOGGER = logging.getLogger("FactorioProxy")

def setup_logging() -> None:
    if not os.path.exists("logs"):
        os.makedirs("logs")
    with open("logger_config.json") as f:
        config = json.load(f)
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)

class ErrorLogWriter():
    def write(message: str):
        message = message.replace('\n', ' ')
        FACTORIO_LOGGER.error(message)