import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    ec2.instances.filter(InstanceIds=["i-0eb6cb8607c458bfd"]).stop()
    print("Complete")
