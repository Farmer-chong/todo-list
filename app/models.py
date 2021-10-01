# -*- coding: utf-8 -*-
'''
    :file: models.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 13:02:01
'''
# 解决无代码提示
import sqlalchemy as sa
from datetime import datetime
from app.extensions import db

GMT_FORMAT =  '%a, %d %b %Y %H:%M:%S GMT'

class TodoList(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    task = sa.Column(sa.String(255))
    completed = sa.Column(sa.Boolean, default=False)
    time = sa.Column(
        sa.DateTime, default=datetime.now, onupdate=datetime.now)

    def save_task(self) -> bool:
        return False
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            return False
        return True

    @staticmethod
    def get_tasks():
        return TodoList.query.all()
    