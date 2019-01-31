# Mux Python
Official Mux API wrapper for python projects 🐍.

Mux Video is an API-first platform, powered by data and designed by video experts to make beautiful video possible for every development team.

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

Its up to you to manage your token and secret. In our examples, we read them from `MUX_TOKEN_ID` and `MUX_TOKEN_SECRET` in your environment.

### Example Usage
Below is a quick example of using mux-python to list the Video assets stored in your Mux account.

Be sure to also checkout the [exmples directory](examples/):
* [List Assets, Live Streams, Signing Keys, and Uploads.](examples/list-everything.py)
* [Create an Asset, wait for it to become availiable, and print its playback URL](examples/ingest.py)
* [Create a new Live Stream and retrieve its Stream key.](examples/create-live-stream.py)

There's also example usage of every API call (also used for testing):
* [Assets API](examples/exercise-assets.py)
* [Live Streams API](examples/exercise-live-streams.py)
* [Signing Keys API](examples/exercise-signing-keys.py)
* [Uploads API](examples/exercise-uploads.py)

```python
import os
import mux_python
from mux_python.rest import ApiException

# Authentication Setup
configuration = mux_python.Configuration()
configuration.username = os.environ['MUX_TOKEN_ID']
configuration.password = os.environ['MUX_TOKEN_SECRET']

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

## Exceptions & Error Handling

All exceptions inherit from `ApiException`, you can catch it as in the example above, or you can catch one of the more specific exceptions below:

### NotFoundException

`NotFoundException` is thrown when a resource is not found. This is useful when trying to get an entity by its ID, for example `get_asset("some-id-here")` in the AssetsApi.

### UnauthorizedException

`UnauthorizedException` is thrown when Mux cannot authenticate your request. [You should check you have configured your credentials correctly.](#authentication)

### ServiceException

`ServiceException` is thrown when Mux returns a HTTP 5XX Status Code. If you encounter this reproducibly, please get in touch with [support@mux.com](mailto:support@mux.com).

## Documentation

[Be sure to check out the documentation in the `docs` directory.](docs/)

## Issues
If you run into problems, [please raise a GitHub issue,](https://github.com/muxinc/mux-python/issues) filling in the issue template. We'll take a look as soon as possible.

## Contributing
Please do not submit PRs against this package. It is generated from our OpenAPI definitions - [Please open an issue instead!](https://github.com/muxinc/mux-python/issues)

## License
[MIT License.](LICENSE) Copyright 2019 Mux, Inc.
