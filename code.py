import boto3

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2')
    machine_names = []
    running_instance = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    for instance in running_instance:
        for tag in instance.tags:
            if tag['Key'] == 'env' and tag['Value'] == 'test':
                machine_names.append(instance.instance_id)
                instance.stop()
    #Return ID
    return machine_names
