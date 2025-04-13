variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "aws_access_key" {
    description = "AWS Access Key"
    type        = string
}

variable "aws_secret_key" {
    description = "AWS Access Key"
    type        = string
}

variable "ami_id" {
  description = "AMI ID for EC2"
  default     = "ami-0c94855ba95c71c99" # Example for us-east-1 (Amazon Linux 2)
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "bucket_name" {
  description = "S3 Bucket name"
  type        = string
}
