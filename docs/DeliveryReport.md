# DeliveryReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_stream_id** | **str** | Unique identifier for the live stream that created the asset. | [optional]
**asset_id** | **str** | Unique identifier for the asset. | [optional]
**passthrough** | **str** | The &#x60;passthrough&#x60; value for the asset. | [optional]
**created_at** | **str** | Time at which the asset was created. Measured in seconds since the Unix epoch. | [optional]
**deleted_at** | **str** | If exists, time at which the asset was deleted. Measured in seconds since the Unix epoch. | [optional]
**asset_state** | **str** | The state of the asset. | [optional]
**asset_duration** | **float** | The duration of the asset in seconds. | [optional]
**asset_resolution_tier** | **str** | The resolution tier that the asset was ingested at, affecting billing for ingest &amp; storage | [optional]
**asset_encoding_tier** | **str** | This field is deprecated. Please use &#x60;asset_video_quality&#x60; instead. The encoding tier that the asset was ingested at. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**asset_video_quality** | **str** | The video quality that the asset was ingested at. This field replaces &#x60;asset_encoding_tier&#x60;. [See the video quality guide for more details.](https://docs.mux.com/guides/use-video-quality-levels) | [optional]
**delivered_seconds** | **float** | Total number of delivered seconds during this time window. | [optional]
**delivered_seconds_by_resolution** | [**DeliveryReportDeliveredSecondsByResolution**](DeliveryReportDeliveredSecondsByResolution.md) |  | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


