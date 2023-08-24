import boto3

def list_all_load_balancers():
    elbv2 = boto3.client('elbv2')
    response = elbv2.describe_load_balancers()
    return response['LoadBalancers']

def get_associated_resources(load_balancer_arn):
    elbv2 = boto3.client('elbv2')
    response = elbv2.describe_target_groups(LoadBalancerArn=load_balancer_arn)
    
    associated_resources = []
    
    for target_group in response['TargetGroups']:
        response = elbv2.describe_target_health(TargetGroupArn=target_group['TargetGroupArn'])
        for target in response['TargetHealthDescriptions']:
            associated_resources.append(target['Target']['Id'])
    
    return associated_resources

def main():
    unused_load_balancers = []
    all_load_balancers = list_all_load_balancers()
    
    for lb in all_load_balancers:
        associated_resources = get_associated_resources(lb['LoadBalancerArn'])
        
        if not associated_resources:
            unused_load_balancers.append(lb['LoadBalancerName'])
    
    if unused_load_balancers:
        print("Unused Load Balancers:")
        for lb_name in unused_load_balancers:
            print(lb_name)
    else:
        print("No unused load balancers found.")

if __name__ == "__main__":
    main()
