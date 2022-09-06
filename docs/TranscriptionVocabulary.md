# TranscriptionVocabulary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Transcription Vocabulary | [optional]
**name** | **str** | The user-supplied name of the Transcription Vocabulary. | [optional]
**phrases** | **list[str]** | Phrases, individual words, or proper names to include in the Transcription Vocabulary. When the Transcription Vocabulary is attached to a live stream&#39;s &#x60;generated_subtitles&#x60; configuration, the probability of successful speech recognition for these words or phrases is boosted. | [optional]
**passthrough** | **str** | Arbitrary user-supplied metadata set for the Transcription Vocabulary. Max 255 characters. | [optional]
**created_at** | **str** | Time the Transcription Vocabulary was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**updated_at** | **str** | Time the Transcription Vocabulary was updated, defined as a Unix timestamp (seconds since epoch). | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


