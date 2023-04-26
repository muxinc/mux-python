# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger


# Exercises all url signing key operations.

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
keys_api = mux_python.URLSigningKeysApi(mux_python.ApiClient(configuration))

# ========== create-url-signing-key ==========
create_key_response = keys_api.create_url_signing_key()
logger.print_debug(create_key_response)
assert create_key_response != None
assert create_key_response.data.id != None
assert create_key_response.data.private_key != None
print("create-url-signing-key OK ✅")

# ========== list-url-signing-keys ==========
list_keys_response = keys_api.list_url_signing_keys()
logger.print_debug(list_keys_response)
assert list_keys_response != None
assert list_keys_response.data[-1].id != None
assert list_keys_response.data[-1].id == create_key_response.data.id
assert list_keys_response.data[-1].private_key == None
print("list-url-signing-keys OK ✅")

# ========== get-url-signing-key ==========
get_key_response = keys_api.get_url_signing_key(create_key_response.data.id)
logger.print_debug(get_key_response)
assert get_key_response != None
assert get_key_response.data.private_key == None
print("get-url-signing-key OK ✅")

# ========== delete-url-signing-key ==========
keys_api.delete_url_signing_key(create_key_response.data.id)
try:
    print("Sleeping for 60 seconds to ensure key cache is invalidated ⏳")
    for remaining in range(60, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rSleep complete! ⏳            \n")
    keys_api.get_url_signing_key(create_key_response.data.id)
    print("Should have 404'd when getting deleted signing key ❌ ")
    sys.exit(1)
except NotFoundException as e:
    assert e != None
    print("delete-url-signing-key OK ✅")
