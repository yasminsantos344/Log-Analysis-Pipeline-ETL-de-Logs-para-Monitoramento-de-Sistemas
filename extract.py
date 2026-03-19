import re

log_pattern = r'(\S+) (\S+) (\S+) \[([^\]]+)\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+) "([^"]*)" "([^"]*)" "(.*)"'

def extract_logs():
    with open('log.txt') as file:
        data = file.read().splitlines()

    logs = []
    for line in data:
        match = re.match(log_pattern, line)
        if match:
            logs.append({
                'ip_adress': match.group(1),
                'client_id': match.group(2),
                'autenticated_user': match.group(3),
                'date_time': match.group(4),
                'method': match.group(5),
                'url': match.group(6),
                'protocol': match.group(7),
                'status_code': match.group(8),
                'response_size': match.group(9),
                'referrer': match.group(10),
                'user_agent': match.group(11),
                'other': match.group(12)
            })
    return logs
