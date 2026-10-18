# AWS CI/CD Platform

## 🌐 Project Overview

This project demonstrates how to build an automated **Continuous Integration and Continuous Deployment (CI/CD) pipeline** to test and deploy a Python Flask application to AWS Lambda using GitHub Actions.

The pipeline automatically runs application tests, authenticates with AWS using **OpenID Connect (OIDC)**, deploys updated code to Lambda, and verifies the live application using automated smoke tests. Amazon CloudWatch is used to monitor execution logs, metrics, and Lambda errors.

## 🏗️ Architecture Details

- **Source Code Repository**:
  - GitHub repository: `aws-cicd-platform`
  - Stores the Flask application, tests, and CI/CD workflow files.

- **CI/CD Pipeline**:
  - GitHub Actions
  - CI workflow: `.github/workflows/ci.yml`
  - Deployment workflow: `.github/workflows/deploy-lambda.yml`

- **AWS Authentication**:
  - AWS IAM deployment role: `GitHubActionsDeployRole`
  - Identity provider: GitHub Actions OIDC
  - Uses temporary AWS credentials instead of long-lived access keys stored in GitHub.

- **Application**:
  - AWS Lambda function: `aws-cicd-platform-app`
  - Python Flask application
  - Lambda Function URL for HTTP access.

- **Monitoring**:
  - Amazon CloudWatch Logs
  - AWS Lambda invocation and error metrics
  - CloudWatch alarm: `aws-cicd-platform-lambda-errors`

## 🛠️ Configuration Steps Taken

1. **Application Development**:
   - Created a Python Flask application with a home endpoint and a health-check endpoint.
   - Added `pytest` tests to validate application behavior.
   - Configured the application for execution through AWS Lambda.

2. **GitHub Repository Setup**:
   - Stored the application source code and configuration files in GitHub.
   - Created GitHub Actions workflows for automated testing and deployment.
   - Configured repository variables for the AWS deployment role ARN, AWS Region, and Lambda Function URL.

3. **Continuous Integration (CI)**:
   - Configured GitHub Actions to run when code is pushed or a pull request targets the `main` branch.
   - Installed Python dependencies.
   - Executed automated tests using `pytest`.

4. **Secure AWS Authentication Using OIDC**:
   - Configured GitHub Actions as an OpenID Connect identity provider in AWS IAM.
   - Created the `GitHubActionsDeployRole` IAM role with a repository-specific trust policy.
   - Configured deployment permissions for the required Lambda operations.

5. **Continuous Deployment (CD)**:
   - Configured the deployment workflow to run on pushes to `main`.
   - Packaged the Flask application and its dependencies into a deployment ZIP file.
   - Authenticated with AWS through OIDC.
   - Updated the code of the `aws-cicd-platform-app` Lambda function.

6. **Post-Deployment Verification**:
   - Added automated smoke tests to check the home endpoint.
   - Verified the `/health` endpoint returns a healthy status.
   - Configured the workflow to fail if the live endpoint checks do not pass.

7. **Monitoring and Error Detection**:
   - Used CloudWatch Logs to inspect Lambda execution details.
   - Reviewed Lambda invocation and error metrics.
   - Created a CloudWatch alarm to detect when the Lambda Errors metric reaches one or more errors within a five-minute period.

## ✅ Verification & Results

- Successfully executed the GitHub Actions CI workflow.
- Successfully deployed the Flask application to AWS Lambda through GitHub Actions.
- Verified the home endpoint returns the expected application greeting.
- Verified the `/health` endpoint returns a healthy status.
- Confirmed that post-deployment smoke tests passed.
- Inspected Lambda execution logs and monitoring metrics in Amazon CloudWatch.
- Configured a CloudWatch alarm for Lambda execution errors.

## 🔐 Security Considerations

- Used GitHub Actions OIDC to obtain temporary AWS credentials rather than storing long-lived AWS access keys in GitHub.
- Restricted AWS deployment permissions through an IAM role and trust policy.
- Kept application configuration separate from sensitive credentials.
- Reviewed AWS IAM permissions and monitored potential service costs.
- The Lambda Function URL is currently configured for public access and is intended for this demonstration. Public endpoints should be protected appropriately before handling sensitive data or production traffic.

## 📚 Technologies Used

- Amazon Web Services (AWS)
- AWS Lambda
- AWS IAM
- OpenID Connect (OIDC)
- Amazon CloudWatch
- Git and GitHub
- GitHub Actions
- Python
- Flask
- pytest
- Docker

## 🚀 Key Learnings

- Understanding CI/CD concepts and automation.
- Integrating GitHub Actions with AWS.
- Configuring secure, federated authentication using OIDC.
- Deploying Python applications to AWS Lambda.
- Writing automated tests and post-deployment smoke tests.
- Monitoring serverless applications using CloudWatch logs and metrics.
- Configuring CloudWatch alarms for error detection.

## 🔮 Future Improvements

- Configure Amazon SNS notifications for CloudWatch alarm state changes.
- Use Lambda versions and aliases for safer deployments and rollback.
- Automate AWS infrastructure provisioning using Terraform.
- Add container build validation to the CI pipeline.
- Improve deployment validation and security testing.
- Add a documented architecture diagram and screenshots of successful workflow runs and AWS monitoring.


