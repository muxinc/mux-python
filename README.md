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
git checkout git@github.com:muxinc/mux-python.git
cd mux-python
python setup.py install --user
```

## Getting Started

### Authentication
TODO: Document this.

### Example Usage
Here's a quick example of using mux-python to list the Video assets stored in your Mux account.

[For more examples, check out python-demo.py.](python-demo.py)

```python
from __future__ import print_function
import os
import time
import mux_python
from mux_python.rest import ApiException
from pprint import pprint

# Auth Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_ACCESS_TOKEN_ID']
configuration.password = os.environ['MUX_ACCESS_TOKEN_SECRET']

# API Client Init
assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))
live_streams_api = mux_python.LiveStreamsApi(mux_python.ApiClient(configuration))
direct_uploads_api = mux_python.DirectUploadsApi(mux_python.ApiClient(configuration))
# signing_key_api = mux_python.URLSigningKeysApi()

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
If you run into problems, please raise a GitHub issue, filling in the issue template. We'll take a look as soon as possible.

## Contributing
Please do not submit PRs against this package. It is generated from our OpenAPI definitions - [Please open an issue instead!](##Issues)

## License
[MIT License.](LICENSE.md) Copyright 2019 Mux, Inc.
