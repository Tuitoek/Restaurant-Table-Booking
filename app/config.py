import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='a77302eea2d2'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:sarahjt12@localhost/tblog'
    SQLALCHEMY_TRACK_MODIFICATIONS =False

    #  email configurations
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
