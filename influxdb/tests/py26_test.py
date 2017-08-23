#!/usr/bin/python

import sys
import os
import datetime
import requests

from influxdb import InfluxDBClient

# InfluxDB Server parameters
influxdb_server = 'localhost'
port = 8086
database_name = 'test_db'
ip_addr = os.popen('hostname').read()

# InfluxDB connection and database creation if it doesn't exists
client = InfluxDBClient(influxdb_server, port, 'influx-user', 'influx-pass')

try:
    client.create_database(database_name)
except requests.ConnectionError as e:
    print 'Failed to start, unable to establish connection with InfluxDB server %s - %s' % (influxdb_server, e)
    sys.exit(2)

# System Load
load_avg_1 = os.popen("cat /proc/loadavg|awk '{print $1,$2,$3}'").read()[0]
load_avg_5 = os.popen("cat /proc/loadavg|awk '{print $1,$2,$3}'").read()[1]
load_avg_15 = os.popen("cat /proc/loadavg|awk '{print $1,$2,$3}'").read()[2]

while True:
    load_1 = [
        {"measurement": 'Load_1_minute',
        "tags": {"hosts": ip_addr},
                    "time": datetime.datetime.now(), "fields": {"load_avg_1": int(load_avg_1)}}]
    client.write_points(load_1)

    load_5 = [
        {"measurement": 'Load_5_minutes',
        "tags": {"hosts": ip_addr},
        "time": datetime.datetime.now(), "fields": {"load_avg_5": int(load_avg_5)}}]
    client.write_points(load_5)

    load_15 = [
        {"measurement": 'Load_1_minute',
        "tags": {"hosts": ip_addr},
        "time": datetime.datetime.now(), "fields": {"load_avg_15": int(load_avg_15)}}]
    client.write_points(load_15)
