#!/usr/bin/python

import sys
from pprint import pprint

from googleplayapi.config import *
from googleplayapi.googleplay import GooglePlayAPI
from googleplayapi.helpers import sizeof_fmt

if (len(sys.argv) < 2):
    print "Usage: %s packagename [filename]"
    print "Download an app."
    print "If filename is not present, will write to packagename.apk."
    sys.exit(0)

packagename = sys.argv[1]

if (len(sys.argv) == 3):
    filename = sys.argv[2]
else:
    filename = packagename + ".apk"

# Connect
api = GooglePlayAPI(androidId=ANDROID_ID, email=GOOGLE_LOGIN, password=GOOGLE_PASSWORD, authSubToken=AUTH_TOKEN)

# login if necessary
if not AUTH_TOKEN:
    # api.login(GOOGLE_LOGIN, GOOGLE_PASSWORD, AUTH_TOKEN)
    api.login()

# Get the version code and the offer type from the app details
m = api.details(packagename)
doc = m.docV2
vc = doc.details.appDetails.versionCode
ot = doc.offer[0].offerType

# Download
print "Downloading %s..." % sizeof_fmt(doc.details.appDetails.installationSize),
data = api.download(packagename, vc, ot)
open(filename, "wb").write(data)
print "Done"

