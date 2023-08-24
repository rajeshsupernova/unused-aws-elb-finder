# unused-aws-elb-finder
Python script to find unused aws loadbalancer
# 
Python script that uses the AWS Boto3 library to find unused load balancers in your AWS account. Make sure you have Boto3 installed (pip install boto3) and have configured your AWS credentials properly before running the script.

This script uses the boto3 library to interact with AWS services. It first lists all load balancers in your account and then checks each load balancer to see if it has associated resources. If a load balancer has no associated resources, it's considered unused and added to the unused_load_balancers list. Finally, the script prints out the names of the unused load balancers.

Make sure you have the necessary AWS credentials configured before running the script. Also, keep in mind that AWS services and APIs might have changed since my last knowledge update in September 2021, so make sure to consult the latest AWS documentation if you encounter any issues.

## AWs credentials
AWS credentials can be configured in a few different ways depending on your use case and preferences. Here are a couple of common methods:

### AWS CLI Configuration:
If you have the AWS Command Line Interface (CLI) installed, you can use the aws configure command to set up your credentials. Open your terminal and run:

```
aws configure
```
It will prompt you to enter your AWS Access Key ID, Secret Access Key, default region, and output format. These credentials will be saved in a configuration file on your system.

### Environment Variables:
You can also set the AWS credentials as environment variables. In Unix-like systems, you can do this in your terminal:

```
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_DEFAULT_REGION=your_default_region
```
You'll need to set these environment variables every time you open a new terminal session or add these lines to a startup script (e.g., .bashrc, .zshrc) to make them persistent.

### AWS Shared Credentials File:
You can create a shared credentials file (usually located at ~/.aws/credentials) and manually add your credentials like this:

```
[default]
aws_access_key_id = your_access_key
aws_secret_access_key = your_secret_key
```
### IAM Roles (for EC2 instances and other AWS services):
If your code is running on an AWS resource like an EC2 instance, you can assign an IAM role to that instance. The credentials will be automatically provided to the code without any explicit configuration.

### Using Boto3 with Explicit Credentials:
In your Python script, you can pass the credentials explicitly when creating Boto3 clients or resources:

```
import boto3

session = boto3.Session(
    aws_access_key_id='your_access_key',
    aws_secret_access_key='your_secret_key',
    region_name='your_region'
)

elbv2 = session.client('elbv2')
```
Please note that for security reasons, it's recommended to use IAM roles or environment variables to store your credentials rather than hardcoding them in your scripts or code. Always ensure that your credentials are kept secure and not shared publicly.
