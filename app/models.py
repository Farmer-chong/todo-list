# -*- coding: utf-8 -*-
'''
    :file: models.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 13:02:01
'''
from sqlalchemy.sql.expression import false
from app.extensions import db
# 解决无代码提示
import sqlalchemy as sa

class TodoList(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    task = sa.Column(sa.String(255))
    completed = sa.Column(sa.Boolean, default=False)
    
    def save_task(self) -> bool:
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            return False
        return True

    @staticmethod
    def get_tasks():
        return TodoList.query.all()
    