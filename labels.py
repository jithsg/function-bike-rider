#write a function that takes in a s3 bucket and images and returns a list of labels for each image
# import libraries

import boto3


s3 = boto3.resource('s3')
# Now you can use the s3 resource to interact with your S3 buckets and objects.
#use fire to create a command line interface that accepts a bucket and image as input and returns a list of labels



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

