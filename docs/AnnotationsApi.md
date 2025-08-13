# mux_python.AnnotationsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_annotation**](AnnotationsApi.md#create_annotation) | **POST** /data/v1/annotations | Create Annotation
[**delete_annotation**](AnnotationsApi.md#delete_annotation) | **DELETE** /data/v1/annotations/{ANNOTATION_ID} | Delete Annotation
[**get_annotation**](AnnotationsApi.md#get_annotation) | **GET** /data/v1/annotations/{ANNOTATION_ID} | Get Annotation
[**list_annotations**](AnnotationsApi.md#list_annotations) | **GET** /data/v1/annotations | List Annotations
[**update_annotation**](AnnotationsApi.md#update_annotation) | **PATCH** /data/v1/annotations/{ANNOTATION_ID} | Update Annotation


# **create_annotation**
> AnnotationResponse create_annotation(annotation_input)

Create Annotation

Creates a new annotation.

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
    api_instance = mux_python.AnnotationsApi(api_client)
    annotation_input = {"note":"This is a note","date":1745438400,"sub_property_id":"123456"} # AnnotationInput | 

    try:
        # Create Annotation
        api_response = api_instance.create_annotation(annotation_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->create_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_input** | [**AnnotationInput**](AnnotationInput.md)|  | 

### Return type

[**AnnotationResponse**](AnnotationResponse.md)

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

# **delete_annotation**
> delete_annotation(annotation_id)

Delete Annotation

Deletes an annotation.

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
    api_instance = mux_python.AnnotationsApi(api_client)
    annotation_id = 'annotation_id_example' # str | The annotation ID

    try:
        # Delete Annotation
        api_instance.delete_annotation(annotation_id)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->delete_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | [**str**](.md)| The annotation ID | 

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

# **get_annotation**
> AnnotationResponse get_annotation(annotation_id)

Get Annotation

Returns the details of a specific annotation.

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
    api_instance = mux_python.AnnotationsApi(api_client)
    annotation_id = 'annotation_id_example' # str | The annotation ID

    try:
        # Get Annotation
        api_response = api_instance.get_annotation(annotation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->get_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | [**str**](.md)| The annotation ID | 

### Return type

[**AnnotationResponse**](AnnotationResponse.md)

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

# **list_annotations**
> ListAnnotationsResponse list_annotations(limit=limit, page=page, order_direction=order_direction, timeframe=timeframe)

List Annotations

Returns a list of annotations.

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
    api_instance = mux_python.AnnotationsApi(api_client)
    limit = 25 # int | Number of items to include in the response (optional) (default to 25)
page = 1 # int | Offset by this many pages, of the size of `limit` (optional) (default to 1)
order_direction = 'order_direction_example' # str | Sort order. (optional)
timeframe = ['timeframe_example'] # list[str] | Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=).  Accepted formats are...    * array of epoch timestamps e.g. `timeframe[]=1498867200&timeframe[]=1498953600`   * duration string e.g. `timeframe[]=24:hours or timeframe[]=7:days`  (optional)

    try:
        # List Annotations
        api_response = api_instance.list_annotations(limit=limit, page=page, order_direction=order_direction, timeframe=timeframe)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->list_annotations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to include in the response | [optional] [default to 25]
 **page** | **int**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **order_direction** | **str**| Sort order. | [optional] 
 **timeframe** | [**list[str]**](str.md)| Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60;  | [optional] 

### Return type

[**ListAnnotationsResponse**](ListAnnotationsResponse.md)

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

# **update_annotation**
> AnnotationResponse update_annotation(annotation_id, annotation_input)

Update Annotation

Updates an existing annotation.

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
    api_instance = mux_python.AnnotationsApi(api_client)
    annotation_id = 'annotation_id_example' # str | The annotation ID
annotation_input = {"note":"This is a note","date":1745438400,"sub_property_id":"123456"} # AnnotationInput | 

    try:
        # Update Annotation
        api_response = api_instance.update_annotation(annotation_id, annotation_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AnnotationsApi->update_annotation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **annotation_id** | [**str**](.md)| The annotation ID | 
 **annotation_input** | [**AnnotationInput**](AnnotationInput.md)|  | 

### Return type

[**AnnotationResponse**](AnnotationResponse.md)

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

