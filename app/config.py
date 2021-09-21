# -*- coding: utf-8 -*-
'''
    :file: config.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 12:50:12
'''

from app.schemas.output import Normal
import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# 基本配置
class BaseConfig(object):
    # 鉴权加密密钥（cookie）
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    # ORM框架配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BASE_RESPONSE_SCHEMA = Normal
    BASE_RESPONSE_DATA_KEY = 'data'

# 开发环境配置
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_ECHO = True
    # 开发环境使用sqlite作为开发数据库
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))

# 测试配置
class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database

# 生产环境配置
class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))

# xport配置
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}