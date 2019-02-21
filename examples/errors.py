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
errors_api = mux_python.ErrorsApi(mux_python.ApiClient(configuration))

# List Errors
print("Listing Errors: \n")

# You can only filter by one dimension on the errrors API it seems...
list_errors_response = errors_api.list_errors(filters=['browser:Firefox'], timeframe=['1:hours'])

pprint(list_errors_response)

for error in list_errors_response.data:
    print('ID: ' + str(error.id))
    print "\n"
