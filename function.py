import json
import boto3
def handler(event, context):
    client = boto3.client('glue')
    response = client.create_database(
    CatalogId='130159455024',
    DatabaseInput={
        'Name': 'test-database',
    }
    )

    response1 = client.create_crawler(
    Name='test_crawler',
    Role='arn:aws:iam::130159455024:role/SunLifeCyberSecurity-Developer-3857',
    DatabaseName='test-database',
    Targets={
        'S3Targets': [
            {
                'Path': 's3://sunlife-cyber-security-firehose/Firehose_test_guardiam/testset.json'
            }
        ]
    } 
    TablePrefix='glue-test',
    )

    response2 = client.start_crawler(
    Name='test_crawler'
    )