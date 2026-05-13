# Commands Used

## SSH into EC2

```bash
ssh -i devops-3tier-key.pem ubuntu@<EC2_PUBLIC_IP>
```

## Install PostgreSQL Client on EC2

```bash
sudo apt update
sudo apt install postgresql-client -y
```

## Connect EC2 to RDS PostgreSQL

```bash
psql "host=<RDS_ENDPOINT> port=5432 dbname=postgres user=<RDS_USERNAME> sslmode=require"
```

## Create Students Table

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(100),
    course VARCHAR(50)
);
```

## Insert Sample Data

```sql
INSERT INTO students (name, email, course)
VALUES ('Prathyusha', 'prathyusha@example.com', 'AWS DevOps');
```

## View Data

```sql
SELECT * FROM students;
```

## Install Python Dependencies

```bash
sudo apt update
sudo apt install python3-pip -y
python3 -m pip install flask psycopg2-binary --user
```

## Run Flask Application

```bash
export DB_HOST="<RDS_ENDPOINT>"
export DB_NAME="postgres"
export DB_USER="<RDS_USERNAME>"
export DB_PASSWORD="<RDS_PASSWORD>"

python3 app.py
```

## Application URLs

```text
http://<ALB_DNS_NAME>
http://<ALB_DNS_NAME>/students
```
