import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kanya#005",
        database="library_management",
        auth_plugin="mysql_native_password"
    )
    print("Connected successfully")
    conn.close()
except Exception as e:
    print("Error:", e)