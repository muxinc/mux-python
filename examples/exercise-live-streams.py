# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException

# Exercises all live stream operations:
#   create-live-stream
#   list-live-streams
#   get-live-stream
#   delete-live-stream
#   create-live-stream-playback-id
#   delete-live-stream-playback-id
#   reset-stream-key
#   signal-live-stream-complete

def print_debug(log_line):
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        print log_line

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
live_api = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))

# ========== create-live-stream ==========
new_asset_settings = mux_python.CreateAssetRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC])
create_live_stream_request = mux_python.CreateLiveStreamRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC], new_asset_settings=new_asset_settings)
create_live_stream_response = live_api.create_live_stream(create_live_stream_request=create_live_stream_request)
print_debug(str(create_live_stream_response))
assert create_live_stream_response != None
assert create_live_stream_response.data != None
assert create_live_stream_response.data.id != None
print "create-live-stream OK ✅"

# ========== list-live-streams ==========
list_live_streams_response = live_api.list_live_streams()
print_debug(str(list_live_streams_response))
assert list_live_streams_response != None
assert list_live_streams_response.data != None
assert list_live_streams_response.data[0].id == create_live_stream_response.data.id
print "list-live-streams OK ✅"

# ========== get-live-stream ==========
live_stream_response = live_api.get_live_stream(create_live_stream_response.data.id)
print_debug(str(live_stream_response))
assert live_stream_response != None
assert live_stream_response.data != None
assert live_stream_response.data.id == create_live_stream_response.data.id
print "get-live-stream OK ✅"

# ========== create-live-stream-playback-id ==========
create_playback_id_request = mux_python.CreatePlaybackIDRequest(policy=mux_python.PlaybackPolicy.SIGNED)
create_playback_id_response = live_api.create_live_stream_playback_id(live_stream_id=create_live_stream_response.data.id, create_playback_id_request=create_playback_id_request)
print_debug(str(create_playback_id_response))
assert create_playback_id_response != None
assert create_playback_id_response.data != None
assert create_playback_id_response.data.policy == "signed"
print "create-live-stream-playback-id OK ✅"

# ========== delete-live-stream-playback-id ==========
live_api.delete_live_stream_playback_id(live_stream_id=create_live_stream_response.data.id, playback_id=create_playback_id_response.data.id)
live_stream_response_after_delete_pbid = live_api.get_live_stream(create_live_stream_response.data.id)
print_debug(str(live_stream_response_after_delete_pbid))
assert len(live_stream_response_after_delete_pbid.data.playback_ids) == 1
assert live_stream_response_after_delete_pbid.data.playback_ids[0].policy == "public"
print "delete-live-stream-playback-id OK ✅"

# ========== reset-stream-key ==========
live_stream_response_new_stream_key = live_api.reset_stream_key(create_live_stream_response.data.id)
print_debug(live_stream_response_new_stream_key)
assert live_stream_response_new_stream_key != None
assert live_stream_response_new_stream_key.data.stream_key != create_live_stream_response.data.stream_key
print "reset-stream-key OK ✅"

# ========== signal-live-stream-complete ==========
try:
    live_api.signal_live_stream_complete(create_live_stream_response.data.id)
except ApiException as e:
    print "Should not have errored when signalling live stream complete ❌ "
    sys.exit(1)
print "signal-live-stream-complete OK ✅"

# ========== delete-live-stream ==========
live_api.delete_live_stream(create_live_stream_response.data.id)
print_debug("Deleted Live Stream (void response) ")
try:
    deleted_live_stream_response = live_api.get_live_stream(create_live_stream_response.data.id)
    print "Should have 404'd when getting deleted live stream ❌ "
    sys.exit(1)
except NotFoundException as e:
    assert e != None
    print "delete-live-stream OK ✅"
