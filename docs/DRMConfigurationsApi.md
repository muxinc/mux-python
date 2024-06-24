# mux_python.DRMConfigurationsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drm_configuration**](DRMConfigurationsApi.md#get_drm_configuration) | **GET** /video/v1/drm-configurations/{DRM_CONFIGURATION_ID} | Retrieve a DRM Configuration
[**list_drm_configurations**](DRMConfigurationsApi.md#list_drm_configurations) | **GET** /video/v1/drm-configurations | List DRM Configurations


# **get_drm_configuration**
> DRMConfigurationResponse get_drm_configuration(drm_configuration_id)

Retrieve a DRM Configuration

Retrieves a single DRM Configuration.

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
    api_instance = mux_python.DRMConfigurationsApi(api_client)
    drm_configuration_id = 'drm_configuration_id_example' # str | The DRM Configuration ID.

    try:
        # Retrieve a DRM Configuration
        api_response = api_instance.get_drm_configuration(drm_configuration_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DRMConfigurationsApi->get_drm_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drm_configuration_id** | **str**| The DRM Configuration ID. | 

### Return type

[**DRMConfigurationResponse**](DRMConfigurationResponse.md)

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

# **list_drm_configurations**
> ListDRMConfigurationsResponse list_drm_configurations(page=page, limit=limit)

List DRM Configurations

Returns a list of DRM Configurations

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
    api_instance = mux_python.DRMConfigurationsApi(api_client)
    page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
limit = 25 # int | Number of items to include in the response (optional) (default to 25)

    try:
        # List DRM Configurations
        api_response = api_instance.list_drm_configurations(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DRMConfigurationsApi->list_drm_configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]

### Return type

[**ListDRMConfigurationsResponse**](ListDRMConfigurationsResponse.md)

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

