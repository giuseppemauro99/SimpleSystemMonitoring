# Simple System Monitoring

start the server (prometheus + grafana): docker-compose up -d --build

start the client to register the information (installa package in venv):

```
python3 -m venv myenv

source myenv/bin/activate

pip install influxdb

pip install psutil

python collector.py
```


navigate to http://localhost:7974/ and configure grafana using the influxdb credentials in the docker-compose
