# -*- coding: utf-8 -*-

import json


def configure_json(json_file):
    """
    Load a JSON file

    :param json_file:
    :return:
    """
    with open(json_file) as json_file:
        data = json.load(json_file)

    return data


def loads(data):
    """
    Creates a JSON based on the data

    :param data:
    :return:
    """
    return json.loads(data)
