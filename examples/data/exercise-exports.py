# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Exercises all export operations.

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
exports_api = mux_python.ExportsApi(mux_python.ApiClient(configuration))

# ========== list-exports ==========
list_exports_response = exports_api.list_exports()
logger.print_debug('Listed Exports:' + str(list_exports_response))
assert list_exports_response != None
assert list_exports_response.data != None
print("list-exports OK ✅")
