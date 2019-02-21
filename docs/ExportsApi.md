# mux_python.ExportsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_exports**](ExportsApi.md#list_exports) | **GET** /data/v1/exports | List property video view export links


# **list_exports**
> ListExportsResponse list_exports()

List property video view export links

Lists the available video view exports along with URLs to retrieve them 

### Example

* Basic Authentication (accessToken): 
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
configuration = mux_python.Configuration()
# Configure HTTP basic authorization: accessToken
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mux_python.ExportsApi(mux_python.ApiClient(configuration))

try:
    # List property video view export links
    api_response = api_instance.list_exports()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportsApi->list_exports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListExportsResponse**](ListExportsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

