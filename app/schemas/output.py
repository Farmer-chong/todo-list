# -*- coding: utf-8 -*-
'''
    :file: output.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 15:53:39
'''
from apiflask import Schema
from apiflask.fields import Integer, String, Field, Boolean


class Normal(Schema):
    status_code = Integer(metadata={'example': 200})
    message = String(metadata={'example': 'response message'})
    data = Field()


class TodoListOutSchema(Schema):
    id = Integer()
    task = String(metadata={'example': 'This is a task description example.'})
    completed = Boolean(metadata={'example': False})