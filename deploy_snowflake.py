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
with open('snowflake/sql/init.sql', 'r') as f:
    sql = f.read()
    for statement in sql.split(';'):
        stmt = statement.strip()
        if stmt and not stmt.startswith('--'):
            cursor.execute(stmt)
cursor.execute('SELECT CURRENT_DATABASE(), CURRENT_SCHEMA()')
print(cursor.fetchone())
cursor.close()
conn.close()
