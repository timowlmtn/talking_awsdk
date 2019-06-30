
#--------------------------------------------------------------------------------
# The Provider is used to create, manage, and update infrastructure resources
#
#  See: https://www.terraform.io/docs/providers/aws/index.html
#
# This will require the setup of the AWS access keys.
#
# terraform plan
#
provider "aws" {
  version = "~> 2.7"
  region = "us-east-1"
  profile = "awsdk-book"
}


#--------------------------------------------------------------------------------
# S3
#

resource "aws_s3_bucket" "s3_bucket" {
  bucket = "awsdk-book"
  acl    = "private"
}


resource "aws_s3_bucket_object" "jsonpath_config" {
  bucket = "${aws_s3_bucket.s3_bucket.bucket}"
  key    = "json-files/table_of_contents.json"
  source = "../../data/s3/json-files/table_of_contents.json"
}
