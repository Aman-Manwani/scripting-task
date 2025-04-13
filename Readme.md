# AWS Automation Scripts – NatWest Group

## 👋 Introduction

Hi, I'm **Aman Manwani**, a DevOps and Cloud enthusiast with hands-on experience in automating cloud infrastructure and scripting operational workflows using AWS tools like Terraform and Python. This repository contains scripts I built for the **NatWest Group** to streamline AWS operations like EC2 provisioning, S3 website hosting, and monitoring S3 bucket contents programmatically.

---

## 📁 Repository Overview

This repo includes:

- ✅ Terraform scripts to automate EC2 instance and S3 bucket provisioning
- 🐍 A Python script to list all S3 buckets and count objects in a specific bucket
- ⚙️ Integration setup to trigger AWS Lambda from S3 events

---

## 🚀 Terraform Modules

The Terraform configuration handles:

- EC2 instance creation with custom key pair and security group
- Public S3 bucket for static website hosting
- IAM roles and policies for Lambda
- S3 event trigger to deploy/update Lambda on file changes

> Variables like instance type, region, key name, and bucket name are parameterized for flexibility and reuse.

---

## 🐍 Python Script – S3 Inspector

A beginner-friendly Python script using `boto3` to:

1. **List all S3 buckets** in your AWS account
2. **Count the total number of objects** in a specified bucket

### Usage:

```bash
python listBuckets.py
