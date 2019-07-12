# coding: utf-8

import os
import sys
import time
import mux_python
from mux_python.rest import NotFoundException
import logger

# Exercises all metrics operations:
#   list-breakdown-values
#   get-overall-values
#   list-insights
#   get-metric-timeseries-data
#   list-all-metric-values

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

# API Client Initialization
metrics_api = mux_python.MetricsApi(mux_python.ApiClient(configuration))

# ========== list-breakdown-values ==========
list_breakdown_values_response = metrics_api.list_breakdown_values(metric_id='video_startup_time', group_by='browser', timeframe=['7:days'])
logger.print_debug('List Breakdown Values: Response' + str(list_breakdown_values_response))
assert list_breakdown_values_response != None
assert list_breakdown_values_response.data != None
print("list-breakdown-values OK ✅")

# ========== get-overall-values ==========
get_overall_values_response = metrics_api.get_overall_values(metric_id='video_startup_time', timeframe=['7:days'])
logger.print_debug('Get Overall Values Response: ' + str(get_overall_values_response))
assert get_overall_values_response != None
assert get_overall_values_response.data != None
print("get-overall-values OK ✅")

# ========== list-insights ==========
list_insights_response = metrics_api.list_insights(metric_id='video_startup_time', timeframe=['7:days'])
logger.print_debug('List Insights Response: ' + str(list_insights_response))
assert list_insights_response != None
assert list_insights_response.data != None
print("list-insights OK ✅")

# ========== get-metric-timeseries-data ==========
get_metric_timeseries_data_response = metrics_api.get_metric_timeseries_data(metric_id='video_startup_time',  timeframe=['7:days'])
logger.print_debug('Get Metric Timeseries Data Response: ' + str(get_metric_timeseries_data_response))
assert get_metric_timeseries_data_response != None
assert get_metric_timeseries_data_response.data != None
print("get-metric-timeseries-data OK ✅")

# ========== list-all-metric-values ==========
list_all_metric_values_response = metrics_api.list_all_metric_values()
logger.print_debug('List All Metric Values Response: ' + str(list_all_metric_values_response))
assert list_all_metric_values_response != None
assert list_all_metric_values_response.data != None
print("list-all-metric-values OK ✅")
