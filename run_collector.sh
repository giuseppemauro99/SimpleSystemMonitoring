#!/bin/bash
cd /home/giusepperasp/SimpleSystemMonitoring #PathToTheGitRepository

# Crea l'ambiente virtuale se non esiste già
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

# Attiva l'ambiente virtuale e avvia lo script
source myenv/bin/activate
exec python collector.py
