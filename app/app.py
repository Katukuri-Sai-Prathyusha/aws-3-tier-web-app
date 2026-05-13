from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>AWS 3-Tier Web Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                padding: 40px;
            }
            .card {
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                width: 70%;
            }
            h1 {
                color: #232f3e;
            }
            p {
                font-size: 18px;
            }
            a {
                color: #0073bb;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AWS 3-Tier Web Application</h1>
            <p>Application is running successfully behind an Application Load Balancer.</p>
            <p><a href="/students">View Student Records from RDS</a></p>
        </div>
    </body>
    </html>
    """

@app.route("/students")
def students():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            sslmode="require"
        )

        cur = conn.cursor()
        cur.execute("SELECT id, name, email, course FROM students;")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        html = """
        <html>
        <head>
            <title>Student Records</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f6f8;
                    padding: 40px;
                }
                h1 {
                    color: #232f3e;
                }
                table {
                    border-collapse: collapse;
                    width: 80%;
                    background-color: white;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                }
                th, td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: left;
                }
                th {
                    background-color: #232f3e;
                    color: white;
                }
                tr:nth-child(even) {
                    background-color: #f9f9f9;
                }
                .success {
                    color: green;
                    font-weight: bold;
                }
                a {
                    color: #0073bb;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <h1>AWS 3-Tier Web Application</h1>
            <p class="success">Data successfully fetched from Amazon RDS PostgreSQL</p>

            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Course</th>
                </tr>
        """

        for row in rows:
            html += f"""
                <tr>
                    <td>{row[0]}</td>
                    <td>{row[1]}</td>
                    <td>{row[2]}</td>
                    <td>{row[3]}</td>
                </tr>
            """

        html += """
            </table>
            <br>
            <a href="/">Back to Home</a>
        </body>
        </html>
        """

        return html

    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
