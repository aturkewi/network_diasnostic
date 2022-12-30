import subprocess
import csv
import time
from datetime import datetime

def file_name():
  return 'network_log.csv'

def get_raw_ping_data():
  output = subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
  return output.decode()

def get_time_string(raw_ping_string):
  key = 'time='
  start = raw_ping_string.find('time=')
  start = start + len(key)
  end = start + 6
  return raw_ping_string[start:end]

def write_to_file(time):
  with open(file_name(), 'a') as file:
    writer = csv.writer(file)
    writer.writerow([datetime.now().isoformat(), time])

def ensure_file():
  with open(file_name(), 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "ping"])


def run():
  ensure_file()

  while True:
    raw_ping_string = get_raw_ping_data()
    ping = get_time_string(raw_ping_string)
    write_to_file(ping)
    time.sleep(1)

run()
