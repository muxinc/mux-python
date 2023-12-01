# CreateUploadRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked &#x60;timed_out&#x60; | [optional] [default to 3600]
**cors_origin** | **str** | If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers. | [optional]
**new_asset_settings** | [**CreateAssetRequest**](CreateAssetRequest.md) |  | [optional]
**test** | **bool** |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


