# AssetStaticRenditions

An object containing the current status of any static renditions (mp4s). The object does not exist if no static renditions have been requested. See [Download your videos](https://docs.mux.com/guides/enable-static-mp4-renditions) for more information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates the status of downloadable MP4 versions of this asset. | [optional] [default to 'disabled']
**files** | [**list[AssetStaticRenditionsFiles]**](AssetStaticRenditionsFiles.md) | Array of file objects. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


