import boto3
from botocore.exceptions import ClientError
import requests
from io import BytesIO
import uuid
from src.api.utils.aws.config import get_aws_credentials

def upload_image_to_s3(image_url, bucket_name, folder_name):
    aws_credentials = get_aws_credentials()
    s3_client = boto3.client('s3', **aws_credentials)

    # Generate the S3 key (file name in S3)
    unique_filename = f"{uuid.uuid4()}.png"
    s3_key = f"{folder_name}/{unique_filename}"
    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"

    # Download the image
    response =  requests.get(image_url)
    image_data = BytesIO(response.content)

    # Upload the image to S3
    try:
        s3_client.upload_fileobj(
            Fileobj=image_data,
            Bucket=bucket_name,
            Key=s3_key,
            ExtraArgs={'ContentType': 'image/png'}
        )
    except ClientError as e:
        print(f"Failed to upload image to S3: {e}")
        return None

    return s3_url
