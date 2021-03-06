#!/usr/bin/python

BANNER = """
Google Play Unofficial API Interactive Shell
Successfully logged in using your Google account. The variable 'api' holds the API object.
Feel free to use help(api).
"""

import sys
import urlparse
import code
from pprint import pprint
from google.protobuf import text_format

from googleplayapi.config import *
from googleplayapi.googleplay import GooglePlayAPI

api = GooglePlayAPI(ANDROID_ID)
api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)
code.interact(BANNER, local=locals())
