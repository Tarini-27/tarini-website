import os
import boto3
import yaml
import zipfile

gl = boto3.client('glue')
s3 = boto3.client('s3')
lb = boto3.client('lambda')
fileNames_allowed = ["function.py", "update.py"]
print(os.environ['NAME1'], flush=True)
path=os.environ['NAME1']
path=path.split(' ')
print(path, flush=True)

def get_job(filename):
    try:
        response = gl.get_job(
        JobName=filename
        )
        return response
    except:
        response = gl.create_job(
        Name=filename,
        Role='arn:aws:iam::130159455024:role/SunLifeCyberSecurity-Developer-3857',
        Command={
            'Name': 'glueetl',
            'ScriptLocation': 's3://sunlife-lambda-deploy',
            'PythonVersion': '3'
            }
        )
        print("job created")
        return response

for i in path:
    if i in fileNames_allowed:
            filename = os.path.basename(i)
            #filename = filename.split('.')
            #filename = filename[0]
            #filename = zipfile.Zipfile(filename, 'w', compression=ZIP_STORED)
            s3.upload_file(Filename=filename, Bucket='bucket-22097', Key=filename)
            #s3.put_object(Body='i',Bucket='sunlife-cybersec-pe-freshers-backup',Key='i')
            print("file uploaded to s3 successfully")
            
            filename = filename.split('.')
            filename = filename[0]
            glue_job = get_job(filename)
            
            if glue_job is not None:
                response = gl.start_job_run(
                JobName=filename)
                print("job started successfully")
                  
    else:
        print("error")
            


    
            
            
