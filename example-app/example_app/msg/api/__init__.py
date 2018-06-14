# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

from ..validators import request_validate, response_filter


class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]



# # -*- coding: utf-8 -*-
# from __future__ import absolute_import
#
# import msg
#
# from flask import Flask
#
#
# def create_app():
#     app = Flask(__name__, static_folder='static')
#     app.register_blueprint(
#         msg.bp,
#         url_prefix='/msg')
#     return app
#
# if __name__ == '__main__':
#     create_app().run(debug=True)