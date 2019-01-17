# Mux Python
Official Mux API wrapper for python projects 🐍.

Not familiar with Mux? Check out https://mux.com/ for more information.

## Requirements.

Python 2.7 or 3.4+

## Installation

### Via pip

```sh
pip install git+https://github.com/muxinc/mux-python.git
```
(you may need to run `pip` with root permission)

### Via source
```sh
git checkout https://github.com/muxinc/mux-python.git
cd mux-python
python setup.py install --user
```

## Getting Started

### Authentication
To use the Mux API, you'll need an access token and a secret. [Details on obtaining these can be found here in the Mux documentation.](https://docs.mux.com/docs#section-1-get-an-api-access-token)

Its up to you to manage your token and secret. In our examples, we read them from `MUX_ACCESS_TOKEN_ID` and `MUX_ACCESS_TOKEN_SECRET` in your environment.

### Example Usage
Below is a quick example of using mux-python to list the Video assets stored in your Mux account.

Be sure to also checkout the [exmples directory](examples/):
* [List Assets, Live Streams, Signing Keys, and Uploads.](examples/list-everything.py)
* [Create an Asset, wait for it to become availiable, and print its playback URL](examples/ingest.py)
* [Create a new Live Stream and retrieve its Stream key.](examples/create-live-stream.py)

```python
import os
import mux_python
from mux_python.rest import ApiException

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_ACCESS_TOKEN_ID']
configuration.password = os.environ['MUX_ACCESS_TOKEN_SECRET']

# API Client Initialization
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))

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
```

## Issues
If you run into problems, [please raise a GitHub issue,](https://github.com/muxinc/mux-python/issues) filling in the issue template. We'll take a look as soon as possible.

## Contributing
Please do not submit PRs against this package. It is generated from our OpenAPI definitions - [Please open an issue instead!](https://github.com/muxinc/mux-python/issues)

## License
[MIT License.](LICENSE) Copyright 2019 Mux, Inc.
