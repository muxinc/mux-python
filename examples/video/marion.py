# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID_DEV']
configuration.password = os.environ['MUX_TOKEN_SECRET_DEV']

assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))
playback_ids_api = mux_python.PlaybackIDApi(mux_python.ApiClient(configuration))

ovl = mux_python.InputSettingsOverlaySettings(vertical_align='top')
watermark =  mux_python.InputSettings(url='/marion-onboarding-assets/baguette.jpg',overlay_settings=ovl)
video = mux_python.InputSettings(url='marion-onboarding-assets/movie_1_test.mov')

input_settings = [video,watermark]
print(input_settings)

create_asset_request = mux_python.CreateAssetRequest(input=input_settings, playback_policy=[mux_python.PlaybackPolicy.PUBLIC])
create_asset_response = assets_api.create_asset(create_asset_request)
logger.print_debug("Created Asset: " + str(create_asset_response))
assert create_asset_response != None
assert create_asset_response.data.id != None

print("create-asset OK ✅")

if create_asset_response.data.status != 'ready':
    print("    waiting for asset to become ready...")
    while True:
        # ========== get-asset ==========
        asset_response = assets_api.get_asset(create_asset_response.data.id)
        assert asset_response != None
        assert asset_response.data.id == create_asset_response.data.id
        if asset_response.data.status != 'ready':
            logger.print_debug("Asset still not ready. Status was: " + asset_response.data.status)
            time.sleep(1)
        else:
            # ========== get-asset-input-info ==========
            logger.print_debug("Asset Ready. Checking input info.")
            get_asset_input_info_response = assets_api.get_asset_input_info(create_asset_response.data.id)
            logger.print_debug("Got Asset Input Info: " + str(get_asset_input_info_response))
            assert get_asset_input_info_response != None
            assert get_asset_input_info_response.data != None
            break
print("get-asset OK ✅")
print("get-asset-input-info OK ✅")

add_captions = mux_python.CreateTrackRequest(url="marion-onboarding-assets/captions.vtt", type="text", text_type="subtitles", language_code="en", closed_captions=True, name="English")
caption_track = assets_api.create_asset_track(create_asset_response.data.id, add_captions)
assert caption_track != None
assert caption_track.data != None
assert caption_track.data.id != None
assert caption_track.data.name == 'English'

print("create-asset-track OK ✅")
