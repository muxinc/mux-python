# mux_python.PlaybackIDApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_or_livestream_id**](PlaybackIDApi.md#get_asset_or_livestream_id) | **GET** /video/v1/playback-ids/{PLAYBACK_ID} | Retrieve an Asset or Live Stream ID


# **get_asset_or_livestream_id**
> GetAssetOrLiveStreamIdResponse get_asset_or_livestream_id(playback_id)

Retrieve an Asset or Live Stream ID

Retrieves the Identifier of the Asset or Live Stream associated with the Playback ID. 

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
api_instance = mux_python.PlaybackIDApi(mux_python.ApiClient(configuration))
playback_id = 'playback_id_example' # str | The live stream's playback ID.

try:
    # Retrieve an Asset or Live Stream ID
    api_response = api_instance.get_asset_or_livestream_id(playback_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlaybackIDApi->get_asset_or_livestream_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_id** | **str**| The live stream&#39;s playback ID. | 

### Return type

[**GetAssetOrLiveStreamIdResponse**](GetAssetOrLiveStreamIdResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

