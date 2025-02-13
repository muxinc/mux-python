# StaticRendition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the static rendition file | [optional]
**ext** | **str** | Extension of the static rendition file | [optional]
**height** | **int** | The height of the static rendition&#39;s file in pixels | [optional]
**width** | **int** | The width of the static rendition&#39;s file in pixels | [optional]
**bitrate** | **int** | The bitrate in bits per second | [optional]
**filesize** | **str** | The file size in bytes | [optional]
**type** | **str** | Indicates the static rendition type of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]
**status** | **str** | Indicates the status of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. * &#x60;ready&#x60; indicates the MP4 has been generated and is ready for download * &#x60;preparing&#x60; indicates the asset has not been ingested or the static rendition is still being generated after an asset is ready * &#x60;skipped&#x60; indicates the static rendition will not be generated because the requested resolution conflicts with the asset attributes after the asset has been ingested * &#x60;errored&#x60; indicates the static rendition cannot be generated. For example, an asset could not be ingested  | [optional]
**resolution_tier** | **str** | Indicates the resolution tier of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]
**resolution** | **str** | Indicates the resolution of this specific MP4 version of this asset. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]
**id** | **str** | The ID of this static rendition, used in managing this static rendition. This field is only valid for &#x60;static_renditions&#x60;, not for &#x60;mp4_support&#x60;. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


