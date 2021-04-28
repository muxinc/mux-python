# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID_DEV']
configuration.password = os.environ['MUX_TOKEN_SECRET_DEV']

# API Client Initialization
usage_api = mux_python.DeliveryUsageApi(mux_python.ApiClient(configuration))

# ========== list-delivery-usage ==========
# Example with a valid timeframe:
# usage = usage_api.list_delivery_usage(timeframe=['1574175600', '1574305200'])
usage = usage_api.list_delivery_usage()
assert usage != None
assert usage.data != None
print("list-delivery-usage OK ✅")
