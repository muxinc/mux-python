# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mux_python
from mux_python.models.monitoring_histogram_timeseries_datapoint import MonitoringHistogramTimeseriesDatapoint  # noqa: E501
from mux_python.rest import ApiException

class TestMonitoringHistogramTimeseriesDatapoint(unittest.TestCase):
    """MonitoringHistogramTimeseriesDatapoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MonitoringHistogramTimeseriesDatapoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mux_python.models.monitoring_histogram_timeseries_datapoint.MonitoringHistogramTimeseriesDatapoint()  # noqa: E501
        if include_optional :
            return MonitoringHistogramTimeseriesDatapoint(
                timestamp = '', 
                sum = 56, 
                p95 = 1.337, 
                median = 1.337, 
                max_percentage = 1.337, 
                bucket_values = [
                    mux_python.models.monitoring_histogram_timeseries_bucket_values.MonitoringHistogramTimeseriesBucketValues(
                        percentage = 1.337, 
                        count = 56, )
                    ], 
                average = 1.337
            )
        else :
            return MonitoringHistogramTimeseriesDatapoint(
        )

    def testMonitoringHistogramTimeseriesDatapoint(self):
        """Test MonitoringHistogramTimeseriesDatapoint"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
