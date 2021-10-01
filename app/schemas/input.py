# -*- coding: utf-8 -*-
'''
    :file: input.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 15:53:44
'''
from apiflask import Schema
from apiflask.fields import String, Boolean, Integer

class TodoListInSchema(Schema):
    task = String(metadata={'example': 'This is a task description example.'})
    completed = Boolean(metadata={'example': False})

class TodoListUpdateSchema(TodoListInSchema):
    id = Integer()

# class ChangeTodoStatus(schema):
#     id = Integer(default=-1)
#     completed = Boolean(metadata={'example': False})