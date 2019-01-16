# Mux Python
Official Mux API wrapper for python projects 🐍.

Not familiar with Mux? Check out https://mux.com/ for more information.

## Requirements.

Python 2.7 or 3.4+

## Installation
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/muxinc/mux-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/muxinc/mux-python.git`)

## Getting Started

### Authentication
TODO: Document this.

### Example Usage
Here's a quick example of using mux-python to list the Video assets stored in your Mux account:

```python
from __future__ import print_function
import os
import time
import mux_video_sdk
from mux_video_sdk.rest import ApiException
from pprint import pprint

# Authentication Setup
configuration = mux_video_sdk.Configuration()
configuration.username = os.environ['MUX_ACCESS_TOKEN_ID']
configuration.password = os.environ['MUX_ACCESS_TOKEN_SECRET']

# API Client Initialization
api_instance = mux_video_sdk.AssetsApi(mux_video_sdk.ApiClient(configuration))

# List Assets
print("Listing Assets in account: \n")
try:
    list_assets_success_response = api_instance.list_assets()
    for asset in list_assets_success_response.data:
        print('Asset ID: ' + asset.id)
        print('Status: ' + asset.status)
        print('Duration: ' + str(asset.duration) + "\n")
except ApiException as e:
    print("Exception when calling AssetsApi->list_assets: %s\n" % e)
```

## Issues
If you run into problems, please raise a GitHub issue, filling in the issue template. We'll take a look as soon as possible.

## Contributing
Please do not submit PRs against this package. It is generated from our OpenAPI definitions - [Please open an issue instead!](##Issues)

## License
[MIT License.](LICENSE.md) Copyright 2019 Mux, Inc.
