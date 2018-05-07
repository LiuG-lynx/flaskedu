# encoding: utf-8
# __author__ : poet
# Date: 2018/5/7

from flask import Blueprint

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/')
def main_index():
    return 'admin'
