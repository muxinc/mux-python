# mux_python.WebInputsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_web_input**](WebInputsApi.md#create_web_input) | **POST** /video/v1/web-inputs | Create a new Web Input
[**delete_web_input**](WebInputsApi.md#delete_web_input) | **DELETE** /video/v1/web-inputs/{WEB_INPUT_ID} | Delete a Web Input
[**get_web_input**](WebInputsApi.md#get_web_input) | **GET** /video/v1/web-inputs/{WEB_INPUT_ID} | Retrieve a Web Input
[**launch_web_input**](WebInputsApi.md#launch_web_input) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/launch | Launch a Web Input
[**list_web_inputs**](WebInputsApi.md#list_web_inputs) | **GET** /video/v1/web-inputs | List Web Inputs
[**reload_web_input**](WebInputsApi.md#reload_web_input) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/reload | Reload a Web Input
[**shutdown_web_input**](WebInputsApi.md#shutdown_web_input) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/shutdown | Shut down a Web Input
[**update_web_input_url**](WebInputsApi.md#update_web_input_url) | **PUT** /video/v1/web-inputs/{WEB_INPUT_ID}/url | Update Web Input URL


# **create_web_input**
> WebInputResponse create_web_input(create_web_input_request)

Create a new Web Input

Create a new Web Input

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
    api_instance = mux_python.WebInputsApi(api_client)
    create_web_input_request = {"url":"https://example.com/hello.html","live_stream_id":"ZEBrNTpHC02iUah025KM3te6ylM7W4S4silsrFtUkn3Ag"} # CreateWebInputRequest | 

    try:
        # Create a new Web Input
        api_response = api_instance.create_web_input(create_web_input_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->create_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_web_input_request** | [**CreateWebInputRequest**](CreateWebInputRequest.md)|  | 

### Return type

[**WebInputResponse**](WebInputResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Web Input Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_input**
> delete_web_input(web_input_id)

Delete a Web Input

Deletes a Web Input and all its data

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
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Delete a Web Input
        api_instance.delete_web_input(web_input_id)
    except ApiException as e:
        print("Exception when calling WebInputsApi->delete_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

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

# **get_web_input**
> WebInputResponse get_web_input(web_input_id)

Retrieve a Web Input

Retrieve a single Web Input's info

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
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Retrieve a Web Input
        api_response = api_instance.get_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->get_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**WebInputResponse**](WebInputResponse.md)

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

# **launch_web_input**
> LaunchWebInputResponse launch_web_input(web_input_id)

Launch a Web Input

Launches the browsers instance, loads the URL specified, and then starts streaming to the specified Live Stream.

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
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Launch a Web Input
        api_response = api_instance.launch_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->launch_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**LaunchWebInputResponse**](LaunchWebInputResponse.md)

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

# **list_web_inputs**
> ListWebInputsResponse list_web_inputs(limit=limit, page=page)

List Web Inputs

List Web Inputs

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
    api_instance = mux_python.WebInputsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)

    try:
        # List Web Inputs
        api_response = api_instance.list_web_inputs(limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->list_web_inputs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]

### Return type

[**ListWebInputsResponse**](ListWebInputsResponse.md)

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

# **reload_web_input**
> ReloadWebInputResponse reload_web_input(web_input_id)

Reload a Web Input

Reloads the page that a Web Input is displaying.  Note: Using this when the Web Input is streaming will display the page reloading. 

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
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Reload a Web Input
        api_response = api_instance.reload_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->reload_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**ReloadWebInputResponse**](ReloadWebInputResponse.md)

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

# **shutdown_web_input**
> ShutdownWebInputResponse shutdown_web_input(web_input_id)

Shut down a Web Input

Ends streaming to the specified Live Stream, and then shuts down the Web Input browser instance.

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
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID

    try:
        # Shut down a Web Input
        api_response = api_instance.shutdown_web_input(web_input_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->shutdown_web_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 

### Return type

[**ShutdownWebInputResponse**](ShutdownWebInputResponse.md)

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

# **update_web_input_url**
> WebInputResponse update_web_input_url(web_input_id, update_web_input_url_request)

Update Web Input URL

Changes the URL that a Web Input loads when it launches.  Note: This can only be called when the Web Input is idle. 

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
    api_instance = mux_python.WebInputsApi(api_client)
    web_input_id = 'abcd1234' # str | The Web Input ID
update_web_input_url_request = {"url":"https://example.com/hello-there.html"} # UpdateWebInputUrlRequest | 

    try:
        # Update Web Input URL
        api_response = api_instance.update_web_input_url(web_input_id, update_web_input_url_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebInputsApi->update_web_input_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_input_id** | **str**| The Web Input ID | 
 **update_web_input_url_request** | [**UpdateWebInputUrlRequest**](UpdateWebInputUrlRequest.md)|  | 

### Return type

[**WebInputResponse**](WebInputResponse.md)

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

