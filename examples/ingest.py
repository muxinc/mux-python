import os
import time
import mux_python
from mux_python.rest import ApiException

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

# Create an asset
input_settings = [mux_python.InputSettings(url='https://storage.googleapis.com/muxdemofiles/mux-video-intro.mp4')]
create_asset_request = mux_python.CreateAssetRequest(input=input_settings, playback_policy=[mux_python.PlaybackPolicy.PUBLIC])

create_asset_response = assets_api.create_asset(create_asset_request=create_asset_request)
print("Created Asset ID: " + create_asset_response.data.id)

# Wait for the asset to become ready, and then print its playback URL
if create_asset_response.data.status != 'ready':

    print "Waiting for asset to become ready..."
    while True:
        asset_response = assets_api.get_asset(create_asset_response.data.id)
        if asset_response.data.status != 'ready':
            print("Asset still not ready. Status was: " + asset_response.data.status)
            time.sleep(1)
        else:
            print "Asset Ready! Playback URL: https://stream.mux.com/" + asset_response.data.playback_ids[0].id + ".m3u8"
            break
