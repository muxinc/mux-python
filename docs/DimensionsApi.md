# mux_python.DimensionsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dimension_values**](DimensionsApi.md#list_dimension_values) | **GET** /data/v1/dimensions/{DIMENSION_ID} | Lists the values for a specific dimension
[**list_dimensions**](DimensionsApi.md#list_dimensions) | **GET** /data/v1/dimensions | List Dimensions


# **list_dimension_values**
> ListDimensionValuesResponse list_dimension_values(dimension_id, limit=limit, page=page, filters=filters, metric_filters=metric_filters, timeframe=timeframe)

Lists the values for a specific dimension

Lists the values for a dimension along with a total count of related views.  Note: This API replaces the list-filter-values API call. 

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
    api_instance = mux_python.DimensionsApi(api_client)
    dimension_id = 'abcd1234' # str | ID of the Dimension
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
filters = ['filters_example'] # list[str] | Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a `!` character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * `filters[]=operating_system:windows&filters[]=!country:US`  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # Lists the values for a specific dimension
        api_response = api_instance.list_dimension_values(dimension_id, limit=limit, page=page, filters=filters, metric_filters=metric_filters, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DimensionsApi->list_dimension_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dimension_id** | **str**| ID of the Dimension | 
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **filters** | [**list[str]**](str.md)| Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60;  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListDimensionValuesResponse**](ListDimensionValuesResponse.md)

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

# **list_dimensions**
> ListDimensionsResponse list_dimensions()

List Dimensions

List all available dimensions.  Note: This API replaces the list-filters API call. 

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
    api_instance = mux_python.DimensionsApi(api_client)
    
    try:
        # List Dimensions
        api_response = api_instance.list_dimensions()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DimensionsApi->list_dimensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDimensionsResponse**](ListDimensionsResponse.md)

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

