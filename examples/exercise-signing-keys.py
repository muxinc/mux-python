# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import ApiException

# Exercises all url signing key operations:
#   create-url-signing-key
#   list-url-signing-keys
#   get-url-signing-key
#   delete-url-signing-key

def print_debug(log_line):
    if len(sys.argv) == 2 and sys.argv[1] == "--debug":
        print log_line

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_ACCESS_TOKEN_ID']
configuration.password = os.environ['MUX_ACCESS_TOKEN_SECRET']

# API Client Initialization
keys_api = mux_python.URLSigningKeysApi(mux_python.ApiClient(configuration))

# ========== create-url-signing-key ==========
create_key_response = keys_api.create_url_signing_key()
print_debug(create_key_response)
assert create_key_response != None
assert create_key_response.data.id != None
assert create_key_response.data.private_key != None
print "create-url-signing-key OK ✅"

# ========== list-url-signing-keys ==========
list_keys_response = keys_api.list_url_signing_keys()
print_debug(list_keys_response)
assert list_keys_response != None
assert list_keys_response.data[0].id != None
assert list_keys_response.data[0].id == create_key_response.data.id
assert list_keys_response.data[0].private_key == None
print "list-url-signing-keys OK ✅"

# ========== get-url-signing-key ==========
get_key_response = keys_api.get_url_signing_key(create_key_response.data.id)
print_debug(get_key_response)
assert get_key_response != None
assert get_key_response.data.private_key == None
print "get-url-signing-key OK ✅"

# ========== delete-url-signing-key ==========
keys_api.delete_url_signing_key(create_key_response.data.id)
try:
    deleted_key_response = keys_api.get_url_signing_key(create_key_response.data.id)
except ApiException as e:
    assert e != None
    print "delete-url-signing-key OK ✅"
