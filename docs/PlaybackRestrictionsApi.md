# mux_python.PlaybackRestrictionsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_playback_restriction**](PlaybackRestrictionsApi.md#create_playback_restriction) | **POST** /video/v1/playback-restrictions | Create a Playback Restriction
[**delete_playback_restriction**](PlaybackRestrictionsApi.md#delete_playback_restriction) | **DELETE** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID} | Delete a Playback Restriction
[**get_playback_restriction**](PlaybackRestrictionsApi.md#get_playback_restriction) | **GET** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID} | Retrieve a Playback Restriction
[**list_playback_restrictions**](PlaybackRestrictionsApi.md#list_playback_restrictions) | **GET** /video/v1/playback-restrictions | List Playback Restrictions
[**update_referrer_domain_restriction**](PlaybackRestrictionsApi.md#update_referrer_domain_restriction) | **PUT** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID}/referrer | Update the Referrer Playback Restriction
[**update_user_agent_restriction**](PlaybackRestrictionsApi.md#update_user_agent_restriction) | **PUT** /video/v1/playback-restrictions/{PLAYBACK_RESTRICTION_ID}/user_agent | Update the User Agent Restriction


# **create_playback_restriction**
> PlaybackRestrictionResponse create_playback_restriction(create_playback_restriction_request)

Create a Playback Restriction

Create a new Playback Restriction.

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
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    create_playback_restriction_request = {"referrer":{"allowed_domains":["*.example.com"],"allow_no_referrer":true},"user_agent":{"allow_no_user_agent":false,"allow_high_risk_user_agent":false}} # CreatePlaybackRestrictionRequest | 

    try:
        # Create a Playback Restriction
        api_response = api_instance.create_playback_restriction(create_playback_restriction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->create_playback_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_playback_restriction_request** | [**CreatePlaybackRestrictionRequest**](CreatePlaybackRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

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

# **delete_playback_restriction**
> delete_playback_restriction(playback_restriction_id)

Delete a Playback Restriction

Deletes a single Playback Restriction.

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
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.

    try:
        # Delete a Playback Restriction
        api_instance.delete_playback_restriction(playback_restriction_id)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->delete_playback_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 

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

# **get_playback_restriction**
> PlaybackRestrictionResponse get_playback_restriction(playback_restriction_id)

Retrieve a Playback Restriction

Retrieves a Playback Restriction associated with the unique identifier.

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
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.

    try:
        # Retrieve a Playback Restriction
        api_response = api_instance.get_playback_restriction(playback_restriction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->get_playback_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

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

# **list_playback_restrictions**
> ListPlaybackRestrictionsResponse list_playback_restrictions(page=page, limit=limit)

List Playback Restrictions

Returns a list of all Playback Restrictions.

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
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
limit = 25 # int | Number of items to include in the response (optional) (default to 25)

    try:
        # List Playback Restrictions
        api_response = api_instance.list_playback_restrictions(page=page, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->list_playback_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]

### Return type

[**ListPlaybackRestrictionsResponse**](ListPlaybackRestrictionsResponse.md)

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

# **update_referrer_domain_restriction**
> PlaybackRestrictionResponse update_referrer_domain_restriction(playback_restriction_id, update_referrer_domain_restriction_request)

Update the Referrer Playback Restriction

Allows you to modify the list of domains or change how Mux validates playback requests without the `Referer` HTTP header. The Referrer restriction fully replaces the old list with this new list of domains.

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
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.
update_referrer_domain_restriction_request = {"allowed_domains":["*.example.com"],"allow_no_referrer":true} # UpdateReferrerDomainRestrictionRequest | 

    try:
        # Update the Referrer Playback Restriction
        api_response = api_instance.update_referrer_domain_restriction(playback_restriction_id, update_referrer_domain_restriction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->update_referrer_domain_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 
 **update_referrer_domain_restriction_request** | [**UpdateReferrerDomainRestrictionRequest**](UpdateReferrerDomainRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

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

# **update_user_agent_restriction**
> PlaybackRestrictionResponse update_user_agent_restriction(playback_restriction_id, update_user_agent_restriction_request)

Update the User Agent Restriction

Allows you to modify how Mux validates playback requests with different user agents.  Please see [Using User-Agent HTTP header for validation](https://docs.mux.com/guides/secure-video-playback#using-user-agent-http-header-for-validation) for more details on this feature.

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
    api_instance = mux_python.PlaybackRestrictionsApi(api_client)
    playback_restriction_id = 'playback_restriction_id_example' # str | ID of the Playback Restriction.
update_user_agent_restriction_request = {"allow_no_user_agent":false,"allow_high_risk_user_agent":false} # UpdateUserAgentRestrictionRequest | 

    try:
        # Update the User Agent Restriction
        api_response = api_instance.update_user_agent_restriction(playback_restriction_id, update_user_agent_restriction_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlaybackRestrictionsApi->update_user_agent_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **playback_restriction_id** | **str**| ID of the Playback Restriction. | 
 **update_user_agent_restriction_request** | [**UpdateUserAgentRestrictionRequest**](UpdateUserAgentRestrictionRequest.md)|  | 

### Return type

[**PlaybackRestrictionResponse**](PlaybackRestrictionResponse.md)

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

