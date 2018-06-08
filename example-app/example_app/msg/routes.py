# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.get_msg import GetMsg
from .api.add_msg import AddMsg


routes = [
    dict(resource=GetMsg, urls=['/get_msg'], endpoint='get_msg'),
    dict(resource=AddMsg, urls=['/add_msg'], endpoint='add_msg'),
]