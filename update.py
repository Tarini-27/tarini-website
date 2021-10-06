import os
import boto3
import yaml
import zipfile

cb = boto3.client('codebuild')
s3 = boto3.client('s3')
lb = boto3.client('lambda')

def lambda_handler(event, context):
    file_extension_allowed = [".py"]
    fileNames_allowed = ["function", "function1"]
    path=os.environ('file_name')
    print(path)
    for i in path:
        if i in fileNames_allowed:
            filename = os.path.basename(path)
            filename = zipfile.Zipfile(filename, 'w', compression=ZIP_STORED)
            s3.upload_file('filename', sunlife-cybersec-pe-freshers-backup', '2021')
            print("file uploaded to s3 successfully")
        else:
            print("not appropriate file modified")

    
            
            

            
