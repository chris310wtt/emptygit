# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

from . import Resource

import connexion

import json

import pymysql.cursors

app = connexion.App(__name__)

class GetMsg(Resource):

    def get(Product_Line_Id=None):
        print(g.args)
        conn = pymysql.connect(host='192.168.1.254', user='root', password='111111', database='testwutt',
                               charset='utf8')
        cursor = conn.cursor()
        sql_select = '''select  MESSAGE_NAME,
                                            MESSAGE_CONTENT
                                            from SYSTEM_MESSAGE
                                            # where PRODUCT_LINE_ID = % s ''' % (Product_Line_Id)
        print(sql_select)
        cursor.execute(sql_select)
        values = cursor.fetchall()
        print(values)
        print(type(values))
        # 字段含中文转成json串解决办法ensure_ascii=False
        j = json.dumps(values, ensure_ascii=False)
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        conn.close()
        return {"系统信息": j}, 200, None