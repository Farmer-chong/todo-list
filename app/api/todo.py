# -*- coding: utf-8 -*-
'''
    :file: todo.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 12:55:13
'''

from app.schemas.output import TodoListOutSchema
from app.models import TodoList
from app.schemas.input import TodoListInSchema
from app.utils import make_resp
from apiflask import APIBlueprint, output, input
from flask.views import MethodView

todo_bp = APIBlueprint('todo', __name__)


@todo_bp.route("/")
class TodoViews(MethodView):

    @output(TodoListOutSchema(many=True))
    def get(self):
        todos = TodoList.get_tasks()
        print(todos)
        return make_resp(data=todos)

    @input(TodoListInSchema)
    @output(TodoListOutSchema)
    def put(self, todo_item):
        return make_resp(data=todo_item)

    @input(TodoListInSchema)
    def patch(self, todo_item):
        return make_resp(data=todo_item)

