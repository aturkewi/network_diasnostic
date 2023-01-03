import subprocess
import csv
import time
from datetime import datetime

def get_file_name():
  timestamp = datetime.now().isoformat().split('.')[0]
  return f"network_log_{timestamp}.csv"

def get_raw_ping_data():
  output = subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
  return output.decode()

def get_time_string(raw_ping_string):
  key = 'time='
  start = raw_ping_string.find('time=')
  start = start + len(key)
  end = start + 6
  return raw_ping_string[start:end]

def write_to_file(time, file_name):
  with open(file_name, 'a') as file:
    writer = csv.writer(file)
    writer.writerow([datetime.now().isoformat(), time])

def ensure_file(file_name):
  with open(file_name, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "ping"])


def run():
  file_name = get_file_name()
  ensure_file(file_name)

  while True:
    raw_ping_string = get_raw_ping_data()
    ping = get_time_string(raw_ping_string)
    write_to_file(ping, file_name)
    time.sleep(1)

run()
