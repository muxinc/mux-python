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
incidents_api = mux_python.IncidentsApi(mux_python.ApiClient(configuration))

# Test coverage here is poor due to not knowning if the account we're testing against has any incidents.

# ========== list-incidents ==========
incidents = incidents_api.list_incidents()
logger.print_debug('List Incidents Response: ' + str(incidents))
assert incidents != None
assert incidents.data != None
print("list-incidents OK ✅")

# ========== get-incident ==========
print("get-incident SKIP ⚠️")

# ========== list-related-incidents ==========
print("list-related-incidents SKIP ⚠️")
