# Simple System Monitoring

This repo is running on my raspberry pi 4 for monitoring the entire system (memory, cpu, disk usage, ecc...)

## Usage

start the server (prometheus + grafana): ```docker-compose up -d --build```

start the client to register the information (installa package in venv):

```
python3 -m venv myenv

source myenv/bin/activate

pip install influxdb

pip install psutil

python collector.py

# OR to run in background
nohup python collector.py >/dev/null 2>&1 &

# to verify that the script is runnign ps ax | grep *.py
```


navigate to http://localhost:7974/ and configure grafana using influxdb as data source (the url to set in grafana is ```http://simplesystemmonitoring-influxdb:8086``` and the credentials are in the docker-compose). 

Then you can setup you own dashboard
