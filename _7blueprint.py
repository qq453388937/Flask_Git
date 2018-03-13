# -*- coding:utf-8 -*-

from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/list')
def list():
    return 'list'


@api.route('/list2')
def list2():
    return 'list2'