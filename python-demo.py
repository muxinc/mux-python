from __future__ import print_function
import os
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint

# To install package locally (see python-sdk/README.md):
# cd python-sdk
# python setup.py install --user

# Auth Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_ACCESS_TOKEN_ID']
configuration.password = os.environ['MUX_ACCESS_TOKEN_SECRET']

# API Client Init
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))
live_streams_api = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
direct_uploads_api = mux_python.DirectUploadsApi(mux_python.ApiClient(configuration))
url_signing_keys_api = mux_python.URLSigningKeysApi(mux_python.ApiClient(configuration))

# List Assets
print("Listing Assets: \n")
try:
    list_assets_response = assets_api.list_assets()
    for asset in list_assets_response.data:
        print('Asset ID: ' + asset.id)
        print('Status: ' + asset.status)
        print('Duration: ' + str(asset.duration) + "\n")
except ApiException as e:
    print("Exception when calling AssetsApi->list_assets: %s\n" % e)

# List Live Streams
print("Listing Live Streams: \n")
try:
    list_live_streams_response = live_streams_api.list_live_streams()
    for live_stream in list_live_streams_response.data:
        print('Live Stream ID: ' + live_stream.id)
        print('Status: ' + live_stream.status)
        print('Stream Key: ' + live_stream.stream_key + "\n")
except ApiException as e:
    print("Exception when calling LiveStreamsApi->list_live_streams: %s\n" % e)

# List Direct Uploads
print("Listing Direct Uploads: \n")
try:
    list_direct_uploads_response = direct_uploads_api.list_direct_uploads()
    for upload in list_direct_uploads_response.data:
        print('Status: ' + upload.status)
        print('Asset ID: ' + str(upload.asset_id) + "\n") # asset_id can be None
except ApiException as e:
    print("Exception when calling DirectUploadApi->list_direct_uploads: %s\n" % e)

# List URL Signing Keys
print("Listing URL Signing Keys: \n")
try:
    list_url_signing_keys_response = url_signing_keys_api.list_url_signing_keys()
    for key in list_url_signing_keys_response.data:
        print('Signing Key ID: ' + key.id)
except ApiException as e:
    print("Exception when calling URLSigningKeysApi->list_url_signing_keys: %s\n" % e)
