import os
import time
import mux_python
from mux_python.rest import ApiException

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID_DEV']
configuration.password = os.environ['MUX_TOKEN_SECRET_DEV']

# API Client Initialization
live_api = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))

# Create a live stream
new_asset_settings = mux_python.CreateAssetRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC])
create_live_stream_request = mux_python.CreateLiveStreamRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC], new_asset_settings=new_asset_settings)
create_live_stream_response = live_api.create_live_stream(create_live_stream_request)

# Give back the RTMP entry point playback endpoint
print("New Live Stream created!")
print("RTMP Endpoint: rtmp://live.mux.com/app")
print("Stream Key: " + create_live_stream_response.data.stream_key)
