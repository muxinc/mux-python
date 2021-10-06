![Mux Python Banner](github-python-sdk.png)

![](https://github.com/muxinc/mux-python/workflows/Integration%20Test/badge.svg)

# Mux Python

Official Mux API wrapper for python projects, supporting both Mux Data and Mux Video.

[Mux Video](https://mux.com/video) is an API-first platform, powered by data and designed by video experts to make beautiful video possible for every development team.

[Mux Data](https://mux.com/data) is a platform for monitoring your video streaming performance with just a few lines of code. Get in-depth quality of service analytics on web, mobile, and OTT devices.

Not familiar with Mux? Check out https://mux.com/ for more information.

## Requirements

Python 2.7 or 3.4+

### Compatibility with Ubuntu 14.04

Mux uses cross signed TLS root certificates, which may not be compatible with Ubuntu 14.04 LTS [as documented in this issue](https://github.com/certifi/python-certifi/issues/26). We suggest upgrading to a later LTS operating system if you encounter this issue.

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

### Overview

Mux Python is a code generated lightweight wrapper around the Mux REST API and reflects them accurately. This has a few consequences you should watch out for:

1) For almost all API responses, the object you're looking for will be in the `data` field on the API response object, as in the example below. This is because we designed our APIs with similar concepts to the [JSON:API](https://jsonapi.org/) standard. This means we'll be able to return more metadata from our API calls (such as related entities) without the need to make breaking changes to our APIs. We've decided not to hide that in this library.

2) We don't use a lot of object orientation. For example API calls that happen on a single asset don't exist in the asset class, but are API calls in the AssetsApi which require an asset ID.

### Authentication
To use the Mux API, you'll need an access token and a secret. [Details on obtaining these can be found here in the Mux documentation.](https://docs.mux.com/docs#section-1-get-an-api-access-token)

Its up to you to manage your token and secret. In our examples, we read them from `MUX_TOKEN_ID` and `MUX_TOKEN_SECRET` in your environment.

### Example Usage
Below is a quick example of using mux-python to list the Video assets stored in your Mux account.

Be sure to also checkout the [examples directory](examples/):
* [List Assets, Live Streams, Signing Keys, and Uploads.](examples/video/list-everything.py)
* [Create an Asset, wait for it to become availiable, and print its playback URL](examples/video/ingest.py)
* [Create a new Live Stream and retrieve its Stream key.](examples/video/create-live-stream.py)

There's also example usage of every API call (also used for testing):
* [Video](examples/video/)
  * [Assets](examples/video/exercise-assets.py)
  * [Live Streams](examples/video/exercise-live-streams.py)
  * [Signing Keys](examples/video/exercise-signing-keys.py)
  * [Uploads](examples/video/exercise-uploads.py)
* [Data](examples/data/)
  * [Errors](examples/data/exercise-errors.py)
  * [Exports](examples/data/exercise-exports.py)
  * [Filters](examples/data/exercise-filters.py)
  * [Metrics](examples/data/exercise-metrics.py)
  * [Video Views](examples/data/exercise-video-views.py)

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

All exceptions inherit from `ApiException`, you can catch it as in the example above, or you can catch one of the more specific exceptions below. You can check the fields `error_type` and `error_messages` in all Exceptions to see what error the Mux API reported.

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
