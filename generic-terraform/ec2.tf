data "aws_vpc" "vpc" {
    id = var.vpc
}
data "aws_subnet" "subnet" {
  id = var.subnet
}

#################### SECUIRITY GROUPS #############################
resource "aws_security_group" "generic-sg" {
  name        = "${var.stack_name}"
  description = "generic sg group"
  vpc_id      = data.aws_vpc.vpc.id

  ingress {
    description = "allow ssh from my ip"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["46.204.108.97/32"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

}



#################### ROLES #############################


#################### INSTANCES #############################

module "generic-ec2" {
    source = "git@github.com:terraform-aws-modules/terraform-aws-ec2-instance.git"
    ami_ssm_parameter = var.ami_ssm_parameter
    name = "${var.stack_name}"
    associate_public_ip_address = true
    availability_zone = var.az
    subnet_id = data.aws_subnet.subnet.id
    key_name = var.key_name
    vpc_security_group_ids = [aws_security_group.generic-sg.id]
    user_data = var.startup_script
}

  


