# Asset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**deleted_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**duration** | **float** |  | [optional] 
**max_stored_resolution** | **str** |  | [optional] 
**max_stored_frame_rate** | **float** |  | [optional] 
**aspect_ratio** | **str** |  | [optional] 
**playback_ids** | [**list[PlaybackID]**](PlaybackID.md) |  | [optional] 
**tracks** | [**list[Track]**](Track.md) |  | [optional] 
**errors** | [**AssetErrors**](AssetErrors.md) |  | [optional] 
**per_title_encode** | **bool** |  | [optional] 
**is_live** | **bool** |  | [optional] 
**passthrough** | **str** |  | [optional] 
**live_stream_id** | **str** |  | [optional] 
**master** | [**AssetMaster**](AssetMaster.md) |  | [optional] 
**master_access** | **str** |  | [optional] [default to 'none']
**mp4_support** | **str** |  | [optional] [default to 'none']
**normalize_audio** | **bool** |  | [optional] [default to False]
**static_renditions** | [**AssetStaticRenditions**](AssetStaticRenditions.md) |  | [optional] 
**recording_times** | [**list[AssetRecordingTimes]**](AssetRecordingTimes.md) | An array of individual live stream recording sessions. A recording session is created on each encoder connection during the live stream | [optional] 
**non_standard_input_reasons** | [**AssetNonStandardInputReasons**](AssetNonStandardInputReasons.md) |  | [optional] 
**test** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


