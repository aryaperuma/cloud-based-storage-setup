import boto3
from botocore.exceptions import NoCredentialsError

# AWS S3 Configuration
AWS_ACCESS_KEY = 'your_access_key'
AWS_SECRET_KEY = 'your_secret_key'
BUCKET_NAME = 'your_bucket_name'

# Initialize a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

# Initialize S3 resource
s3 = session.resource('s3')

def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket"""
    if object_name is None:
        object_name = file_name

    try:
        s3.Bucket(BUCKET_NAME).upload_file(file_name, object_name)
        print(f"Successfully uploaded {file_name} to {BUCKET_NAME}/{object_name}")
    except NoCredentialsError:
        print("Credentials not available")

def list_files():
    """List files in the S3 bucket"""
    print(f"Files in bucket {BUCKET_NAME}:")
    for obj in s3.Bucket(BUCKET_NAME).objects.all():
        print(obj.key)

def delete_file(object_name):
    """Delete a file from the S3 bucket"""
    s3.Object(BUCKET_NAME, object_name).delete()
    print(f"Successfully deleted {object_name} from {BUCKET_NAME}")

if __name__ == '__main__':
    # Example usage
    upload_file('example.txt')  # Replace with your local file
    list_files()
    delete_file('example.txt')  # Replace with the file name you want to delete
