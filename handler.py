import json
import boto3
import smart_open

from lib import processor, reader, transformer, writer
from model import configuration


def handler(event=None, context=None):
    if event is None:
        return "Nothing"
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    config = configuration.Config()
    converter = transformer.Transformer()
    s3Reader = reader.Reader(config=config, s3=boto3.client("s3"))
    s3Writer = writer.Writer(config=config, s_o=smart_open)
    dataProcessor = processor.Processor(
        config=config, r=s3Reader, w=s3Writer, t=converter)

    dataProcessor.run(bucket, key)

    return None

if __name__ == "__main__":
    with open("event.json", "r") as f:
        handler(json.load(f), None)
