import boto3

s3 = boto3.client('s3')

with open('test.txt', 'rb') as f:
    s3.put_object(
    Bucket='luit-2025-pythons3-maroria',
    Key='test_text.txt',
    Body=f,
    ContentType='text/plain'
)
