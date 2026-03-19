import pandas as pd
from datetime import datetime

def data_cleaning(logs):
    cleaned_logs = []
    for log in logs:
        cleaned_log = {
            'ip_adress': log['ip_adress'],
            'client_id': log['client_id'],
            'autenticated_user': log['autenticated_user'],
            'date_time': datetime.strptime(log['date_time'].split(' ')[0], "%d/%b/%Y:%H:%M:%S"),
            'time_zone': log['date_time'].split(' ')[1],  # Extrai o fuso horário
            'method': log['method'],
            'url': log['url'],
            'protocol': log['protocol'],
            'status_code': int(log['status_code']),
            'response_size': int(log['response_size']),
            'referrer': log['referrer'],
            'user_agent': log['user_agent'],
            'other': log['other']
        }
        cleaned_logs.append(cleaned_log)
    cleaned_logs_df = pd.DataFrame(cleaned_logs)
    
    return cleaned_logs_df




