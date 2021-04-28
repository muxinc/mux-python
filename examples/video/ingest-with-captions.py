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

# API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

# ========== create-asset ==========
add_captions = mux_python.CreateTrackRequest(url="https://tears-of-steel-subtitles.s3.amazonaws.com/tears-en.vtt", type="text", text_type="subtitles", language_code="en", closed_captions=False, name="English")
input_settings = [mux_python.InputSettings(url='https://storage.googleapis.com/muxdemofiles/mux-video-intro.mp4'), add_captions]
create_asset_request = mux_python.CreateAssetRequest(input=input_settings, playback_policy=mux_python.PlaybackPolicy.PUBLIC)
create_asset_response = assets_api.create_asset(create_asset_request)
logger.print_debug("Created Asset: " + str(create_asset_response))
assert create_asset_response != None
assert create_asset_response.data.id != None
print("create-asset OK ✅")
