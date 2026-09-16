# Module 14.5 of DevOps Bootcamp by [TechWorld with Nana](https://www.techworld-with-nana.com/)
Health Check: EC2 Status Checks

## Technologies used:
- Python
- Boto3
- aws
- Terraform

## Project description:
- Create EC2 Instances with Terraform
- Write a Python script that fetches statuses of EC2 Instances and prints to the console
- Extend the Python script to continuously check the status of EC2 Instances in a specific interval

## Implementation steps:
1. Copy Terraform starting code from [demo repository](https://gitlab.com/twn-devops-bootcamp/latest/14-automation-with-python/terraform/-/tree/feature/starting-code)
2. Execute `terraform init`
3. Add two additional resource definitions for ec2 instances
4. Apply: `terraform apply`
5. Go to aws console and verify that resources are created
6. Add main.py
7. Add Python logic to extract and print state of ec2 instances
8. Run script with `python3 main.py`
9. Use scheduler library to run status check regularly
