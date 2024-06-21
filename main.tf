terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  shared_config_files      = ["/Users/777/.aws/config"]
  shared_credentials_files = ["/Users/777/.aws/credentials"]
  profile                  = "default"
}

resource "aws_instance" "docker_host" {
  ami           = "ami-080e1f13689e07408"
  instance_type = "t2.micro"
  key_name = "testpem"
  tags = {
    Name = var.instance_name
  }

  vpc_security_group_ids = [
    aws_security_group.app_security_group.id
  ]
  associate_public_ip_address = true
  
  user_data = <<-EOF
              #!/bin/bash
              sudo apt update
              sudo apt install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo usermod -aG docker ubuntu
              IP=$(curl -s ifconfig.me)
              sudo docker pull anddr0/tictactoe-backend:latest
              sudo docker pull anddr0/tictactoe-frontend:latest
              sudo docker run -d -p 80:80 -e SERVER_ADRESS=$IP anddr0/tictactoe-frontend:latest
              sudo docker run -d -p 5000:5000 -e SERVER_ADRESS=$IP anddr0/tictactoe-backend:latest
              $(date)
              EOF
}

