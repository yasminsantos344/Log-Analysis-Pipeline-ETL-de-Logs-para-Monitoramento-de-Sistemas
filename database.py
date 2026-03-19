import mysql.connector
from config import DATABASE_CONFIG

def connect():
    try:
        connection = mysql.connector.connect(
            host=DATABASE_CONFIG['host'],
            port=DATABASE_CONFIG['port'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            database=DATABASE_CONFIG['database']
        )

        return connection
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert_log(connection, cleaned_logs_df):
    cursor = connection.cursor()
    insert_query = """
        INSERT INTO tb_log (ip_adress, client_id, autenticated_user, date_time, time_zone, method, url, protocol, status_code, response_size, referrer, user_agent, other)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    # Use executemany para inserir múltiplas linhas
    cursor.executemany(insert_query, cleaned_logs_df.values.tolist())
    connection.commit()
    row_count = cursor.rowcount
    cursor.close()
     
    if row_count > 0:
        print(f"{row_count} logs inserted successfully.")
    else:
        print("Failed to insert logs.")

def update_aggregate_tables(connection, queries):
    cursor = connection.cursor()
    for query in queries:
        cursor.execute(query)  # Use execute para consultas únicas
    connection.commit()
    cursor.close()

def fetch_results(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results

