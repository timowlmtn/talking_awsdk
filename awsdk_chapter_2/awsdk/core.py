# -*- coding: utf-8 -*-

# Facade pattern
from . import awsdkjson


def configure_json(json_file):
    return awsdkjson.configure_json(json_file)
