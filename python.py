import os
import boto3
import yaml

cb = boto3.client('codebuild')
s3 = boto3.client('s3')
path=os.env('file_name')
# with open(r'buildspec.yaml') as file:
#     path = yaml.load(file, Loader=yaml.FullLoader)
#     print(file_name)

def lambda_handler(event, context):

    # Initialize needed variables
    file_extension_allowed = [".py"]
    fileNames_allowed = ["lambda_1", "lambda_2"]
    #region = event['Records'][0]['awsRegion']

    # Check whether specific file or specific extension file is committed
    trigger = False
    file_name=os.path.basename(path)
    root, extension = os.path.splitext(file_name)
    if ((extension in file_extension_allowed) or (root in fileNames_allowed)):
        trigger = True

    if trigger:
        s3.put_object(Bucket='sunlife-cybersec-pe-freshers-backup',Key='fileName')
            
