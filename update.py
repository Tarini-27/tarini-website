import os
import boto3
import yaml
import zipfile

cb = boto3.client('codebuild')
s3 = boto3.client('s3')
lb = boto3.client('lambda')

def lambda_handler(event, context):
    fileNames_allowed = ["function.py", "function1.py"]
    path=os.environ('name1')
    path=path.split(' ')
    print(path)
    for i in path:
        if i in fileNames_allowed:
            #filename = os.path.basename(i)
            #filename = filename.split('.')
            #filename = zipfile.Zipfile(filename[0], 'w', compression=ZIP_STORED)
            #s3.upload_file('filename', 'sunlife-cybersec-pe-freshers-backup', '2021/')
            s3.put_object(Body='i',Bucket='sunlife-cybersec-pe-freshers-backup',Key='i')
            print("file uploaded to s3 successfully")
        else:
            print("not appropriate file modified")

    
            
            

            
