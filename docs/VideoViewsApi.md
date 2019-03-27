# mux_python.VideoViewsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_view**](VideoViewsApi.md#get_video_view) | **GET** /data/v1/video-views/{VIDEO_VIEW_ID} | Get a Video View
[**list_video_views**](VideoViewsApi.md#list_video_views) | **GET** /data/v1/video-views | List Video Views


# **get_video_view**
> VideoViewResponse get_video_view(video_view_id)

Get a Video View

Returns the details of a video view 

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
api_instance = mux_python.VideoViewsApi(mux_python.ApiClient(configuration))
video_view_id = abcd1234 # str | ID of the Video View

try:
    # Get a Video View
    api_response = api_instance.get_video_view(video_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoViewsApi->get_video_view: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_view_id** | **str**| ID of the Video View | 

### Return type

[**VideoViewResponse**](VideoViewResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_video_views**
> ListVideoViewsResponse list_video_views(limit=limit, page=page, viewer_id=viewer_id, error_id=error_id, order_direction=order_direction, filters=filters, timeframe=timeframe)

List Video Views

Returns a list of video views 

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
api_instance = mux_python.VideoViewsApi(mux_python.ApiClient(configuration))
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
viewer_id = 'viewer_id_example' # str | Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux. (optional)
error_id = 56 # int | Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error. (optional)
order_direction = 'order_direction_example' # str | Sort order. (optional)
filters = ['filters_example'] # list[str] | Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US).  Possible filter names are the same as returned by the List Filters endpoint.  (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600    * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days.  (optional)

try:
    # List Video Views
    api_response = api_instance.list_video_views(limit=limit, page=page, viewer_id=viewer_id, error_id=error_id, order_direction=order_direction, filters=filters, timeframe=timeframe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideoViewsApi->list_video_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **viewer_id** | **str**| Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux. | [optional] 
 **error_id** | **int**| Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error. | [optional] 
 **order_direction** | **str**| Sort order. | [optional] 
 **filters** | [**list[str]**](str.md)| Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;country:US).  Possible filter names are the same as returned by the List Filters endpoint.  | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600    * duration string e.g. timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days.  | [optional] 

### Return type

[**ListVideoViewsResponse**](ListVideoViewsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

