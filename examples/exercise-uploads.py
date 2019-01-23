# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import ApiException

# Exercises all direct upload operations:
# create-direct-upload
# list-direct-uploads
# get-direct-upload
# cancel-direct-upload

def print_debug(log_line):
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        print log_line

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
uploads_api = mux_python.DirectUploadsApi(mux_python.ApiClient(configuration))

# ========== create-direct-upload ==========
create_asset_request = mux_python.CreateAssetRequest(playback_policy=[mux_python.PlaybackPolicy.PUBLIC])
create_upload_request = mux_python.CreateUploadRequest(timeout=3600, new_asset_settings=create_asset_request, cors_origin="philcluff.co.uk")
create_upload_response = uploads_api.create_direct_upload(create_upload_request=create_upload_request)
print_debug(str(create_upload_response))
assert create_upload_response != None
assert create_upload_response.data != None
assert create_upload_response.data.id != None
print "create-direct-upload OK ✅"

# ========== list-direct-uploads ==========
list_direct_uploads_response = uploads_api.list_direct_uploads()
print_debug(str(list_direct_uploads_response))
assert list_direct_uploads_response != None
assert list_direct_uploads_response.data != []
assert list_direct_uploads_response.data[0].id == create_upload_response.data.id
print "list-direct-uploads OK ✅"

# ========== get-direct-upload ==========
upload_response = uploads_api.get_direct_upload(create_upload_response.data.id)
print_debug(str(upload_response))
assert upload_response != None
assert upload_response.data.id != None
assert upload_response.data.id == create_upload_response.data.id
print "get-direct-upload OK ✅"

# ========== cancel-direct-upload ==========
canceled_upload_response = uploads_api.cancel_direct_upload(create_upload_response.data.id)
print_debug(str(canceled_upload_response))
assert canceled_upload_response != None
assert canceled_upload_response.data.id != None
assert canceled_upload_response.data.id == create_upload_response.data.id
assert canceled_upload_response.data.status == "cancelled"
print "cancel-direct-upload OK ✅"

# TODO: At some point I'd like to actually perform an upload here and check the state changes etc. but I don't have time right now.
