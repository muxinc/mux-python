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
> GetMetricTimeseriesDataResponse get_metric_timeseries_data(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement, order_direction=order_direction, group_by=group_by)

Get metric timeseries data

Returns timeseries data for a specific metric.  Each interval represented in the data array contains an array with the following values:   * the first element is the interval time   * the second element is the calculated metric value   * the third element is the number of views in the interval that have a valid metric value 

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
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * `filters[]=dimension:value` - Include rows where dimension equals value * `filters[]=!dimension:value` - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * `filters[]=+dimension:value` - Include rows where trace contains value * `filters[]=-dimension:value` - Exclude rows where trace contains value * `filters[]=dimension:[value1,value2]` - Exact trace match  **Examples:** * `filters[]=country:US` - US views only * `filters[]=+video_cdn_trace:fastly` - Views using Fastly CDN  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
group_by = 'group_by_example' # str | Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the timeframe.  For timeframes of less than 90 minutes, the default granularity is `minute`. Between 90 minutes and 6 hours, the default granularity is `ten_minutes`. Between 6 hours and 15 days inclusive, the default granularity is `hour`. The granularity of timeframes that exceed 15 days is `day`. This default behavior is subject to change; it is strongly suggested that you explicitly specify the granularity.  (optional)

    try:
        # Get metric timeseries data
        api_response = api_instance.get_metric_timeseries_data(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement, order_direction=order_direction, group_by=group_by)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_metric_timeseries_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * &#x60;filters[]&#x3D;dimension:value&#x60; - Include rows where dimension equals value * &#x60;filters[]&#x3D;!dimension:value&#x60; - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * &#x60;filters[]&#x3D;+dimension:value&#x60; - Include rows where trace contains value * &#x60;filters[]&#x3D;-dimension:value&#x60; - Exclude rows where trace contains value * &#x60;filters[]&#x3D;dimension:[value1,value2]&#x60; - Exact trace match  **Examples:** * &#x60;filters[]&#x3D;country:US&#x60; - US views only * &#x60;filters[]&#x3D;+video_cdn_trace:fastly&#x60; - Views using Fastly CDN  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **group_by** | **str**| Time granularity to group results by. If this value is omitted, a default granularity is chosen based on the timeframe.  For timeframes of less than 90 minutes, the default granularity is &#x60;minute&#x60;. Between 90 minutes and 6 hours, the default granularity is &#x60;ten_minutes&#x60;. Between 6 hours and 15 days inclusive, the default granularity is &#x60;hour&#x60;. The granularity of timeframes that exceed 15 days is &#x60;day&#x60;. This default behavior is subject to change; it is strongly suggested that you explicitly specify the granularity.  | [optional] 

### Return type

[**GetMetricTimeseriesDataResponse**](GetMetricTimeseriesDataResponse.md)

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

# **get_overall_values**
> GetOverallValuesResponse get_overall_values(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement)

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
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * `filters[]=dimension:value` - Include rows where dimension equals value * `filters[]=!dimension:value` - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * `filters[]=+dimension:value` - Include rows where trace contains value * `filters[]=-dimension:value` - Exclude rows where trace contains value * `filters[]=dimension:[value1,value2]` - Exact trace match  **Examples:** * `filters[]=country:US` - US views only * `filters[]=+video_cdn_trace:fastly` - Views using Fastly CDN  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)

    try:
        # Get Overall values
        api_response = api_instance.get_overall_values(metric_id, timeframe=timeframe, filters=filters, metric_filters=metric_filters, measurement=measurement)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->get_overall_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * &#x60;filters[]&#x3D;dimension:value&#x60; - Include rows where dimension equals value * &#x60;filters[]&#x3D;!dimension:value&#x60; - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * &#x60;filters[]&#x3D;+dimension:value&#x60; - Include rows where trace contains value * &#x60;filters[]&#x3D;-dimension:value&#x60; - Exclude rows where trace contains value * &#x60;filters[]&#x3D;dimension:[value1,value2]&#x60; - Exact trace match  **Examples:** * &#x60;filters[]&#x3D;country:US&#x60; - US views only * &#x60;filters[]&#x3D;+video_cdn_trace:fastly&#x60; - Views using Fastly CDN  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 

