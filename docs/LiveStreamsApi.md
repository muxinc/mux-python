# mux_python.LiveStreamsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_live_stream**](LiveStreamsApi.md#create_live_stream) | **POST** /video/v1/live-streams | Create a live stream
[**create_live_stream_playback_id**](LiveStreamsApi.md#create_live_stream_playback_id) | **POST** /video/v1/live-streams/{LIVE_KEY_ID}/playback-ids | Create a live stream playback ID
[**delete_live_stream**](LiveStreamsApi.md#delete_live_stream) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID} | Delete a live stream
[**delete_live_stream_playback_id**](LiveStreamsApi.md#delete_live_stream_playback_id) | **DELETE** /video/v1/live-streams/{LIVE_KEY_ID}/playback-ids/{PLAYBACK_ID} | Delete a live stream playback ID
[**get_live_stream**](LiveStreamsApi.md#get_live_stream) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID} | Retrieve a live stream
[**list_live_streams**](LiveStreamsApi.md#list_live_streams) | **GET** /video/v1/live-streams | List live streams
[**reset_stream_key**](LiveStreamsApi.md#reset_stream_key) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/reset-stream-key | Reset a live stream’s stream key
[**signal_live_stream_complete**](LiveStreamsApi.md#signal_live_stream_complete) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/complete | Signal a live stream is finished


# **create_live_stream**
> LiveStreamResponse create_live_stream(create_live_stream_request=create_live_stream_request)

Create a live stream

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
create_live_stream_request = mux_python.CreateLiveStreamRequest() # CreateLiveStreamRequest |  (optional)

try:
    # Create a live stream
    api_response = api_instance.create_live_stream(create_live_stream_request=create_live_stream_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->create_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_live_stream_request** | [**CreateLiveStreamRequest**](CreateLiveStreamRequest.md)|  | [optional] 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_live_stream_playback_id**
> CreatePlaybackIDResponse create_live_stream_playback_id(live_stream_id, create_playback_id_request=create_playback_id_request)

Create a live stream playback ID

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | The live stream ID
create_playback_id_request = mux_python.CreatePlaybackIDRequest() # CreatePlaybackIDRequest |  (optional)

try:
    # Create a live stream playback ID
    api_response = api_instance.create_live_stream_playback_id(live_stream_id, create_playback_id_request=create_playback_id_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->create_live_stream_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **create_playback_id_request** | [**CreatePlaybackIDRequest**](CreatePlaybackIDRequest.md)|  | [optional] 

### Return type

[**CreatePlaybackIDResponse**](CreatePlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream**
> delete_live_stream(live_stream_id)

Delete a live stream

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | The live stream ID

try:
    # Delete a live stream
    api_instance.delete_live_stream(live_stream_id)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->delete_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream_playback_id**
> delete_live_stream_playback_id(live_stream_id, playback_id)

Delete a live stream playback ID

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | The live stream ID
playback_id = 'playback_id_example' # str | The live stream's playback ID.

try:
    # Delete a live stream playback ID
    api_instance.delete_live_stream_playback_id(live_stream_id, playback_id)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->delete_live_stream_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_stream**
> LiveStreamResponse get_live_stream(live_stream_id)

Retrieve a live stream

Retrieves the details of a live stream that has previously been created. Supply the unique live stream ID that was returned from your previous request, and Mux will return the corresponding live stream information. The same information is returned when creating a live stream.

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | The live stream ID

try:
    # Retrieve a live stream
    api_response = api_instance.get_live_stream(live_stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->get_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_live_streams**
> ListLiveStreamsResponse list_live_streams(limit=limit, page=page)

List live streams

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

try:
    # List live streams
    api_response = api_instance.list_live_streams(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->list_live_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListLiveStreamsResponse**](ListLiveStreamsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_stream_key**
> LiveStreamResponse reset_stream_key(live_stream_id)

Reset a live stream’s stream key

Reset a live stream key if you want to immediately stop the current stream key from working and create a new stream key that can be used for future broadcasts.

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | The live stream ID

try:
    # Reset a live stream’s stream key
    api_response = api_instance.reset_stream_key(live_stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->reset_stream_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_live_stream_complete**
> SignalLiveStreamCompleteResponse signal_live_stream_complete(live_stream_id)

Signal a live stream is finished

(Optional) Make the recorded asset available immediately instead of waiting for the reconnect_window.

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
api_instance = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
live_stream_id = 'live_stream_id_example' # str | The live stream ID

try:
    # Signal a live stream is finished
    api_response = api_instance.signal_live_stream_complete(live_stream_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LiveStreamsApi->signal_live_stream_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**SignalLiveStreamCompleteResponse**](SignalLiveStreamCompleteResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

