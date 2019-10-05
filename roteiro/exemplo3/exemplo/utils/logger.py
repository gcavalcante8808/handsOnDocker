import logging


class HandlerSpy(logging.Handler):
    def emit(self, record):
        self.last_message = record.msg


def get_stream_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    logger.addHandler(console_handler)

    return logger


def get_test_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = HandlerSpy()
    logger.handlers = []
    logger.addHandler(handler)

    return logger
