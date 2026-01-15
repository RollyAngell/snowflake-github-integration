import snowflake.connector
import os
import re

conn = snowflake.connector.connect(
    user=os.environ['SNOWFLAKE_USER'],
    password=os.environ['SNOWFLAKE_PASSWORD'],
    account=os.environ['SNOWFLAKE_ACCOUNT'],
    warehouse=os.environ['SNOWFLAKE_WAREHOUSE'],
    database=os.environ['SNOWFLAKE_DATABASE'],
    role=os.environ['SNOWFLAKE_ROLE']
)
cursor = conn.cursor()
print("Connected to:", os.environ['SNOWFLAKE_DATABASE'])

# Explicitly use the database
try:
    cursor.execute(f"USE DATABASE {os.environ['SNOWFLAKE_DATABASE']}")
    print(f"Successfully set database context to: {os.environ['SNOWFLAKE_DATABASE']}")
except Exception as e:
    print(f"Error setting database context: {e}")
    # Continue anyway, as the connection parameter might have worked

with open('snowflake/sql/init.sql', 'r') as f:
    sql = f.read()
    print("SQL to execute:")
    print(sql)
    sql_no_comments = re.sub(r'--.*', '', sql)
    statements = sql_no_comments.split(';')
    print(f"Found {len(statements)} statements.")
    for i, statement in enumerate(statements):
        stmt = statement.strip()
        print(f"Statement {i+1}: {repr(stmt)}")
        if stmt:
            print(f"Executing: {stmt[:60]}...")
            try:
                cursor.execute(stmt)
                print("Success.")
            except Exception as e:
                print(f"Error executing: {stmt[:60]}...\n{e}")
cursor.execute('SELECT CURRENT_DATABASE(), CURRENT_SCHEMA()')
print(cursor.fetchone())
with open('snowflake/sql/load_customers_data.sql', 'r') as f:
    sql = f.read()
    print("SQL to execute (data load):")
    print(sql)
    sql_no_comments = re.sub(r'--.*', '', sql)
    statements = sql_no_comments.split(';')
    print(f"Found {len(statements)} statements.")
    for i, statement in enumerate(statements):
        stmt = statement.strip()
        print(f"Statement {i+1}: {repr(stmt)}")
        if stmt:
            print(f"Executing: {stmt[:60]}...")
            try:
                cursor.execute(stmt)
                print("Success.")
            except Exception as e:
                print(f"Error executing: {stmt[:60]}...\n{e}")
cursor.close()
conn.close()
