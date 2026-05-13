# Troubleshooting Notes

## Issue 1: RDS connection was hanging

### Problem

The `psql` command was just blinking and not connecting.

### Checks performed

- Confirmed the command was running from EC2, not laptop
- Checked RDS status was Available
- Checked EC2 and RDS were in the same VPC
- Checked RDS security group allowed PostgreSQL port 5432 from EC2 security group
- Tested RDS connectivity from EC2

### Learning

For private RDS, connection should happen from EC2 inside the VPC, not directly from laptop.

---

## Issue 2: PostgreSQL password authentication failed

### Problem

RDS was reachable, but login failed because the wrong username was used.

### Error

```text
FATAL: password authentication failed for user

Fix

Checked the actual master username in RDS Configuration and connected using the correct username.

Learning

RDS endpoint can be correct, but login still fails if username or password is wrong.

Issue 3: Flask module not found
Problem

The Flask app failed with:

ModuleNotFoundError: No module named 'flask'
Fix

Installed Flask and PostgreSQL driver using pip:

python3 -m pip install flask psycopg2-binary --user
Learning

Python dependencies must be installed before running the application.

Issue 4: Flask app file error
Problem

The application failed with:

NameError: name 'app' is not defined
Cause

Only the /students function was saved in app.py, and the full Flask application structure was missing.

Fix

Replaced app.py with the full Flask application code.

Learning

A Flask app needs imports, app initialization, routes, and run configuration.



