import boto3

s3 = boto3.client('s3')

s3.upload_file(
    'test_text.txt',
    'luit-2025-pythons3-maroria',
    'test_text_upload.txt',
    ExtraArgs={'ContentType': 'text/plain'}
    )
