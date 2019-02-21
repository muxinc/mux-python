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
filters_api = mux_python.FiltersApi(mux_python.ApiClient(configuration))

# List Filters
print("Listing Filters: \n")

list_filters_response = filters_api.list_filters()

pprint(list_filters_response)

print 'Basic: '
for filter in list_filters_response.data.basic:
    print('Filter: ' + filter)

print "\n"

print 'Advanced: '
for filter in list_filters_response.data.advanced:
    print('Filter: ' + filter)

list_filter_values_response = filters_api.list_filter_values('browser', timeframe=['2:days'])

pprint(list_filter_values_response)