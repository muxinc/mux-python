# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Exercises all asset operations.

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

# ========== create-asset ==========
add_captions = mux_python.CreateTrackRequest(url="https://tears-of-steel-subtitles.s3.amazonaws.com/tears-fr.vtt", type="text", text_type="subtitles", language_code="fr", closed_captions=False, name="French")
input_settings = [mux_python.InputSettings(url='https://storage.googleapis.com/muxdemofiles/mux-video-intro.mp4'), add_captions]
create_asset_request = mux_python.CreateAssetRequest(input=input_settings)
create_asset_response = assets_api.create_asset(create_asset_request)
logger.print_debug("Created Asset: " + str(create_asset_response))
assert create_asset_response != None
assert create_asset_response.data.id != None
print("create-asset OK ✅")

# ========== list-assets ==========
list_assets_response = assets_api.list_assets()
logger.print_debug ("Got List Asset Response: " + str(list_assets_response))
assert list_assets_response != None
assert list_assets_response.data[0].id == create_asset_response.data.id
print("list-assets OK ✅")

# Wait for the asset to become ready...
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

# ========== create-asset-playback-id ==========
create_playback_id_request = mux_python.CreatePlaybackIDRequest(policy=mux_python.PlaybackPolicy.PUBLIC)
create_asset_playback_id_response = assets_api.create_asset_playback_id(create_asset_response.data.id, create_playback_id_request)
logger.print_debug("Added Playback ID: " + str(create_asset_playback_id_response))
assert create_asset_playback_id_response != None
assert create_asset_playback_id_response.data != None
print("create-asset-playback-id OK ✅")

# ========== get-asset-playback-id ==========
playback_id_response = assets_api.get_asset_playback_id(create_asset_response.data.id, create_asset_playback_id_response.data.id)
logger.print_debug("Got Playback ID: " + str(playback_id_response))
assert playback_id_response != None
assert playback_id_response.data != None
assert playback_id_response.data.id == create_asset_playback_id_response.data.id
print("get-asset-playback-id OK ✅")

# ========== update-asset-mp4-support ==========
update_asset_mp4_support_request = mux_python.UpdateAssetMP4SupportRequest(mp4_support="standard")
asset_response_mp4 = assets_api.update_asset_mp4_support(create_asset_response.data.id, update_asset_mp4_support_request)
logger.print_debug("Added MP4 support: " + str(asset_response_mp4))
assert asset_response_mp4 != None
assert asset_response_mp4.data != None
assert asset_response_mp4.data.id == create_asset_response.data.id
assert asset_response_mp4.data.mp4_support == "standard"
print("update-asset-mp4-support OK ✅")

# ========== create-asset-track ==========
add_captions = mux_python.CreateTrackRequest(url="https://tears-of-steel-subtitles.s3.amazonaws.com/tears-en.vtt", type="text", text_type="subtitles", language_code="en", closed_captions=False, name="English")
caption_track = assets_api.create_asset_track(create_asset_response.data.id, add_captions)
assert caption_track != None
assert caption_track.data != None
assert caption_track.data.id != None
assert caption_track.data.name == 'English'
asset_with_2_captions = assets_api.get_asset(create_asset_response.data.id)
assert len(asset_with_2_captions.data.tracks) == 4 # Audio, Video, French that we ingested with the asset, and the English we added here!
print("create-asset-track OK ✅")

# ========== delete-asset-track ==========
assets_api.delete_asset_track(create_asset_response.data.id, caption_track.data.id)
asset_no_captions = assets_api.get_asset(create_asset_response.data.id)
assert len(asset_no_captions.data.tracks) == 3 # Audio, Video, French that we ingested with the asset
print("delete-asset-track OK ✅")

# ========== delete-asset-playback-id ==========
assets_api.delete_asset_playback_id(create_asset_response.data.id, create_asset_playback_id_response.data.id)
logger.print_debug("Deleted Playback ID (void response) ")
deleted_playback_id_get_asset_response = assets_api.get_asset(create_asset_response.data.id)
assert deleted_playback_id_get_asset_response.data.playback_ids == None
print("delete-asset-playback-id OK ✅")

# ========== delete-asset ==========
assets_api.delete_asset(create_asset_response.data.id)
logger.print_debug("Deleted Asset (void response) ")
try:
    assets_api.get_asset(create_asset_response.data.id)
    print("Should have 404'd when getting deleted asset ❌ ")
    sys.exit(1)
except NotFoundException as e:
    assert e != None
    print("delete-asset OK ✅")
