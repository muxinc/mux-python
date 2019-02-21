import os
import mux_python
from mux_python.rest import ApiException
from pprint import pprint

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']
configuration.debug = True

# API Client Initialization
metrics_api = mux_python.MetricsApi(mux_python.ApiClient(configuration))

# List Breakdown Values
print("Listing Breakdown Values: \n")
list_breakdown_values_response = metrics_api.list_breakdown_values(metric_id='video_startup_time', group_by='browser', timeframe=['7:days'])
pprint(list_breakdown_values_response)

# Get Overall Values
print("Getting Overall Values: \n")
get_overall_values_response = metrics_api.get_overall_values(metric_id='video_startup_time', timeframe=['7:days'])
pprint(get_overall_values_response)

# List Insights
print("Listing Insights: \n")
list_insights_response = metrics_api.list_insights(metric_id='video_startup_time', timeframe=['7:days'])
pprint(list_insights_response)

# Get Metric Timeseries Data
print("Getting Metric Timeseries Data:\n")
get_metric_timeseries_data_response = metrics_api.get_metric_timeseries_data(metric_id='video_startup_time')
pprint(get_metric_timeseries_data_response)

# List All Metric Values (comparison)
print("List All metric values (comparison):\n")
list_all_metric_values_response = metrics_api.list_all_metric_values()
pprint(list_all_metric_values_response)
