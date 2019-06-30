# -*- coding: utf-8 -*-

# Facade pattern
from . import awsdkjson
from . import awsdks3


def configure_json(json_file):
    if json_file.startswith("s3://"):
        (bucket, key) = split_s3_path(json_file)
        session = awsdks3.create_aws_session()
        s3 = session.resource('s3')
        file_content =s3.Object(bucket, key).get()['Body'].read().decode('utf-8')
        return awsdkjson.loads(file_content)
    else:
        return awsdkjson.configure_json(json_file)

def split_s3_path(s3_path):
    path_parts = s3_path.replace("s3://", "").split("/")
    bucket = path_parts.pop(0)
    key = "/".join(path_parts)
    return bucket, key