### Return type

[**GetOverallValuesResponse**](GetOverallValuesResponse.md)

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

# **list_all_metric_values**
> ListAllMetricValuesResponse list_all_metric_values(timeframe=timeframe, filters=filters, metric_filters=metric_filters, dimension=dimension, value=value)

List all metric values

List all of the values across every breakdown for a specific metric.

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
    api_instance = mux_python.MetricsApi(api_client)
    timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * `filters[]=dimension:value` - Include rows where dimension equals value * `filters[]=!dimension:value` - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * `filters[]=+dimension:value` - Include rows where trace contains value * `filters[]=-dimension:value` - Exclude rows where trace contains value * `filters[]=dimension:[value1,value2]` - Exact trace match  **Examples:** * `filters[]=country:US` - US views only * `filters[]=+video_cdn_trace:fastly` - Views using Fastly CDN  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
dimension = 'dimension_example' # str | Dimension the specified value belongs to (optional)
value = 'value_example' # str | Value to show all available metrics for (optional)

    try:
        # List all metric values
        api_response = api_instance.list_all_metric_values(timeframe=timeframe, filters=filters, metric_filters=metric_filters, dimension=dimension, value=value)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_all_metric_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * &#x60;filters[]&#x3D;dimension:value&#x60; - Include rows where dimension equals value * &#x60;filters[]&#x3D;!dimension:value&#x60; - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * &#x60;filters[]&#x3D;+dimension:value&#x60; - Include rows where trace contains value * &#x60;filters[]&#x3D;-dimension:value&#x60; - Exclude rows where trace contains value * &#x60;filters[]&#x3D;dimension:[value1,value2]&#x60; - Exact trace match  **Examples:** * &#x60;filters[]&#x3D;country:US&#x60; - US views only * &#x60;filters[]&#x3D;+video_cdn_trace:fastly&#x60; - Views using Fastly CDN  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **dimension** | **str**| Dimension the specified value belongs to | [optional] 
 **value** | **str**| Value to show all available metrics for | [optional] 

### Return type

[**ListAllMetricValuesResponse**](ListAllMetricValuesResponse.md)

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

# **list_breakdown_values**
> ListBreakdownValuesResponse list_breakdown_values(metric_id, group_by=group_by, measurement=measurement, filters=filters, metric_filters=metric_filters, limit=limit, page=page, order_by=order_by, order_direction=order_direction, timeframe=timeframe)

List breakdown values

