CREATE DATABASE data_log;

use data_log;

CREATE TABLE tb_log(
log_id int(7) auto_increment primary key,
ip_adress varchar(20) not null,
client_id varchar(30),
autenticated_user varchar(10),
date_time datetime not null not null,
time_zone char(5) not null,
method varchar(10) not null,
url varchar(300) not null,
protocol varchar(10) not null,
status_code int(3) not null,
response_size int(6),
referrer varchar(150),
user_agent varchar(300),
other varchar(100)
);

SELECT * FROM tb_log;


-- log by minute
CREATE TABLE log_per_minute
SELECT DATE_FORMAT(date_time, '%H:%i:00') as date_hours_minutes,
        COUNT(log_id) as total_req, 
        COUNT(CASE WHEN status_code BETWEEN 400 AND 599 THEN 1 END) as total_error,
        COUNT(CASE WHEN status_code BETWEEN 200 AND 299 THEN 1 END) as status_200,
        COUNT(CASE WHEN status_code BETWEEN 500 AND 599 THEN 1 END) as status_500
FROM tb_log
GROUP BY date_hours_minutes;

SELECT * FROM log_per_minute;

-- log by status
CREATE TABLE log_per_status
SELECT status_code, COUNT(*) as quantity
FROM tb_log
GROUP BY status_code;

SELECT * FROM log_per_status;
        
-- log by endpoint
CREATE TABLE logs_per_endpoint
SELECT url as endpoint, 
        COUNT(log_id) as total_requests,
        COUNT(CASE WHEN status_code BETWEEN 400 AND 599 THEN 1 END) as total_errors
FROM tb_log
GROUP BY endpoint;

SELECT * FROM logs_per_endpoint;

