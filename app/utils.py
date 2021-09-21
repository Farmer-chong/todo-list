# -*- coding: utf-8 -*-
'''
    :file: utils.py
    :author: -Farmer
    :url: https://blog.farmer233.top
    :date: 2021/09/21 16:37:12
'''
from typing import Any, Dict


def make_resp(status_code: int = 200, message: str = "ok", data: Any = None) -> Dict:
    return {
        "status_code": status_code,
        "message": message,
        "data": data
    }
