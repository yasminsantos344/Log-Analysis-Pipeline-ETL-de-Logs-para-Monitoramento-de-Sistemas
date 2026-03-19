from extract import extract_logs
from transform import data_cleaning
from database import connect, insert_log, update_aggregate_tables, fetch_results
from tabulate import tabulate
from analytics import log_per_minute_query, log_per_status_query, logs_per_endpoint_query, log_per_status_query_delete, logs_per_endpoint_query_delete

data = data_cleaning(extract_logs())
connection = connect()
if connection:
    insert_log(connection, data)

    # Atualiza as tabelas agregadas
    update_aggregate_tables(connection, [log_per_minute_query])
    update_aggregate_tables(connection, [log_per_status_query_delete, log_per_status_query])
    update_aggregate_tables(connection, [logs_per_endpoint_query_delete, logs_per_endpoint_query])

    # Busca os resultados das tabelas
    logs_per_minutes = fetch_results(connection, "SELECT * FROM log_per_minute")
    logs_per_status = fetch_results(connection, "SELECT * FROM log_per_status")
    logs_per_endpoint = fetch_results(connection, "SELECT * FROM logs_per_endpoint")

    connection.close()

print("Logs por minuto:")
print(tabulate(logs_per_minutes, headers=["Date Hours Minutes", "Total Requests", "Total Errors", "Status 200", "Status 500"]))

print("\nLogs por status code:")
print(tabulate(logs_per_status, headers=["Status Code", "Quantity"]))

print("\nLogs por endpoint:")
print(tabulate(logs_per_endpoint, headers=["Endpoint", "Total Requests", "Total Errors"]))