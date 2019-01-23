# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import ApiException

# Exercises all asset operations:
#   get-asset
#   delete-asset
#   create-asset
#   list-assets
#   get-asset-input-info
#   create-asset-playback-id
#   get-asset-playback-id
#   delete-asset-playback-id
#   update-asset-mp4-support

def print_debug(log_line):
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        print log_line

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_ACCESS_TOKEN_ID']
configuration.password = os.environ['MUX_ACCESS_TOKEN_SECRET']

# API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

# ========== create-asset ==========
input_settings = [mux_python.InputSettings(url='https://storage.googleapis.com/muxdemofiles/mux-video-intro.mp4')]
create_asset_request = mux_python.CreateAssetRequest(input=input_settings)
create_asset_response = assets_api.create_asset(create_asset_request=create_asset_request)
print_debug("Created Asset: " + str(create_asset_response))
assert create_asset_response != None
assert create_asset_response.data.id != None
print "create-asset OK ✅"

# ========== list-assets ==========
list_assets_response = assets_api.list_assets()
print_debug ("Got List Asset Response: " + str(list_assets_response))
assert list_assets_response != None
assert list_assets_response.data[0].id == create_asset_response.data.id
print "list-assets OK ✅"

# Wait for the asset to become ready...
if create_asset_response.data.status != 'ready':
    print "    waiting for asset to become ready..."
    while True:
        # ========== get-asset ==========
        asset_response = assets_api.get_asset(create_asset_response.data.id)
        assert asset_response != None
        assert asset_response.data.id == create_asset_response.data.id
        if asset_response.data.status != 'ready':
            print_debug("Asset still not ready. Status was: " + asset_response.data.status)
            time.sleep(1)
        else:
            # ========== get-asset-input-info ==========
            print_debug("Asset Ready. Checking input info.")
            get_asset_input_info_response = assets_api.get_asset_input_info(create_asset_response.data.id)
            print_debug("Got Asset Input Info: " + str(get_asset_input_info_response))
            assert get_asset_input_info_response != None
            assert get_asset_input_info_response.data != None
            break
print "get-asset OK ✅"
print "get-asset-input-info OK ✅"

# ========== create-asset-playback-id ==========
create_playback_id_request = mux_python.CreatePlaybackIDRequest(policy=mux_python.PlaybackPolicy.PUBLIC)
create_asset_playback_id_response = assets_api.create_asset_playback_id(asset_id=create_asset_response.data.id, create_playback_id_request=create_playback_id_request)
print_debug("Added Playback ID: " + str(create_asset_playback_id_response))
assert create_asset_playback_id_response != None
assert create_asset_playback_id_response.data != None
print "create-asset-playback-id OK ✅"

# ========== get-asset-playback-id ==========d
playback_id_response = assets_api.get_asset_playback_id(asset_id=create_asset_response.data.id, playback_id=create_asset_playback_id_response.data.id)
print_debug("Got Playback ID: " + str(playback_id_response))
assert playback_id_response != None
assert playback_id_response.data != None
assert playback_id_response.data.id == create_asset_playback_id_response.data.id
print "get-asset-playback-id OK ✅"

# ========== update-asset-mp4-support ==========
update_asset_mp4_support_request = mux_python.UpdateAssetMP4SupportRequest(mp4_support="standard")
asset_response_mp4 = assets_api.update_asset_mp4_support(asset_id=create_asset_response.data.id, update_asset_mp4_support_request=update_asset_mp4_support_request)
print_debug("Added MP4 support: " + str(asset_response_mp4))
assert asset_response_mp4 != None
assert asset_response_mp4.data != None
assert asset_response_mp4.data.id == create_asset_response.data.id
assert asset_response_mp4.data.mp4_support == "standard"
print "update-asset-mp4-support OK ✅"

# ========== delete-asset-playback-id ==========
assets_api.delete_asset_playback_id(asset_id=create_asset_response.data.id, playback_id=create_asset_playback_id_response.data.id)
print_debug("Deleted Playback ID (void response) ")
deleted_playback_id_get_asset_response = assets_api.get_asset(create_asset_response.data.id)
assert deleted_playback_id_get_asset_response.data.playback_ids == None
print "delete-asset-playback-id OK ✅"

# ========== delete-asset ==========
assets_api.delete_asset(create_asset_response.data.id)
print_debug("Deleted Asset (void response) ")
try:
    assets_api.get_asset(create_asset_response.data.id)
    print "Should have 404'd when getting deleted asset ❌ "
    sys.exit(1)
except ApiException as e:
    assert e != None
    print "delete-asset OK ✅"
