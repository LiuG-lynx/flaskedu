# encoding: utf-8

class BaseConfig(object):
    """配置基类"""
    SECRET_KEY = 'make sure to set a very secret key'



class DevelopmentConfig(BaseConfig):
    """ 开发环境配置 """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/simpledu?charset=utf8'


class ProductionConfig(BaseConfig):
    """ 生产环境"""
    pass


class TestingConfig(BaseConfig):
    """ 测试环境配置"""
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}