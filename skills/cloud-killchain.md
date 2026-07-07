---
name: cloud-killchain
description: AWS/Azure/GCP attack paths.
---

# Cloud Killchain Protocol

## 1. Principles
- **Identity is the Perimeter**: Cloud security is IAM security.
- **Metadata is Key**: VM/Container metadata services often hold credentials (`http://169.254.169.254/`).
- **Misconfigurations > Zero Days**: S3 buckets open to the world, overly permissive roles.

## 2. Techniques
- **SSRF**. Abuse Server-Side Request Forgery to hit the Metadata service.
- **Role Assumption**: Use `sts:AssumeRole` to jump between roles and accounts.
- **User Data**: Check EC2 User Data for hardcoded secrets.
- **Lambda Injection**: Backdoor serverless functions to steal input data.

## 3. Checklist
- [ ] Public buckets enumerated?
- [ ] IAM roles enumerated (Pacu)?
- [ ] Route53/DNS records checked?
- [ ] CloudTrail logging status checked?
