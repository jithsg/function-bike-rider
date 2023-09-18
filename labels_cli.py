import fire

from labels import detect_labels

if __name__ == "__main__":
#use fire to create a command line interface that accepts a bucket and image as input and returns a list of labels
    import fire
    fire.Fire(detect_labels)