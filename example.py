import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAUD5IBRIRYER2PMGO'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'python-image-upload'


data = open('bitmoji.png', 'rb')

# S3 Connect
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
# Image download
s3.Bucket(BUCKET_NAME).put_object(Key='file_upload/bitmoji.png', Body=data)
# This is where you want to download it too.

print ("Done")