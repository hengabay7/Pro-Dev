resource "aws_route_table" "public" {
  vpc_id = module.vpc.vpc_id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }

  tags = {
    Name = "public-route-table"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = module.vpc.public_subnets[0] 
  route_table_id = aws_route_table.public.id
}

output "route_table_id" {
  value = aws_route_table.public.id
}