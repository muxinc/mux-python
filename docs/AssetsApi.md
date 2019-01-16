# mux_python.AssetsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](AssetsApi.md#create_asset) | **POST** /video/v1/assets | Create an asset
[**create_asset_playback_id**](AssetsApi.md#create_asset_playback_id) | **POST** /video/v1/assets/{ASSET_ID}/playback-ids | Create a playback ID
[**delete_asset**](AssetsApi.md#delete_asset) | **DELETE** /video/v1/assets/{ASSET_ID} | Delete an asset
[**delete_asset_playback_id**](AssetsApi.md#delete_asset_playback_id) | **DELETE** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Delete a playback ID
[**get_asset**](AssetsApi.md#get_asset) | **GET** /video/v1/assets/{ASSET_ID} | Retrieve an asset
[**get_asset_input_info**](AssetsApi.md#get_asset_input_info) | **GET** /video/v1/assets/{ASSET_ID}/input-info | Retrieve asset input info
[**get_asset_playback_id**](AssetsApi.md#get_asset_playback_id) | **GET** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Retrieve a playback ID
[**list_asset_playback_ids**](AssetsApi.md#list_asset_playback_ids) | **GET** /video/v1/assets/{ASSET_ID}/playback-ids | List an asset&#39;s playback IDs
[**list_assets**](AssetsApi.md#list_assets) | **GET** /video/v1/assets | List assets
[**update_asset_mp4_support**](AssetsApi.md#update_asset_mp4_support) | **PUT** /video/v1/assets/{ASSET_ID}/mp4-support | Update MP4 support


# **create_asset**
> AssetResponse create_asset(create_asset_request=create_asset_request)

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
configuration = mux_python.Configuration()
# Configure HTTP basic authorization: accessToken
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
create_asset_request = mux_python.CreateAssetRequest() # CreateAssetRequest |  (optional)

try:
    # Create an asset
    api_response = api_instance.create_asset(create_asset_request=create_asset_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->create_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_asset_request** | [**CreateAssetRequest**](CreateAssetRequest.md)|  | [optional] 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_playback_id**
> CreatePlaybackIDResponse create_asset_playback_id(asset_id, create_playback_id_request=create_playback_id_request)

Create a playback ID

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
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
asset_id = 'asset_id_example' # str | The asset ID.
create_playback_id_request = mux_python.CreatePlaybackIDRequest() # CreatePlaybackIDRequest |  (optional)

try:
    # Create a playback ID
    api_response = api_instance.create_asset_playback_id(asset_id, create_playback_id_request=create_playback_id_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->create_asset_playback_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 
 **create_playback_id_request** | [**CreatePlaybackIDRequest**](CreatePlaybackIDRequest.md)|  | [optional] 

### Return type

[**CreatePlaybackIDResponse**](CreatePlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> delete_asset(asset_id)

Delete an asset

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
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset_playback_id**
> delete_asset_playback_id(asset_id, playback_id)

Delete a playback ID

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
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
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
configuration = mux_python.Configuration()
# Configure HTTP basic authorization: accessToken
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
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
configuration = mux_python.Configuration()
# Configure HTTP basic authorization: accessToken
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_playback_id**
> GetAssetPlaybackIDResponse get_asset_playback_id(asset_id, playback_id)

Retrieve a playback ID

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
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_asset_playback_ids**
> ListAssetPlaybackIDsResponse list_asset_playback_ids(asset_id)

List an asset's playback IDs

Gets the Playback IDs associated with the asset 

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
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
asset_id = 'asset_id_example' # str | The asset ID.

try:
    # List an asset's playback IDs
    api_response = api_instance.list_asset_playback_ids(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->list_asset_playback_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| The asset ID. | 

### Return type

[**ListAssetPlaybackIDsResponse**](ListAssetPlaybackIDsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> ListAssetsResponse list_assets(limit=limit, page=page)

List assets

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
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

try:
    # List assets
    api_response = api_instance.list_assets(limit=limit, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->list_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_mp4_support**
> AssetResponse update_asset_mp4_support(asset_id, update_asset_mp4_support_request)

Update MP4 support

Allows you add or remove mp4 support for assets that were created without it. Currently there are two values supported in this request, `standard` and `none`. `none` means that an asset *does not* have mp4 support, so submitting a request with `mp4_support` set to `none` will delete the mp4 assets from the asset in question.

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
api_instance = mux_python.AssetsApi(mux_python.ApiClient(configuration))
asset_id = 'asset_id_example' # str | The asset ID.
update_asset_mp4_support_request = mux_python.UpdateAssetMP4SupportRequest() # UpdateAssetMP4SupportRequest | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

