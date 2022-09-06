# Upload

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Direct Upload. | [optional]
**timeout** | **int** | Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked &#x60;timed_out&#x60; | [optional] [default to 3600]
**status** | **str** |  | [optional]
**new_asset_settings** | [**Asset**](Asset.md) |  | [optional]
**asset_id** | **str** | Only set once the upload is in the &#x60;asset_created&#x60; state. | [optional]
**error** | [**UploadError**](UploadError.md) |  | [optional]
**cors_origin** | **str** | If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers. | [optional]
**url** | **str** | The URL to upload the associated source media to. | [optional]
**test** | **bool** | Indicates if this is a test Direct Upload, in which case the Asset that gets created will be a &#x60;test&#x60; Asset. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


