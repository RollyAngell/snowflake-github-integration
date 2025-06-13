import snowflake.connector
import os

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
with open('snowflake/sql/init.sql', 'r') as f:
    sql = f.read()
    print("SQL to execute:")
    print(sql)
    for statement in sql.split(';'):
        stmt = statement.strip()
        if stmt and not stmt.startswith('--'):
            print(f"Executing: {stmt[:60]}...")
            try:
                cursor.execute(stmt)
            except Exception as e:
                print(f"Error executing: {stmt[:60]}...\n{e}")
cursor.execute('SELECT CURRENT_DATABASE(), CURRENT_SCHEMA()')
print(cursor.fetchone())
cursor.close()
conn.close()
