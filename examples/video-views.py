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
video_views_api = mux_python.VideoViewsApi(mux_python.ApiClient(configuration))

# List Video Views
print("Listing Video Views: \n")

list_video_views_response = video_views_api.list_video_views(filters=['country:GB', 'browser:Safari'], timeframe=['2:days'])

pprint(list_video_views_response)

for view in list_video_views_response.data:
    print('View ID: ' + view.id)
    print('Viewer OS Family: ' + view.viewer_os_family)
    print('Viewer Application Name: ' + view.viewer_application_name)

    video_view_response = video_views_api.get_video_view(view.id)
    print "Got View without blowing up! ID: " + video_view_response.data.id

    print "\n"
