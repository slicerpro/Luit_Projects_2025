import boto3

s3 = boto3.client('s3')

with open('test_text.txt', 'rb') as f:
    s3.put_object(
    Bucket='luit-2025-pythons3-maroria',
    Key='test_text_string.txt',
    Body='Hey! This is a string.',
    ContentType='text/plain'
)
