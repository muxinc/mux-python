# AssetProgress

Detailed state information about the asset ingest process.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The detailed state of the asset ingest process. This field is useful for relaying more granular processing information to end users when a [non-standard input is encountered](https://www.mux.com/docs/guides/minimize-processing-time#non-standard-input).  - &#x60;ingesting&#x60;: Asset is being ingested (initial processing before or after transcoding). While in this state, the &#x60;progress&#x60; percentage will be 0. - &#x60;transcoding&#x60;: Asset is undergoing non-standard transcoding. For assets with a &#x60;delivery_profile&#x60; of &#x60;hls_podcast&#x60;, the &#x60;progress&#x60; percentage runs from 0 to 50 while transcoding. - &#x60;optimizing&#x60;: Asset is finishing additional processing its &#x60;delivery_profile&#x60; requires, such as measuring each rendition&#39;s bitrate for &#x60;hls_podcast&#x60; assets. &#x60;status&#x60; stays &#x60;preparing&#x60;, and the &#x60;progress&#x60; percentage runs from 50 to 100. - &#x60;completed&#x60;: Asset processing is complete (&#x60;status&#x60; is &#x60;ready&#x60;). While in this state, the &#x60;progress&#x60; percentage will be 100. - &#x60;live&#x60;: Asset is a live stream currently in progress. While in this state, the &#x60;progress&#x60; percentage will be -1. - &#x60;errored&#x60;: Asset has encountered an error (&#x60;status&#x60; is &#x60;errored&#x60;). While in this state, the &#x60;progress&#x60; percentage will be -1.  | [optional]
**progress** | **float** | Represents the estimated completion percentage. Returns &#x60;0 - 100&#x60; when in &#x60;ingesting&#x60;, &#x60;transcoding&#x60;, &#x60;optimizing&#x60;, or &#x60;completed&#x60; state, and &#x60;-1&#x60; when in &#x60;live&#x60; or &#x60;errored&#x60; state. | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


