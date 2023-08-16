variable "az" {}
variable "subnet" {}
variable "vpc" {}
variable "stack_name" {}
variable "key_name" {}
variable "ami_ssm_parameter" {}
variable "startup_script" {
    default = <<-EOF
    #!/bin/bash
    sudo echo "start up"> /start.txt
EOF
}