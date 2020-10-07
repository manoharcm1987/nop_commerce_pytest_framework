import logging, os, pathlib


class Logger:

    @staticmethod
    def get_logger():

        #path = "C://Old D drive//SeleniumWorkSpace//nop_commerce_pytest_framework//logs//nop_commerce.log"
        path = os.path.join(pathlib.Path(__file__).parent.parent.absolute(), "logs", "nop_commerce.log")
        log_format = "%(asctime)s:: %(levelname)s:  %(filename)s:%(lineno)d    %(message)s"
        date_format = '%m-%d-%Y %I:%M:%S %p'
        #logging.basicConfig(filename=path, format="%(asctime)s:: %(levelname)s:  %(filename)s:%(lineno)d    %(message)s",
                            #datefmt='%m-%d-%Y %I:%M:%S %p', filemode='w+', level=logging.INFO)
        logger = logging.getLogger(__name__)
        handler = logging.FileHandler(path, mode="w+")
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
