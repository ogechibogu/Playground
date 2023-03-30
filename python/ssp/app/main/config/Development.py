from .GlobalConfig import GlobalConfig


class Development(GlobalConfig):
    ENV = 'development'
    DEBUG = True
