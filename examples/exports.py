import os
import mux_python
from mux_python.rest import ApiException
from pprint import pprint

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']
configuration.debug = True

# API Client Initialization
exports_api = mux_python.ExportsApi(mux_python.ApiClient(configuration))

# List Exports
print("Listing Exports: \n")

list_exports_response = exports_api.list_exports()

pprint(list_exports_response)
