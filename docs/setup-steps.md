# Setup Steps

## 1. VPC

Created a custom VPC:

- Name: devops-3tier-vpc
- CIDR: 10.0.0.0/16

## 2. Subnets

Created 4 subnets:

- public-subnet-1
- public-subnet-2
- private-subnet-1
- private-subnet-2

Public subnets were used for ALB and EC2.

Private subnets were used for RDS.

## 3. Internet Gateway

Created and attached an Internet Gateway to the VPC.

## 4. Route Tables

Created a public route table with:

```text
0.0.0.0/0 -> Internet Gateway

Created a private route table without internet access.

5. Security Groups

Created 3 security groups:

ALB SG: Allows HTTP port 80 from internet
EC2 SG: Allows port 5000 from ALB SG
RDS SG: Allows PostgreSQL port 5432 from EC2 SG
6. EC2

Launched an Ubuntu EC2 instance in the public subnet.

The Flask app runs on EC2 on port 5000.

7. RDS

Created Amazon RDS PostgreSQL in private subnets.

Public access was disabled.

8. EC2 to RDS Connection

Connected from EC2 to RDS using psql.

Created a students table and inserted sample data.

9. Flask App

Created a Flask application.

The app connects to RDS and displays student records.

10. Target Group

Created a target group on port 5000.

Registered EC2 as target.

Target status became healthy.

11. Application Load Balancer

Created an internet-facing ALB.

ALB listens on port 80 and forwards traffic to EC2.

12. Final Output

Tested these URLs:

http://<ALB_DNS_NAME>
http://<ALB_DNS_NAME>/students

The students page successfully showed data from RDS PostgreSQL.
