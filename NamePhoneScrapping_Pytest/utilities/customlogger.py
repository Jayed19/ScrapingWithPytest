import logging
LOG_FILENAME = ".\\logs\\automation.log"
class LogGen:
    @staticmethod
    def logwrite():
        import logging
        logging.basicConfig(filename=LOG_FILENAME ,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        
        return logger