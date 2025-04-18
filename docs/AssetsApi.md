# mux_python.AssetsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetsApi.md#create_asset) | **POST** /video/v1/assets | Create an asset
[**create_asset_playback_id**](AssetsApi.md#create_asset_playback_id) | **POST** /video/v1/assets/{ASSET_ID}/playback-ids | Create a playback ID
[**create_asset_static_rendition**](AssetsApi.md#create_asset_static_rendition) | **POST** /video/v1/assets/{ASSET_ID}/static-renditions | Create a static rendition for an asset
[**create_asset_track**](AssetsApi.md#create_asset_track) | **POST** /video/v1/assets/{ASSET_ID}/tracks | Create an asset track
[**delete_asset**](AssetsApi.md#delete_asset) | **DELETE** /video/v1/assets/{ASSET_ID} | Delete an asset
[**delete_asset_playback_id**](AssetsApi.md#delete_asset_playback_id) | **DELETE** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Delete a playback ID
[**delete_asset_static_rendition**](AssetsApi.md#delete_asset_static_rendition) | **DELETE** /video/v1/assets/{ASSET_ID}/static-renditions/{STATIC_RENDITION_ID} | Delete a single static rendition for an asset
[**delete_asset_track**](AssetsApi.md#delete_asset_track) | **DELETE** /video/v1/assets/{ASSET_ID}/tracks/{TRACK_ID} | Delete an asset track
[**generate_asset_track_subtitles**](AssetsApi.md#generate_asset_track_subtitles) | **POST** /video/v1/assets/{ASSET_ID}/tracks/{TRACK_ID}/generate-subtitles | Generate track subtitles
[**get_asset**](AssetsApi.md#get_asset) | **GET** /video/v1/assets/{ASSET_ID} | Retrieve an asset
[**get_asset_input_info**](AssetsApi.md#get_asset_input_info) | **GET** /video/v1/assets/{ASSET_ID}/input-info | Retrieve asset input info
[**get_asset_playback_id**](AssetsApi.md#get_asset_playback_id) | **GET** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Retrieve a playback ID
[**list_assets**](AssetsApi.md#list_assets) | **GET** /video/v1/assets | List assets
[**update_asset**](AssetsApi.md#update_asset) | **PATCH** /video/v1/assets/{ASSET_ID} | Update an asset
[**update_asset_master_access**](AssetsApi.md#update_asset_master_access) | **PUT** /video/v1/assets/{ASSET_ID}/master-access | Update master access
[**update_asset_mp4_support**](AssetsApi.md#update_asset_mp4_support) | **PUT** /video/v1/assets/{ASSET_ID}/mp4-support | Update MP4 support


# **create_asset**
> AssetResponse create_asset(create_asset_request)

Create an asset

Create a new Mux Video asset.

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
    api_instance = mux_python.AssetsApi(api_client)
    create_asset_request = {"inputs":[{"url":"https://muxed.s3.amazonaws.com/leds.mp4"}],"playback_policies":["public"],"video_quality":"basic"} # CreateAssetRequest | 

    try:
        # Create an asset
        api_response = api_instance.create_asset(create_asset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_asset_request** | [**CreateAssetRequest**](CreateAssetRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_playback_id**
> CreatePlaybackIDResponse create_asset_playback_id(asset_id, create_playback_id_request)

Create a playback ID

Creates a playback ID that can be used to stream the asset to a viewer.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
create_playback_id_request = {"policy":"public"} # CreatePlaybackIDRequest | 

    try:
        # Create a playback ID
        api_response = api_instance.create_asset_playback_id(asset_id, create_playback_id_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
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

# **create_asset_static_rendition**
> CreateStaticRenditionResponse create_asset_static_rendition(asset_id, create_static_rendition_request)

Create a static rendition for an asset

Creates a static rendition (i.e. MP4) for an asset

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
create_static_rendition_request = {"resolution":"highest"} # CreateStaticRenditionRequest | 

    try:
        # Create a static rendition for an asset
        api_response = api_instance.create_asset_static_rendition(asset_id, create_static_rendition_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset_static_rendition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **create_static_rendition_request** | [**CreateStaticRenditionRequest**](CreateStaticRenditionRequest.md)|  | 

### Return type

[**CreateStaticRenditionResponse**](CreateStaticRenditionResponse.md)

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

# **create_asset_track**
> CreateTrackResponse create_asset_track(asset_id, create_track_request)

Create an asset track

Adds an asset track (for example, subtitles, or an alternate audio track) to an asset. Assets must be in the `ready` state before tracks can be added.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
create_track_request = {"url":"https://example.com/myVideo_en.srt","type":"text","text_type":"subtitles","language_code":"en-US","name":"English","closed_captions":true,"passthrough":"English"} # CreateTrackRequest | 

    try:
        # Create an asset track
        api_response = api_instance.create_asset_track(asset_id, create_track_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->create_asset_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **create_track_request** | [**CreateTrackRequest**](CreateTrackRequest.md)|  | 

### Return type

[**CreateTrackResponse**](CreateTrackResponse.md)

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

# **delete_asset**
> delete_asset(asset_id)

Delete an asset

Deletes a video asset and all its data.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.

    try:
        # Delete an asset
        api_instance.delete_asset(asset_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 

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

# **delete_asset_playback_id**
> delete_asset_playback_id(asset_id, playback_id)

Delete a playback ID

Deletes a playback ID, rendering it nonfunctional for viewing an asset's video content. Please note that deleting the playback ID removes access to the underlying asset; a viewer who started playback before the playback ID was deleted may be able to watch the entire video for a limited duration.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Delete a playback ID
        api_instance.delete_asset_playback_id(asset_id, playback_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
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

# **delete_asset_static_rendition**
> delete_asset_static_rendition(asset_id, static_rendition_id)

Delete a single static rendition for an asset

Deletes a single static rendition for an asset

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
static_rendition_id = 'static_rendition_id_example' # str | The static rendition ID.

    try:
        # Delete a single static rendition for an asset
        api_instance.delete_asset_static_rendition(asset_id, static_rendition_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset_static_rendition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **static_rendition_id** | **str**| The static rendition ID. | 

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

# **delete_asset_track**
> delete_asset_track(asset_id, track_id)

Delete an asset track

Removes a text track from an asset. Audio and video tracks on assets cannot be removed.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
track_id = 'track_id_example' # str | The track ID.

    try:
        # Delete an asset track
        api_instance.delete_asset_track(asset_id, track_id)
    except ApiException as e:
        print("Exception when calling AssetsApi->delete_asset_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **track_id** | **str**| The track ID. | 

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

# **generate_asset_track_subtitles**
> GenerateTrackSubtitlesResponse generate_asset_track_subtitles(asset_id, track_id, generate_track_subtitles_request)

Generate track subtitles

Generates subtitles (captions) for a given audio track. This API can be used for up to 7 days after an asset is created.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
track_id = 'track_id_example' # str | The track ID.
generate_track_subtitles_request = {"generated_subtitles":[{"language_code":"en","name":"English (generated)","passthrough":"English (generated)"}]} # GenerateTrackSubtitlesRequest | 

    try:
        # Generate track subtitles
        api_response = api_instance.generate_asset_track_subtitles(asset_id, track_id, generate_track_subtitles_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->generate_asset_track_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **track_id** | **str**| The track ID. | 
 **generate_track_subtitles_request** | [**GenerateTrackSubtitlesRequest**](GenerateTrackSubtitlesRequest.md)|  | 

### Return type

[**GenerateTrackSubtitlesResponse**](GenerateTrackSubtitlesResponse.md)

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

# **get_asset**
> AssetResponse get_asset(asset_id)

Retrieve an asset

Retrieves the details of an asset that has previously been created. Supply the unique asset ID that was returned from your previous request, and Mux will return the corresponding asset information. The same information is returned when creating an asset.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.

    try:
        # Retrieve an asset
        api_response = api_instance.get_asset(asset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 

### Return type

[**AssetResponse**](AssetResponse.md)

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

# **get_asset_input_info**
> GetAssetInputInfoResponse get_asset_input_info(asset_id)

Retrieve asset input info

Returns a list of the input objects that were used to create the asset along with any settings that were applied to each input.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.

    try:
        # Retrieve asset input info
        api_response = api_instance.get_asset_input_info(asset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_asset_input_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 

### Return type

[**GetAssetInputInfoResponse**](GetAssetInputInfoResponse.md)

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

# **get_asset_playback_id**
> GetAssetPlaybackIDResponse get_asset_playback_id(asset_id, playback_id)

Retrieve a playback ID

Retrieves information about the specified playback ID.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
playback_id = 'playback_id_example' # str | The live stream's playback ID.

    try:
        # Retrieve a playback ID
        api_response = api_instance.get_asset_playback_id(asset_id, playback_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->get_asset_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

[**GetAssetPlaybackIDResponse**](GetAssetPlaybackIDResponse.md)

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

# **list_assets**
> ListAssetsResponse list_assets(limit=limit, page=page, live_stream_id=live_stream_id, upload_id=upload_id)

List assets

List all Mux assets.

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
    api_instance = mux_python.AssetsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
live_stream_id = 'live_stream_id_example' # str | Filter response to return all the assets for this live stream only (optional)
upload_id = 'upload_id_example' # str | Filter response to return an asset created from this direct upload only (optional)

    try:
        # List assets
        api_response = api_instance.list_assets(limit=limit, page=page, live_stream_id=live_stream_id, upload_id=upload_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->list_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **live_stream_id** | **str**| Filter response to return all the assets for this live stream only | [optional] 
 **upload_id** | **str**| Filter response to return an asset created from this direct upload only | [optional] 

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

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

# **update_asset**
> AssetResponse update_asset(asset_id, update_asset_request)

Update an asset

Updates the details of an already-created Asset with the provided Asset ID. This currently supports only the `passthrough` field.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
update_asset_request = {"passthrough":"Example"} # UpdateAssetRequest | 

    try:
        # Update an asset
        api_response = api_instance.update_asset(asset_id, update_asset_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->update_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **update_asset_request** | [**UpdateAssetRequest**](UpdateAssetRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

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

# **update_asset_master_access**
> AssetResponse update_asset_master_access(asset_id, update_asset_master_access_request)

Update master access

Allows you to add temporary access to the master (highest-quality) version of the asset in MP4 format. A URL will be created that can be used to download the master version for 24 hours. After 24 hours Master Access will revert to \"none\". This master version is not optimized for web and not meant to be streamed, only downloaded for purposes like archiving or editing the video offline.

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
update_asset_master_access_request = {"master_access":"temporary"} # UpdateAssetMasterAccessRequest | 

    try:
        # Update master access
        api_response = api_instance.update_asset_master_access(asset_id, update_asset_master_access_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->update_asset_master_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **update_asset_master_access_request** | [**UpdateAssetMasterAccessRequest**](UpdateAssetMasterAccessRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

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

# **update_asset_mp4_support**
> AssetResponse update_asset_mp4_support(asset_id, update_asset_mp4_support_request)

Update MP4 support

This method has been deprecated. Please see the [Static Rendition API](https://www.mux.com/docs/guides/enable-static-mp4-renditions#after-asset-creation). Allows you to add or remove mp4 support for assets that were created without it. The values supported are `capped-1080p`, `audio-only`, `audio-only,capped-1080p`, `standard`(deprecated),  and `none`. `none` means that an asset *does not* have mp4 support, so submitting a request with `mp4_support` set to `none` will delete the mp4 assets from the asset in question. 

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
    api_instance = mux_python.AssetsApi(api_client)
    asset_id = 'asset_id_example' # str | The asset ID.
update_asset_mp4_support_request = {"mp4_support":"capped-1080p"} # UpdateAssetMP4SupportRequest | 

    try:
        # Update MP4 support
        api_response = api_instance.update_asset_mp4_support(asset_id, update_asset_mp4_support_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetsApi->update_asset_mp4_support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **update_asset_mp4_support_request** | [**UpdateAssetMP4SupportRequest**](UpdateAssetMP4SupportRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

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

