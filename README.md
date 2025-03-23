# Simple System Monitoring

start the server (prometheus + grafana): docker-compose up -d --build

start the client to register the information:
pip install psutil
pip install influxdb
python collector.py
