# mux_python.LiveStreamsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_live_stream**](LiveStreamsApi.md#create_live_stream) | **POST** /video/v1/live-streams | Create a live stream
[**create_live_stream_playback_id**](LiveStreamsApi.md#create_live_stream_playback_id) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids | Create a live stream playback ID
[**create_live_stream_simulcast_target**](LiveStreamsApi.md#create_live_stream_simulcast_target) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets | Create a live stream simulcast target
[**delete_live_stream**](LiveStreamsApi.md#delete_live_stream) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID} | Delete a live stream
[**delete_live_stream_new_asset_settings_static_renditions**](LiveStreamsApi.md#delete_live_stream_new_asset_settings_static_renditions) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/new-asset-settings/static-renditions | Delete a live stream&#39;s static renditions setting for new assets
[**delete_live_stream_playback_id**](LiveStreamsApi.md#delete_live_stream_playback_id) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids/{PLAYBACK_ID} | Delete a live stream playback ID
[**delete_live_stream_simulcast_target**](LiveStreamsApi.md#delete_live_stream_simulcast_target) | **DELETE** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID} | Delete a live stream simulcast target
[**disable_live_stream**](LiveStreamsApi.md#disable_live_stream) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/disable | Disable a live stream
[**enable_live_stream**](LiveStreamsApi.md#enable_live_stream) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/enable | Enable a live stream
[**get_live_stream**](LiveStreamsApi.md#get_live_stream) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID} | Retrieve a live stream
[**get_live_stream_playback_id**](LiveStreamsApi.md#get_live_stream_playback_id) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID}/playback-ids/{PLAYBACK_ID} | Retrieve a live stream playback ID
[**get_live_stream_simulcast_target**](LiveStreamsApi.md#get_live_stream_simulcast_target) | **GET** /video/v1/live-streams/{LIVE_STREAM_ID}/simulcast-targets/{SIMULCAST_TARGET_ID} | Retrieve a live stream simulcast target
[**list_live_streams**](LiveStreamsApi.md#list_live_streams) | **GET** /video/v1/live-streams | List live streams
[**reset_stream_key**](LiveStreamsApi.md#reset_stream_key) | **POST** /video/v1/live-streams/{LIVE_STREAM_ID}/reset-stream-key | Reset a live stream&#39;s stream key
[**signal_live_stream_complete**](LiveStreamsApi.md#signal_live_stream_complete) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/complete | Signal a live stream is finished
[**update_live_stream**](LiveStreamsApi.md#update_live_stream) | **PATCH** /video/v1/live-streams/{LIVE_STREAM_ID} | Update a live stream
[**update_live_stream_embedded_subtitles**](LiveStreamsApi.md#update_live_stream_embedded_subtitles) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/embedded-subtitles | Update a live stream&#39;s embedded subtitles
[**update_live_stream_generated_subtitles**](LiveStreamsApi.md#update_live_stream_generated_subtitles) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/generated-subtitles | Update a live stream&#39;s generated subtitles
[**update_live_stream_new_asset_settings_static_renditions**](LiveStreamsApi.md#update_live_stream_new_asset_settings_static_renditions) | **PUT** /video/v1/live-streams/{LIVE_STREAM_ID}/new-asset-settings/static-renditions | Update live stream static renditions for new assets


# **create_live_stream**
> LiveStreamResponse create_live_stream(create_live_stream_request)

Create a live stream

Creates a new live stream. Once created, an encoder can connect to Mux via the specified stream key and begin streaming to an audience.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    create_live_stream_request = {"playback_policies":["public"],"new_asset_settings":{"playback_policies":["public"]}} # CreateLiveStreamRequest | 

    try:
        # Create a live stream
        api_response = api_instance.create_live_stream(create_live_stream_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->create_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_live_stream_request** | [**CreateLiveStreamRequest**](CreateLiveStreamRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_live_stream_playback_id**
> CreatePlaybackIDResponse create_live_stream_playback_id(live_stream_id, create_playback_id_request)

Create a live stream playback ID

Create a new playback ID for this live stream, through which a viewer can watch the streamed content of the live stream.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
create_playback_id_request = {"policy":"signed"} # CreatePlaybackIDRequest | 

    try:
        # Create a live stream playback ID
        api_response = api_instance.create_live_stream_playback_id(live_stream_id, create_playback_id_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->create_live_stream_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **create_playback_id_request** | [**CreatePlaybackIDRequest**](CreatePlaybackIDRequest.md)|  | 

### Return type

[**CreatePlaybackIDResponse**](CreatePlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_live_stream_simulcast_target**
> SimulcastTargetResponse create_live_stream_simulcast_target(live_stream_id, create_simulcast_target_request)

Create a live stream simulcast target

Create a simulcast target for the parent live stream. Simulcast target can only be created when the parent live stream is in idle state. Only one simulcast target can be created at a time with this API.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
create_simulcast_target_request = {"url":"rtmp://live.example.com/app","stream_key":"abcdefgh","passthrough":"Example"} # CreateSimulcastTargetRequest | 

    try:
        # Create a live stream simulcast target
        api_response = api_instance.create_live_stream_simulcast_target(live_stream_id, create_simulcast_target_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->create_live_stream_simulcast_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **create_simulcast_target_request** | [**CreateSimulcastTargetRequest**](CreateSimulcastTargetRequest.md)|  | 

### Return type

[**SimulcastTargetResponse**](SimulcastTargetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream**
> delete_live_stream(live_stream_id)

Delete a live stream

Deletes a live stream from the current environment. If the live stream is currently active and being streamed to, ingest will be terminated and the encoder will be disconnected.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream_new_asset_settings_static_renditions**
> delete_live_stream_new_asset_settings_static_renditions(live_stream_id)

Delete a live stream's static renditions setting for new assets

Deletes a live stream's static renditions settings for new assets. Further assets made via this live stream will not create static renditions unless re-added.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Delete a live stream's static renditions setting for new assets
        api_instance.delete_live_stream_new_asset_settings_static_renditions(live_stream_id)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->delete_live_stream_new_asset_settings_static_renditions: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream_playback_id**
> delete_live_stream_playback_id(live_stream_id, playback_id)

Delete a live stream playback ID

Deletes the playback ID for the live stream. This will not disable ingest (as the live stream still exists). New attempts to play back the live stream will fail immediately. However, current viewers will be able to continue watching the stream for some period of time.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_live_stream_simulcast_target**
> delete_live_stream_simulcast_target(live_stream_id, simulcast_target_id)

Delete a live stream simulcast target

Delete the simulcast target using the simulcast target ID returned when creating the simulcast target. Simulcast Target can only be deleted when the parent live stream is in idle state.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
simulcast_target_id = 'simulcast_target_id_example' # str | The ID of the simulcast target.

    try:
        # Delete a live stream simulcast target
        api_instance.delete_live_stream_simulcast_target(live_stream_id, simulcast_target_id)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->delete_live_stream_simulcast_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **simulcast_target_id** | **str**| The ID of the simulcast target. | 

### Return type

void (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_live_stream**
> DisableLiveStreamResponse disable_live_stream(live_stream_id)

Disable a live stream

Disables a live stream, making it reject incoming RTMP streams until re-enabled. The API also ends the live stream recording immediately when active. Ending the live stream recording adds the `EXT-X-ENDLIST` tag to the HLS manifest which notifies the player that this live stream is over.  Mux also closes the encoder connection immediately. Any attempt from the encoder to re-establish connection will fail till the live stream is re-enabled. 

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Disable a live stream
        api_response = api_instance.disable_live_stream(live_stream_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->disable_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**DisableLiveStreamResponse**](DisableLiveStreamResponse.md)

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

# **enable_live_stream**
> EnableLiveStreamResponse enable_live_stream(live_stream_id)

Enable a live stream

Enables a live stream, allowing it to accept an incoming RTMP stream.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Enable a live stream
        api_response = api_instance.enable_live_stream(live_stream_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->enable_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 

### Return type

[**EnableLiveStreamResponse**](EnableLiveStreamResponse.md)

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
    api_instance = mux_python.LiveStreamsApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_live_stream_playback_id**
> GetLiveStreamPlaybackIDResponse get_live_stream_playback_id(live_stream_id, playback_id)

Retrieve a live stream playback ID

Fetches information about a live stream's playback ID, through which a viewer can watch the streamed content from this live stream.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Retrieve a live stream playback ID
        api_response = api_instance.get_live_stream_playback_id(live_stream_id, playback_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->get_live_stream_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

[**GetLiveStreamPlaybackIDResponse**](GetLiveStreamPlaybackIDResponse.md)

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

# **get_live_stream_simulcast_target**
> SimulcastTargetResponse get_live_stream_simulcast_target(live_stream_id, simulcast_target_id)

Retrieve a live stream simulcast target

Retrieves the details of the simulcast target created for the parent live stream. Supply the unique live stream ID and simulcast target ID that was returned in the response of create simulcast target request, and Mux will return the corresponding information.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
simulcast_target_id = 'simulcast_target_id_example' # str | The ID of the simulcast target.

    try:
        # Retrieve a live stream simulcast target
        api_response = api_instance.get_live_stream_simulcast_target(live_stream_id, simulcast_target_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->get_live_stream_simulcast_target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **simulcast_target_id** | **str**| The ID of the simulcast target. | 

### Return type

[**SimulcastTargetResponse**](SimulcastTargetResponse.md)

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

# **list_live_streams**
> ListLiveStreamsResponse list_live_streams(limit=limit, page=page, stream_key=stream_key, status=status)

List live streams

Lists the live streams that currently exist in the current environment.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
stream_key = 'stream_key_example' # str | Filter response to return live stream for this stream key only (optional)
status = mux_python.LiveStreamStatus() # LiveStreamStatus | Filter response to return live streams with the specified status only (optional)

    try:
        # List live streams
        api_response = api_instance.list_live_streams(limit=limit, page=page, stream_key=stream_key, status=status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->list_live_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **stream_key** | **str**| Filter response to return live stream for this stream key only | [optional] 
 **status** | [**LiveStreamStatus**](.md)| Filter response to return live streams with the specified status only | [optional] 

### Return type

[**ListLiveStreamsResponse**](ListLiveStreamsResponse.md)

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

# **reset_stream_key**
> LiveStreamResponse reset_stream_key(live_stream_id)

Reset a live stream's stream key

Reset a live stream key if you want to immediately stop the current stream key from working and create a new stream key that can be used for future broadcasts.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID

    try:
        # Reset a live stream's stream key
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_live_stream_complete**
> SignalLiveStreamCompleteResponse signal_live_stream_complete(live_stream_id)

Signal a live stream is finished

(Optional) End the live stream recording immediately instead of waiting for the reconnect_window. `EXT-X-ENDLIST` tag is added to the HLS manifest which notifies the player that this live stream is over.  Mux does not close the encoder connection immediately. Encoders are often configured to re-establish connections immediately which would result in a new recorded asset. For this reason, Mux waits for 60s before closing the connection with the encoder. This 60s timeframe is meant to give encoder operators a chance to disconnect from their end. 

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
    api_instance = mux_python.LiveStreamsApi(api_client)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream**
> LiveStreamResponse update_live_stream(live_stream_id, update_live_stream_request)

Update a live stream

Updates the parameters of a previously-created live stream. This currently supports a subset of variables. Supply the live stream ID and the updated parameters and Mux will return the corresponding live stream information. The information returned will be the same after update as for subsequent get live stream requests.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_request = {"latency_mode":"standard","reconnect_window":30,"max_continuous_duration":1200} # UpdateLiveStreamRequest | 

    try:
        # Update a live stream
        api_response = api_instance.update_live_stream(live_stream_id, update_live_stream_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_request** | [**UpdateLiveStreamRequest**](UpdateLiveStreamRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream_embedded_subtitles**
> LiveStreamResponse update_live_stream_embedded_subtitles(live_stream_id, update_live_stream_embedded_subtitles_request)

Update a live stream's embedded subtitles

Configures a live stream to receive embedded closed captions. The resulting Asset's subtitle text track will have `closed_captions: true` set. 

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_embedded_subtitles_request = {"embedded_subtitles":[{"passthrough":"Example"}]} # UpdateLiveStreamEmbeddedSubtitlesRequest | 

    try:
        # Update a live stream's embedded subtitles
        api_response = api_instance.update_live_stream_embedded_subtitles(live_stream_id, update_live_stream_embedded_subtitles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream_embedded_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_embedded_subtitles_request** | [**UpdateLiveStreamEmbeddedSubtitlesRequest**](UpdateLiveStreamEmbeddedSubtitlesRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream_generated_subtitles**
> LiveStreamResponse update_live_stream_generated_subtitles(live_stream_id, update_live_stream_generated_subtitles_request)

Update a live stream's generated subtitles

Updates a live stream's automatic-speech-recognition-generated subtitle configuration. Automatic speech recognition subtitles can be removed by sending an empty array in the request payload. 

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_generated_subtitles_request = {"generated_subtitles":[{"name":"English CC (ASR)","language_code":"en","passthrough":"Example"}]} # UpdateLiveStreamGeneratedSubtitlesRequest | 

    try:
        # Update a live stream's generated subtitles
        api_response = api_instance.update_live_stream_generated_subtitles(live_stream_id, update_live_stream_generated_subtitles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream_generated_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_generated_subtitles_request** | [**UpdateLiveStreamGeneratedSubtitlesRequest**](UpdateLiveStreamGeneratedSubtitlesRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_live_stream_new_asset_settings_static_renditions**
> LiveStreamResponse update_live_stream_new_asset_settings_static_renditions(live_stream_id, update_live_stream_new_asset_settings_static_renditions_request)

Update live stream static renditions for new assets

Updates a live stream's static renditions settings for new assets. Further assets made via this live stream will create static renditions per the settings provided. You must provide all static renditions desired.

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
    api_instance = mux_python.LiveStreamsApi(api_client)
    live_stream_id = 'live_stream_id_example' # str | The live stream ID
update_live_stream_new_asset_settings_static_renditions_request = {"static_renditions":[{"resolution":"audio-only"},{"resolution":"highest"}]} # UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest | 

    try:
        # Update live stream static renditions for new assets
        api_response = api_instance.update_live_stream_new_asset_settings_static_renditions(live_stream_id, update_live_stream_new_asset_settings_static_renditions_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LiveStreamsApi->update_live_stream_new_asset_settings_static_renditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **live_stream_id** | **str**| The live stream ID | 
 **update_live_stream_new_asset_settings_static_renditions_request** | [**UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest**](UpdateLiveStreamNewAssetSettingsStaticRenditionsRequest.md)|  | 

### Return type

[**LiveStreamResponse**](LiveStreamResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

