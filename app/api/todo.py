# -*- coding: utf-8 -*-
'''
    :file: todo.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 12:55:13
'''

from app.utils import make_resp
from apiflask import APIBlueprint
from flask.views import MethodView

todo_bp = APIBlueprint('todo', __name__)


@todo_bp.route("/")
class TodoViews(MethodView):

    def get(self):
        return make_resp(message="get")

    def post(self):
        return make_resp(message="post")

    def put(self):
        return make_resp(message="put")

    def patch(self):
        return make_resp(message="patch")

