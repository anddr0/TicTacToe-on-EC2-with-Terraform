# Learn Terraform AWS Instance

This repository contains Terraform configurations and an example project for deploying an AWS instance along with a simple Tic-Tac-Toe application to demonstrate basic infrastructure provisioning using Terraform and Docker.

## Project Overview

The repository is divided into two main sections:

1. **Terraform AWS Instance**: Contains Terraform scripts for provisioning AWS infrastructure.
2. **Tic Tac Toe**: A simple application demonstrating a Dockerized setup with a backend and frontend.

## Repository Structure

- **Terraform Configuration Files**
  - `main.tf`: Main Terraform configuration file that defines the AWS infrastructure.
  - `variables.tf`: Contains variable declarations used in the Terraform scripts.
  - `outputs.tf`: Specifies the output values from the Terraform configuration.
  - `security.tf`: Contains security group configurations for AWS resources.
  - `vpc.tf`: Defines the Virtual Private Cloud (VPC) settings.
  - `.terraform.lock.hcl`: Ensures consistent Terraform provider versions.
  - `terraform.tfstate` and `terraform.tfstate.backup`: Track the state of the Terraform-managed infrastructure.
  - `testpem.pem`: A PEM file for secure communication (e.g., SSH key).

- **Tic Tac Toe Application**
  - **Backend**
    - `tic tac toe/backend/Dockerfile`: Dockerfile for the backend service.
    - `tic tac toe/backend/requirements.txt`: Python dependencies for the backend.
    - `tic tac toe/backend/server.py`: Python script for the backend server.
  - **Frontend**
    - `tic tac toe/frontend/Dockerfile`: Dockerfile for the frontend service.
    - `tic tac toe/frontend/app.js`: JavaScript file for frontend logic.
    - `tic tac toe/frontend/index.html`: HTML file for the frontend.
    - `tic tac toe/frontend/style.css`: CSS file for frontend styling.
  - `tic tac toe/docker-compose.yml`: Docker Compose file to orchestrate the frontend and backend services.

## How to Run the Project

### Prerequisites

- [Terraform](https://www.terraform.io/downloads.html) installed
- [Docker](https://www.docker.com/get-started) installed
- AWS account with appropriate permissions for provisioning resources

### Setting Up the AWS Instance

1. **Initialize Terraform**:
    ```bash
    cd learn-terraform-aws-instance
    terraform init
    ```

2. **Plan the Infrastructure**:
    ```bash
    terraform plan
    ```

3. **Apply the Configuration**:
    ```bash
    terraform apply
    ```

    Confirm the action when prompted.

4. **Access AWS Resources**:
    Use the output values from Terraform to access your AWS resources. For example, the public IP of the EC2 instance can be used to SSH into the server.

5. **Access the Application**:
    Open a web browser and navigate to `http://localhost:3000` to access the Tic Tac Toe game.

## Notes

- Ensure your AWS credentials are properly configured on your local machine for Terraform to interact with your AWS account.
- Use the provided PEM file for secure communication if necessary.
- The Tic Tac Toe application is a simple example and may need further enhancements for production use.

