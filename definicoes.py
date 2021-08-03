import pywintypes # Evita timeout error
import OpenOPC
import time
import pandas as pd
import numpy as np
from influxdb import InfluxDBClient
import datetime
import time
import os
import pytz

pywintypes.datetime = pywintypes.TimeType

client = InfluxDBClient(host="localhost", port=8086, username = 'admin', password='admin')

dconfig = pd.read_csv('config.txt',sep="\t", header=None) #Arquivo de Configuracao
opc_server = dconfig.iloc[0,0]  #Servidor OPC
time_scan = dconfig.iloc[1,0]   #Tempo de Scan
endereco = dconfig.iloc[2,0].split(',') #Itens OPC
Tags = dconfig.iloc[3,0].split(',')
description = dconfig.iloc[4,0].split(',')
engunits = dconfig.iloc[5,0].split(',')

now = datetime.datetime.now()   #Hora atual

client.switch_database("Definicoes") # USE DATABASE

for i in range(len(Tags)):
    
    json_body = [{
        "measurement": Tags[i], 
        "tags":{"Tags":Tags[i]},
        "fields":{                #Campos
        "Item OPC": endereco[i],
        "Descricao": description[i],
        "Unid.Eng": engunits[i],
        },
        "time": now
    }]
    client.write_points(json_body)
print("Escrita Realizada Def")