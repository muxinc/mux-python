# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Exercises all export operations:
#   list-filters
#   list-filter-values

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
filters_api = mux_python.FiltersApi(mux_python.ApiClient(configuration))

# List Filters
list_filters_response = filters_api.list_filters()
logger.print_debug('List Filters Response: ' + str(list_filters_response))
assert list_filters_response != None
assert list_filters_response.data != None
assert list_filters_response.data.basic != None
assert list_filters_response.data.advanced != None
print("list-filters OK ✅")

# List Filter Values
list_filter_values_response = filters_api.list_filter_values('browser', timeframe=['7:days'])
logger.print_debug('List Filters Values Response: ' + str(list_filter_values_response))
assert list_filter_values_response != None
assert list_filter_values_response.data != None
print("list-filter-values OK ✅")