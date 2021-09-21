# -*- coding: utf-8 -*-
'''
    :file: app.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 12:44:37
'''

import os
from apiflask import APIFlask, abort
from app.config import config
from app.extensions import db, cors
from app.api.todo import todo_bp

def create_app(config_name:str=None) -> APIFlask:
    """构造工厂

    Args:
        config_name (str, optional): 配置文件名. Defaults to None.

    Returns:
        APIFlask: falsk app 实例
    """
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = APIFlask(__name__)
    app.config.from_object(config[config_name])

    register_extensions(app)
    register_blueprints(app)
    register_errors(app)
    register_commands(app)

    return app


def register_extensions(app:APIFlask):
    """初始化扩展

    Args:
        app (APIFlask): flask app 实例
    """
    db.init_app(app)
    cors.init_app(app)


def register_blueprints(app:APIFlask):
    app.register_blueprint(todo_bp, url_prefix="/")

def register_errors(app:APIFlask):
    pass
    # @app.errorhandler(Exception)
    # def internal_server_error(e):
    #     abort(500, message=str(e))


def register_commands(app:APIFlask):
    @app.cli.command()
    def initdb():
        db.drop_all()
        db.create_all()


