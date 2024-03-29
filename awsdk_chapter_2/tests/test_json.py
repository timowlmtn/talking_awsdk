# -*- coding: utf-8 -*-

from .context import awsdk

import unittest


class JsonTestSuite(unittest.TestCase):
    """JSON test cases."""

    def test_configure_json(self):
        result = awsdk.configure_json("data/s3/json-files/table_of_contents.json")

        self.assertEqual("An AWS DataKit", result["title"])

    def test_configure_json_s3(self):
        json_content = awsdk.configure_json("s3://awsdk-book/json-files/table_of_contents.json")

        self.assertEqual("An AWS DataKit", json_content["title"])

if __name__ == '__main__':
    unittest.main()
