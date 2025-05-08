import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='luit-2025-pythons3-maroria'
    )
print(response)