# -*- coding: utf-8 -*-
'''
    :file: output.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 15:53:39
'''
from apiflask import Schema
from apiflask.fields import Integer, String, Field, Boolean, DateTime
# from flask_marshmallow

class Normal(Schema):
    status_code = Integer(metadata={'example': 200})
    message = String(metadata={'example': 'response message'})
    data = Field()


def camelcase(s):
    parts = iter(s.split("_"))
    return next(parts) + "".join(i.title() for i in parts)

class TodoListOutSchema(Schema):
    id = Integer()
    task = String(metadata={'example': 'This is a task description example.'})
    completed = Boolean(metadata={'example': False})
    time = DateTime('%a, %d %b %Y %H:%M:%S GMT', data_key="LastTime")

    # def on_bind_field(self, field_name: str, field_obj) -> None:
    #     field_obj.data_key = camelcase(field_obj.data_key or field_name)


        # return super().on_bind_field(field_name, field_obj)
    # @property
    # def time(self):
    #     return self._time.toString("r")
    #     pass