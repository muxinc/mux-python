# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Exercises all error operations.

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
errors_api = mux_python.ErrorsApi(mux_python.ApiClient(configuration))

# ========== list-errors ==========
list_errors_response = errors_api.list_errors(filters=['browser:Safari'], timeframe=['7:days'])
logger.print_debug('List Errors Response: ' + str(list_errors_response))
assert list_errors_response != None
assert list_errors_response.data != None
assert list_errors_response.data[0].id != None
print("list-errors OK ✅")
