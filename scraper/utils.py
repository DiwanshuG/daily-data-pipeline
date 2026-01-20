import datetime
import os

def get_today_date():
    return datetime.date.today().isoformat()

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
