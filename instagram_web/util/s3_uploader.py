from config import Config
import boto3
import botocore
s3 = boto3.client(
   "s3",
   aws_access_key_id=Config.AWS_ACCESS_KEY,
   aws_secret_access_key=Config.AWS_SECRET_KEY
)

def upload_file_to_s3(file):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    try:
        s3.upload_fileobj(file,Config.AWS_BUCKET_NAME,file.filename,ExtraArgs={"ACL":"public-read","ContentType": file.content_type})
        return True
    except Exception as e:
        print("Something Happened: ", e)
        return False

