import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\config.ini")

class readConfig:
    @staticmethod #static means can call this class method without creating object
    def geturl():
        url=config.get('common_info','url')
        return url
        
    @staticmethod
    def getuser():
        user=config.get('common_info','user')
        return user
    @staticmethod 
    def getpwd():
        pwd=config.get('common_info','pwd')
        return pwd