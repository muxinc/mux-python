import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

try:
    assets_api.get_asset("HELLO")
except NotFoundException as e:
    print "Cound not find asset!"
    print "Error Type: " + e.error_type
    print "Error Messages: " + ", ".join(e.error_messages)
