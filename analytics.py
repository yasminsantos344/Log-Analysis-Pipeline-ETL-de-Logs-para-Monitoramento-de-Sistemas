log_per_minute_query = """
INSERT INTO log_per_minute
SELECT DATE_FORMAT(date_time, '%H:%i:00') as date_hours_minutes,
        COUNT(log_id) as total_req, 
        COUNT(CASE WHEN status_code BETWEEN 400 AND 599 THEN 1 END) as total_error,
        COUNT(CASE WHEN status_code BETWEEN 200 AND 299 THEN 1 END) as status_200,
        COUNT(CASE WHEN status_code BETWEEN 500 AND 599 THEN 1 END) as status_500
FROM tb_log
GROUP BY date_hours_minutes
"""

log_per_status_query_delete = "DELETE FROM log_per_status"
log_per_status_query = """
INSERT INTO log_per_status
SELECT status_code, COUNT(*) as quantity
FROM tb_log
GROUP BY status_code
"""

logs_per_endpoint_query_delete = "DELETE FROM logs_per_endpoint"
logs_per_endpoint_query = """
INSERT INTO logs_per_endpoint
SELECT url as endpoint, 
        COUNT(log_id) as total_requests,
        COUNT(CASE WHEN status_code BETWEEN 400 AND 599 THEN 1 END) as total_errors
FROM tb_log
GROUP BY endpoint
"""