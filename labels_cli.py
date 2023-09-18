import fire

from labels import detect_labels

if __name__ == "__main__":
#use fire to create a command line interface that accepts a bucket and image as input and returns a list of labels
    import fire
    fire.Fire(detect_labels)
#write an aws lambda hander function that accepts an s3 event and uses the detect_labels function to return a list of labels for every event

# Path: labels_lambda.py
