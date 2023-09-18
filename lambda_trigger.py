# Description: This file is used to trigger the lambda function when an image is uploaded to the S3 bucket.

from urllib.parse import unquote_plus
import boto3

def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="us-east-1"):
    # create rekognition client
    rekognition = boto3.client("rekognition", region)
    # get image from s3 bucket
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        MaxLabels=max_labels,
        MinConfidence=min_confidence,
    )
    # return list of labels
    return [label["Name"] for label in response["Labels"]]


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        key = unquote_plus(record["s3"]["object"]["key"])
        labels = detect_labels(bucket, key)
        return labels
    
    