List the breakdown values for a specific metric.

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
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
group_by = 'group_by_example' # str | Breakdown value to group the results by (optional)
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)
filters = ['filters_example'] # list[str] | Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * `filters[]=dimension:value` - Include rows where dimension equals value * `filters[]=!dimension:value` - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * `filters[]=+dimension:value` - Include rows where trace contains value * `filters[]=-dimension:value` - Exclude rows where trace contains value * `filters[]=dimension:[value1,value2]` - Exact trace match  **Examples:** * `filters[]=country:US` - US views only * `filters[]=+video_cdn_trace:fastly` - Views using Fastly CDN  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
order_by = 'order_by_example' # str | Value to order the results by (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # List breakdown values
        api_response = api_instance.list_breakdown_values(metric_id, group_by=group_by, measurement=measurement, filters=filters, metric_filters=metric_filters, limit=limit, page=page, order_by=order_by, order_direction=order_direction, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_breakdown_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **group_by** | **str**| Breakdown value to group the results by | [optional] 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * &#x60;filters[]&#x3D;dimension:value&#x60; - Include rows where dimension equals value * &#x60;filters[]&#x3D;!dimension:value&#x60; - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * &#x60;filters[]&#x3D;+dimension:value&#x60; - Include rows where trace contains value * &#x60;filters[]&#x3D;-dimension:value&#x60; - Exclude rows where trace contains value * &#x60;filters[]&#x3D;dimension:[value1,value2]&#x60; - Exact trace match  **Examples:** * &#x60;filters[]&#x3D;country:US&#x60; - US views only * &#x60;filters[]&#x3D;+video_cdn_trace:fastly&#x60; - Views using Fastly CDN  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **order_by** | **str**| Value to order the results by | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListBreakdownValuesResponse**](ListBreakdownValuesResponse.md)

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

# **list_insights**
> ListInsightsResponse list_insights(metric_id, measurement=measurement, order_direction=order_direction, timeframe=timeframe, filters=filters, metric_filters=metric_filters)

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
    api_instance = mux_python.MetricsApi(api_client)
    metric_id = 'video_startup_time' # str | ID of the Metric
measurement = 'measurement_example' # str | Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \"sum\" : `ad_attempt_count`, `ad_break_count`, `ad_break_error_count`, `ad_error_count`, `ad_impression_count`, `playing_time` \"median\" : `ad_preroll_startup_time`, `aggregate_startup_time`, `content_startup_time`, `max_downscale_percentage`, `max_upscale_percentage`, `page_load_time`, `player_average_live_latency`, `player_startup_time`, `rebuffer_count`, `rebuffer_duration`, `requests_for_first_preroll`, `video_startup_preroll_load_time`, `video_startup_preroll_request_time`, `video_startup_time`, `view_average_request_latency`, `view_average_request_throughput`, `view_max_request_latency`, `weighted_average_bitrate` \"avg\" : `ad_break_error_percentage`, `ad_error_percentage`, `ad_exit_before_start_count`, `ad_exit_before_start_percentage`, `ad_playback_failure_percentage`, `ad_startup_error_count`, `ad_startup_error_percentage`, `content_playback_failure_percentage`, `downscale_percentage`, `exits_before_video_start`, `playback_business_exception_percentage`, `playback_failure_percentage`, `playback_success_score`, `rebuffer_frequency`, `rebuffer_percentage`, `seek_latency`, `smoothness_score`, `startup_time_score`, `upscale_percentage`, `video_quality_score`, `video_startup_business_exception_percentage`, `video_startup_failure_percentage`, `view_dropped_percentage`, `viewer_experience_score` \"count\" : `started_views`, `unique_viewers`  (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)
filters = ['filters_example'] # list[str] | Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * `filters[]=dimension:value` - Include rows where dimension equals value * `filters[]=!dimension:value` - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * `filters[]=+dimension:value` - Include rows where trace contains value * `filters[]=-dimension:value` - Exclude rows where trace contains value * `filters[]=dimension:[value1,value2]` - Exact trace match  **Examples:** * `filters[]=country:US` - US views only * `filters[]=+video_cdn_trace:fastly` - Views using Fastly CDN  (optional)
metric_filters = ['metric_filters_example'] # list[str] | Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of `exits_before_video_start`, `unique_viewers`, `video_startup_failure_percentage`, `view_dropped_percentage`, and `views`.  Example:    * `metric_filters[]=aggregate_startup_time>=1000`  (optional)

    try:
        # List Insights
        api_response = api_instance.list_insights(metric_id, measurement=measurement, order_direction=order_direction, timeframe=timeframe, filters=filters, metric_filters=metric_filters)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetricsApi->list_insights: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric_id** | **str**| ID of the Metric | 
 **measurement** | **str**| Measurement for the provided metric. If omitted, the default for the metric will be used. The default measurement for each metric is: \&quot;sum\&quot; : &#x60;ad_attempt_count&#x60;, &#x60;ad_break_count&#x60;, &#x60;ad_break_error_count&#x60;, &#x60;ad_error_count&#x60;, &#x60;ad_impression_count&#x60;, &#x60;playing_time&#x60; \&quot;median\&quot; : &#x60;ad_preroll_startup_time&#x60;, &#x60;aggregate_startup_time&#x60;, &#x60;content_startup_time&#x60;, &#x60;max_downscale_percentage&#x60;, &#x60;max_upscale_percentage&#x60;, &#x60;page_load_time&#x60;, &#x60;player_average_live_latency&#x60;, &#x60;player_startup_time&#x60;, &#x60;rebuffer_count&#x60;, &#x60;rebuffer_duration&#x60;, &#x60;requests_for_first_preroll&#x60;, &#x60;video_startup_preroll_load_time&#x60;, &#x60;video_startup_preroll_request_time&#x60;, &#x60;video_startup_time&#x60;, &#x60;view_average_request_latency&#x60;, &#x60;view_average_request_throughput&#x60;, &#x60;view_max_request_latency&#x60;, &#x60;weighted_average_bitrate&#x60; \&quot;avg\&quot; : &#x60;ad_break_error_percentage&#x60;, &#x60;ad_error_percentage&#x60;, &#x60;ad_exit_before_start_count&#x60;, &#x60;ad_exit_before_start_percentage&#x60;, &#x60;ad_playback_failure_percentage&#x60;, &#x60;ad_startup_error_count&#x60;, &#x60;ad_startup_error_percentage&#x60;, &#x60;content_playback_failure_percentage&#x60;, &#x60;downscale_percentage&#x60;, &#x60;exits_before_video_start&#x60;, &#x60;playback_business_exception_percentage&#x60;, &#x60;playback_failure_percentage&#x60;, &#x60;playback_success_score&#x60;, &#x60;rebuffer_frequency&#x60;, &#x60;rebuffer_percentage&#x60;, &#x60;seek_latency&#x60;, &#x60;smoothness_score&#x60;, &#x60;startup_time_score&#x60;, &#x60;upscale_percentage&#x60;, &#x60;video_quality_score&#x60;, &#x60;video_startup_business_exception_percentage&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, &#x60;viewer_experience_score&#x60; \&quot;count\&quot; : &#x60;started_views&#x60;, &#x60;unique_viewers&#x60;  | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 
 **filters** | [**list[str]**](str.md)| Filter results using key:value pairs. Must be provided as an array query string parameter.  **Basic filtering:** * &#x60;filters[]&#x3D;dimension:value&#x60; - Include rows where dimension equals value * &#x60;filters[]&#x3D;!dimension:value&#x60; - Exclude rows where dimension equals value  **For trace dimensions (like video_cdn_trace):** * &#x60;filters[]&#x3D;+dimension:value&#x60; - Include rows where trace contains value * &#x60;filters[]&#x3D;-dimension:value&#x60; - Exclude rows where trace contains value * &#x60;filters[]&#x3D;dimension:[value1,value2]&#x60; - Exact trace match  **Examples:** * &#x60;filters[]&#x3D;country:US&#x60; - US views only * &#x60;filters[]&#x3D;+video_cdn_trace:fastly&#x60; - Views using Fastly CDN  | [optional] 
 **metric_filters** | [**list[str]**](str.md)| Limit the results to rows that match inequality conditions from provided metric comparison clauses. Must be provided as an array query string parameter.  Possible filterable metrics are the same as the set of metric ids, with the exceptions of &#x60;exits_before_video_start&#x60;, &#x60;unique_viewers&#x60;, &#x60;video_startup_failure_percentage&#x60;, &#x60;view_dropped_percentage&#x60;, and &#x60;views&#x60;.  Example:    * &#x60;metric_filters[]&#x3D;aggregate_startup_time&gt;&#x3D;1000&#x60;  | [optional] 

### Return type

[**ListInsightsResponse**](ListInsightsResponse.md)

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

