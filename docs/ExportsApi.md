# mux_python.ExportsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_exports**](ExportsApi.md#list_exports) | **GET** /data/v1/exports | List property video view export links
[**list_exports_views**](ExportsApi.md#list_exports_views) | **GET** /data/v1/exports/views | List available property view exports


# **list_exports**
> ListExportsResponse list_exports()

List property video view export links

Deprecated: The API has been replaced by the list-exports-views API call.  Lists the available video view exports along with URLs to retrieve them. 

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.ExportsApi(api_client)
    
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_exports_views**
> ListVideoViewExportsResponse list_exports_views()

List available property view exports

Lists the available video view exports along with URLs to retrieve them.

### Example

* Basic Authentication (accessToken):
```python
from __future__ import print_function
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.mux.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mux_python.Configuration(
    host = "https://api.mux.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: accessToken
configuration = mux_python.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mux_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mux_python.ExportsApi(api_client)
    
    try:
        # List available property view exports
        api_response = api_instance.list_exports_views()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExportsApi->list_exports_views: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVideoViewExportsResponse**](ListVideoViewExportsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

