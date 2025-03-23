#!/usr/bin/env python

import datetime, time
import psutil
import socket
from influxdb import InfluxDBClient

# influx configuration - edit these
ifuser = "ssc"
ifpass = "password"
ifdb   = "simplesystemmonitoring"
ifhost = "localhost"
ifport = 7975

# connect to influx
ifclient = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)

while True:
    print("Inizio recupero dati e scrittura su influxdb")
    # configure network device name and disk path
    net = ('eth0')
    drive =('/')

    #get hostname and take a timestamp for this measurement
    hostname = socket.gethostname()
    time_now = datetime.datetime.utcnow()

    # collect some stats from psutil
    cpu = psutil.cpu_percent(interval=1)
    disk = psutil.disk_usage(drive)
    mem = psutil.virtual_memory()
    load = psutil.getloadavg()

    # format the data as a single measurement for influx
    data = [
        {
            "measurement": hostname,
            "time": time_now,
            "fields": {
                "cpu": cpu,
                "load_1": load[0],
                "load_5": load[1],
                "load_15": load[2],
                "disk_percent": disk.percent,
                "disk_free": disk.free,
                "disk_used": disk.used,
                "mem_percent": mem.percent,
                "mem_free": mem.free,
                "mem_used": mem.used
            }
        }
    ]

    # write the measurement
    ifclient.write_points(data)
    time.sleep(15)
