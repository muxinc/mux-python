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
monitoring_api = mux_python.MonitoringApi(mux_python.ApiClient(configuration))

# Test coverage here isn't fantastic due to not knowning if the account we're testing against has
# any monitoring data. The behaviour has been manually verified against real-world data.

# ========== list-monitoring-dimensions ==========
dimensions = monitoring_api.list_monitoring_dimensions()
logger.print_debug('List Dimensions Response: ' + str(dimensions))
assert dimensions != None
assert dimensions.data != None
assert len(dimensions.data) > 0
assert dimensions.data[0].name != None
assert dimensions.data[0].display_name != None
print("list-monitoring-dimensions OK ✅")

# ========== list-monitoring-metrics ==========
metrics = monitoring_api.list_monitoring_metrics()
logger.print_debug('List Metrics Response: ' + str(metrics))
assert metrics != None
assert metrics.data != None
assert len(metrics.data) > 0
assert metrics.data[0].name != None
assert metrics.data[0].display_name != None
print("list-monitoring-metrics OK ✅")

# ========== get-monitoring-breakdown ==========
breakdown = monitoring_api.get_monitoring_breakdown('current-rebuffering-percentage', dimension='asn')
logger.print_debug('Get Monitoring Breakdown Response: ' + str(breakdown))
assert breakdown != None
assert breakdown.data != None
print("get-monitoring-breakdown OK ✅")

# ========== get-monitoring-histogram-timeseries ==========
histogram_timeseries = monitoring_api.get_monitoring_histogram_timeseries('video-startup-time')
logger.print_debug('Get Monitoring Histogram Timeseries Response: ' + str(histogram_timeseries))
assert histogram_timeseries != None
assert histogram_timeseries.meta != None
assert histogram_timeseries.meta.buckets != None
assert len(histogram_timeseries.meta.buckets) > 0
assert histogram_timeseries.data != None
assert len(histogram_timeseries.data) > 0
print("get-monitoring-histogram-timeseries OK ✅")

# ========== get-monitoring-timeseries ==========
timeseries = monitoring_api.get_monitoring_timeseries('current-rebuffering-percentage')
logger.print_debug('Get Monitoring Timeseries Response: ' + str(timeseries))
assert timeseries != None
assert timeseries.data != None
assert len(timeseries.data) > 0
assert timeseries.data[0].date != ''
print("get-monitoring-timeseries OK ✅")
