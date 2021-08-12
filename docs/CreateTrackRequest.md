# CreateTrackRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**type** | **str** |  | 
**text_type** | **str** |  | 
**language_code** | **str** | The language code value must be a valid BCP 47 specification compliant value. For example, en for English or en-US for the US version of English. | 
**name** | **str** | The name of the track containing a human-readable description. This value must be unique across all the text type and subtitles text type tracks. HLS manifest will associate subtitle text track with this value. For example, set the value to \&quot;English\&quot; for subtitles text track with language_code as en-US. If this parameter is not included, Mux will auto-populate based on the language_code value. | [optional] 
**closed_captions** | **bool** | Indicates the track provides Subtitles for the Deaf or Hard-of-hearing (SDH). | [optional] 
**passthrough** | **str** | Arbitrary metadata set for the track either when creating the asset or track. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


