from flask import Flask, render_template, request, jsonify
import psycopg2
import subprocess
import os

app = Flask(__name__)

# Database configuration
SUPERUSER = "ubuntu"

@app.route('/')
def index():
    return render_template('index.html')

# Option 2
@app.route('/createdb', methods=['POST'])
def create_db():
    db_name = request.form['db_name']
    username = request.form['username']
    password = request.form['password']
    mount_point = request.form['mount_point']
    pg_bin = request.form['pg_bin']
    port = request.form['port']

    try:
        # Step 1: Initialize the database using the specified mount point and binary
        initdb_command = f"{pg_bin}/initdb -D {mount_point}/{db_name}"
        subprocess.run(initdb_command, shell=True, check=True)

        # Step 2: Create a port.conf file with the specified port
        port_conf_path = os.path.join(mount_point, db_name, 'port.conf')
        with open(port_conf_path, 'w') as port_file:
            port_file.write(f"port = {port}\n")

        # Step 3: Include port.conf in the postgresql.conf file
        postgresql_conf_path = os.path.join(mount_point, db_name, 'postgresql.conf')
        with open(postgresql_conf_path, 'a') as conf_file:
            conf_file.write(f"include = '{port_conf_path}'\n")
            # Add listen addresses
            conf_file.write("listen_addresses = '*'\n")

        # Step 4: Modify pg_hba.conf to add the trust entry before starting the server
        pg_hba_conf_path = os.path.join(mount_point, db_name, 'pg_hba.conf')
        with open(pg_hba_conf_path, 'a') as hba_file:
            hba_file.write(f"host    {db_name}    {username}    0.0.0.0/0    scram-sha-256\n")

        # Step 5: Start the PostgreSQL server with the new configuration
        pg_ctl_command = f"{pg_bin}/pg_ctl -D {mount_point}/{db_name} start"
        subprocess.run(pg_ctl_command, shell=True, check=True)

        # Step 6: Connect to the PostgreSQL server and create the database and user
        conn = psycopg2.connect(host="localhost", port=port, user=SUPERUSER, database='postgres')
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f'CREATE DATABASE "{db_name}";')
        cur.execute(f"CREATE USER {username} WITH PASSWORD '{password}';")
        cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE \"{db_name}\" TO {username};")

        cur.close()
        conn.close()

        return jsonify({"status": f"Database {db_name} created successfully on port {port} with user {username}"}), 200
    except Exception as e:
        # Log the error message
        error_message = str(e)
        return jsonify({"error": error_message}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
