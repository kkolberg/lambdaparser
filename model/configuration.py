class Config(object):

    def __init__(self):
        self._output_bucket = "s3://testbulk-kk/"

    @property
    def Output_Bucket(self):
        return self._output_bucket
