# CreateWebInputRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the Web Input. | [optional]
**created_at** | **str** | Time the Web Input was created, defined as a Unix timestamp (seconds since epoch). | [optional]
**url** | **str** | The URL for the Web Input to load. | [optional]
**auto_launch** | **bool** | When set to &#x60;true&#x60; the Web Input will automatically launch and start streaming immediately after creation | [optional]
**live_stream_id** | **str** | The Live Stream ID to broadcast this Web Input to | [optional]
**status** | **str** |  | [optional]
**passthrough** | **str** | Arbitrary metadata that will be included in the Web Input details and related webhooks. Can be used to store your own ID for the Web Input. **Max: 255 characters**. | [optional]
**resolution** | **str** | The resolution of the viewport of the Web Input&#39;s browser instance. Defaults to 1920x1080 if not set. | [optional] [default to '1920x1080']
**timeout** | **int** | The number of seconds that the Web Input should stream for before automatically shutting down. | [optional] [default to 3600]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


