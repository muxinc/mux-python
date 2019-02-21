# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Exercises all export operations:
#   list-video-views
#   get-video-view

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
video_views_api = mux_python.VideoViewsApi(mux_python.ApiClient(configuration))

# List Video Views
list_video_views_response = video_views_api.list_video_views(filters=['country:GB', 'browser:Safari'], timeframe=['7:days'])
logger.print_debug('List Video Views Response ' + str(list_video_views_response))
assert list_video_views_response != None
assert list_video_views_response.data != None
assert list_video_views_response.data[0] != None
print("list-video-views OK ✅")

# Get Video View by ID
video_view_response = video_views_api.get_video_view(list_video_views_response.data[0].id)
assert video_view_response != None
assert video_view_response.data != None
print("get-video-views OK ✅")