resource "aws_internet_gateway" "igw" {
  vpc_id = module.vpc.vpc_id

  tags = {
    Name = "example-igw"
  }
}

output "internet_gateway_id" {
  value = aws_internet_gateway.igw.id
}