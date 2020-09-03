import logging


class Logger:

    @staticmethod
    def get_logger():
        logging.basicConfig(filename=".//logs//nop_commerce.log", format="%(asctime)s:: %(levelname)s:  %(filename)s:%(lineno)d    %(message)s",
                            datefmt='%m-%d-%Y %I:%M:%S %p', filemode='w')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
