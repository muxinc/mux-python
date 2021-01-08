# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
realtime_api = mux_python.RealTimeApi(mux_python.ApiClient(configuration))

# Test coverage here isn't fantastic due to not knowning if the account we're testing against has
# any real-time data. The behaviour has been manually verified against real-world data.

# ========== list-realtime-dimensions ==========
dimensions = realtime_api.list_realtime_dimensions()
logger.print_debug('List Dimensions Response: ' + str(dimensions))
assert dimensions != None
assert dimensions.data != None
assert len(dimensions.data) > 0
assert dimensions.data[0].name != None
assert dimensions.data[0].display_name != None
print("list-realtime-dimensions OK ✅")

# ========== list-realtime-metrics ==========
metrics = realtime_api.list_realtime_metrics()
logger.print_debug('List Metrics Response: ' + str(metrics))
assert metrics != None
assert metrics.data != None
assert len(metrics.data) > 0
assert metrics.data[0].name != None
assert metrics.data[0].display_name != None
print("list-realtime-metrics OK ✅")

# ========== get-realtime-breakdown ==========
breakdown = realtime_api.get_realtime_breakdown('current-rebuffering-percentage', dimension='asn')
logger.print_debug('Get Realtime Breakdown Response: ' + str(breakdown))
assert breakdown != None
assert breakdown.data != None
print("get-realtime-breakdown OK ✅")

# ========== get-realtime-histogram-timeseries ==========
histogram_timeseries = realtime_api.get_realtime_histogram_timeseries('video-startup-time')
logger.print_debug('Get Realtime Histogram Timeseries Response: ' + str(histogram_timeseries))
assert histogram_timeseries != None
assert histogram_timeseries.meta != None
assert histogram_timeseries.meta.buckets != None
assert len(histogram_timeseries.meta.buckets) > 0
assert histogram_timeseries.data != None
assert len(histogram_timeseries.data) > 0
print("get-realtime-histogram-timeseries OK ✅")

# ========== get-realtime-timeseries ==========
timeseries = realtime_api.get_realtime_timeseries('current-rebuffering-percentage')
logger.print_debug('Get Realtime Timeseries Response: ' + str(timeseries))
assert timeseries != None
assert timeseries.data != None
assert len(timeseries.data) > 0
assert timeseries.data[0].date != ''
print("get-realtime-timeseries OK ✅")
