# -*- coding: utf-8 -*-

import boto3


def create_aws_session():
    session = boto3.Session(
        profile_name="awsdk-book"
    )
    return session


def split_s3_path(s3_path):
    path_parts = s3_path.replace("s3://", "").split("/")
    bucket = path_parts.pop(0)
    key = "/".join(path_parts)
    return bucket, key



