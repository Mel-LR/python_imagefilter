from datetime import datetime
log_file = "imagefilter.log"

def log(msg):
    now = datetime.now()
    timestamp = now.strftime('%Y/%m/%d %H:%M:%S')
    formatted = f'{timestamp} - {msg}'
    with open(log_file, 'a') as f:
        f.write(formatted + '\n')

