# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_initializers import V1Initializers


class TestV1Initializers(unittest.TestCase):
    """ V1Initializers unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Initializers(self):
        """
        Test V1Initializers
        """
        model = kubernetes.client.models.v1_initializers.V1Initializers()


if __name__ == '__main__':
    unittest.main()