az webapp up -n projectName &&\
az webapp log tail &&\
pyhton3 -m venv ~/.venv &&\
source ~/.venv/bin/activate

