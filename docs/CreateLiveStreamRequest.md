# CreateLiveStreamRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**playback_policy** | [**list[PlaybackPolicy]**](PlaybackPolicy.md) |  | [optional] 
**new_asset_settings** | [**CreateAssetRequest**](CreateAssetRequest.md) |  | [optional] 
**reconnect_window** | **float** | When live streaming software disconnects from Mux, either intentionally or due to a drop in the network, the Reconnect Window is the time in seconds that Mux should wait for the streaming software to reconnect before considering the live stream finished and completing the recorded asset. Default: 60 seconds | [optional] [default to 60]
**passthrough** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


