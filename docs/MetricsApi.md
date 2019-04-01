# mux_python.MetricsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metric_timeseries_data**](MetricsApi.md#get_metric_timeseries_data) | **GET** /data/v1/metrics/{METRIC_ID}/timeseries | Get metric timeseries data
[**get_overall_values**](MetricsApi.md#get_overall_values) | **GET** /data/v1/metrics/{METRIC_ID}/overall | Get Overall values
[**list_all_metric_values**](MetricsApi.md#list_all_metric_values) | **GET** /data/v1/metrics/comparison | List all metric values
[**list_breakdown_values**](MetricsApi.md#list_breakdown_values) | **GET** /data/v1/metrics/{METRIC_ID}/breakdown | List breakdown values
[**list_insights**](MetricsApi.md#list_insights) | **GET** /data/v1/metrics/{METRIC_ID}/insights | List Insights


# **get_metric_timeseries_data**
> GetMetricTimeseriesDataResponse get_metric_timeseries_data(metric_id, timeframe=timeframe, filters=filters, measurement=measurement, order_direction=order_direction, group_by=group_by)

Get metric timeseries data

Returns timeseries data for a specific metric 

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
api_instance = mux_python.MetricsApi(mux_python.ApiClient(configuration))
metric_id = video_startup_time # str | ID of the Metric
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days.  (optional)
filters = ['filters_example'] # list[str] | Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint.  (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the deafult for the metric will be used. (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
group_by = 'group_by_example' # str | Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the supplied timeframe. (optional)

try:
    # Get metric timeseries data
    api_response = api_instance.get_metric_timeseries_data(metric_id, timeframe=timeframe, filters=filters, measurement=measurement, order_direction=order_direction, group_by=group_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_metric_timeseries_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600    * duration string e.g. timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days.  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;country:US).  Possible filter names are the same as returned by the List Filters endpoint.  | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the deafult for the metric will be used. | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **group_by** | **str**| Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the supplied timeframe. | [optional] 

### Return type

[**GetMetricTimeseriesDataResponse**](GetMetricTimeseriesDataResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_overall_values**
> GetOverallValuesResponse get_overall_values(metric_id, timeframe=timeframe, filters=filters, measurement=measurement)

Get Overall values

Returns the overall value for a specific metric, as well as the total view count, watch time, and the Mux Global metric value for the metric. 

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
api_instance = mux_python.MetricsApi(mux_python.ApiClient(configuration))
metric_id = video_startup_time # str | ID of the Metric
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days.  (optional)
filters = ['filters_example'] # list[str] | Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint.  (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the deafult for the metric will be used. (optional)

try:
    # Get Overall values
    api_response = api_instance.get_overall_values(metric_id, timeframe=timeframe, filters=filters, measurement=measurement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->get_overall_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600    * duration string e.g. timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days.  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;country:US).  Possible filter names are the same as returned by the List Filters endpoint.  | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the deafult for the metric will be used. | [optional] 

### Return type

[**GetOverallValuesResponse**](GetOverallValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_metric_values**
> ListAllMetricValuesResponse list_all_metric_values(timeframe=timeframe, filters=filters, dimension=dimension, value=value)

List all metric values

List all of the values across every breakdown for a specific metric 

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
api_instance = mux_python.MetricsApi(mux_python.ApiClient(configuration))
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days.  (optional)
filters = ['filters_example'] # list[str] | Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint.  (optional)
dimension = 'dimension_example' # str | Dimension the specified value belongs to (optional)
value = 'value_example' # str | Value to show all available metrics for (optional)

try:
    # List all metric values
    api_response = api_instance.list_all_metric_values(timeframe=timeframe, filters=filters, dimension=dimension, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->list_all_metric_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600    * duration string e.g. timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days.  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;country:US).  Possible filter names are the same as returned by the List Filters endpoint.  | [optional] 
 **dimension** | **str**| Dimension the specified value belongs to | [optional] 
 **value** | **str**| Value to show all available metrics for | [optional] 

### Return type

[**ListAllMetricValuesResponse**](ListAllMetricValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_breakdown_values**
> ListBreakdownValuesResponse list_breakdown_values(metric_id, group_by=group_by, measurement=measurement, filters=filters, limit=limit, page=page, order_by=order_by, order_direction=order_direction, timeframe=timeframe)

List breakdown values

List the breakdown values for a specific metric 

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
api_instance = mux_python.MetricsApi(mux_python.ApiClient(configuration))
metric_id = video_startup_time # str | ID of the Metric
group_by = 'group_by_example' # str | Breakdown value to group the results by (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the deafult for the metric will be used. (optional)
filters = ['filters_example'] # list[str] | Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint.  (optional)
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days.  (optional)

try:
    # List breakdown values
    api_response = api_instance.list_breakdown_values(metric_id, group_by=group_by, measurement=measurement, filters=filters, limit=limit, page=page, order_by=order_by, order_direction=order_direction, timeframe=timeframe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->list_breakdown_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **group_by** | **str**| Breakdown value to group the results by | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the deafult for the metric will be used. | [optional] 
 **filters** | [**list[str]**](str.md)| Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;country:US).  Possible filter names are the same as returned by the List Filters endpoint.  | [optional] 
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600    * duration string e.g. timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days.  | [optional] 

### Return type

[**ListBreakdownValuesResponse**](ListBreakdownValuesResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_insights**
> ListInsightsResponse list_insights(metric_id, measurement=measurement, order_direction=order_direction, timeframe=timeframe)

List Insights

Returns a list of insights for a metric. These are the worst performing values across all breakdowns sorted by how much they negatively impact a specific metric. 

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
api_instance = mux_python.MetricsApi(mux_python.ApiClient(configuration))
metric_id = video_startup_time # str | ID of the Metric
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the deafult for the metric will be used. (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days.  (optional)

try:
    # List Insights
    api_response = api_instance.list_insights(metric_id, measurement=measurement, order_direction=order_direction, timeframe=timeframe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->list_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the deafult for the metric will be used. | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600    * duration string e.g. timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days.  | [optional] 

### Return type

[**ListInsightsResponse**](ListInsightsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

