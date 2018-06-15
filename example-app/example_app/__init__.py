# # -*- coding: utf-8 -*-
# from __future__ import absolute_import
#
# import msg
# import msg.api.get_msg
# from flask import Flask
#
# def create_app():
#     app = Flask(__name__, static_folder='static')
#     app.register_blueprint(
#         msg.bp,
#         url_prefix='/msg')
#     return app
#
# if __name__ == '__main__':
#     msg.api.get_msg().run(debug=True)

# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

import msg

import msg.api.get_msg

def create_app():
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        msg.bp,
        url_prefix='/msg')
    return app

if __name__ == '__main__':
    create_app().run(debug=True)