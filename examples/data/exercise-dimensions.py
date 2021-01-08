# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
dimensions_api = mux_python.DimensionsApi(mux_python.ApiClient(configuration))

# ========== list-dimensions ==========
dimensions = dimensions_api.list_dimensions()
logger.print_debug('List Dimensions Response: ' + str(dimensions))
assert dimensions != None
assert dimensions.data != None
assert dimensions.data.basic != None
assert dimensions.data.advanced != None
print("list-dimensions OK ✅")

# ========== list-dimension-values ==========
dimension_values = dimensions_api.list_dimension_values('browser', timeframe=['7:days'])
logger.print_debug('List Dimension Values Response: ' + str(dimension_values))
assert dimension_values != None
assert dimension_values.data != None
print("list-filter-dimension_values OK ✅")
