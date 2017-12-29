class BaseConfig:
    """基础配置"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """开发环境配置"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """测试环境配置"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """生产环境配置"""
    DEBUG = False
