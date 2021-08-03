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

local = pytz.timezone ("Brazil/East")
utc = pytz.utc

dconfig = pd.read_csv('config.txt',sep="\t", header=None) #Arquivo de Configuracao
opc_server = dconfig.iloc[0,0]  #Servidor OPC
time_scan = dconfig.iloc[1,0]   #Tempo de Scan
endereco = dconfig.iloc[2,0].split(',') #Itens OPC
Tags = dconfig.iloc[3,0].split(',')
description = dconfig.iloc[4,0].split(',')
engunits = dconfig.iloc[5,0].split(',')

data = []
time_past = np.zeros(len(Tags))

opc = OpenOPC.client()               #Conexao OPC
opc.connect(opc_server) #'Matrikon.OPC.Simulation.1'
client.switch_database("Dados") # Nome da base de dados

while True:
    
    valores = opc.read(endereco, group='Group')
    print(valores)
    
    for i in range(len(Tags)):

        try:
            old_time = datetime.datetime.strptime(valores[i][3][:26], "%Y-%m-%d %H:%M:%S.%f")
        except:
            old_time = datetime.datetime.strptime(valores[i][3][:19], "%Y-%m-%d %H:%M:%S")  #Caso faca a leitura até os segundos

        delta_hours = datetime.timedelta(hours=3)
        new_time = old_time - delta_hours             #Timestamp formato InfluxDB
        time_iflx = int(new_time.timestamp()*1000)
        
        if time_past[i] != time_iflx:           #Monto o arquivo caso o TimeStamp seja diferente do TimeStamp anterior

            if type(valores[i][1]) == str:             #Confirmacao com Tags do Tipo String
                valor_atualizado = '"' + valores[i][1] + '"'
            else:
                valor_atualizado = round(valores[i][1],3)

            data.append("{measurement},Tags={contrib},Status={sta} Valor={value} {timestamp}" #Montagem do arquivo padrao
                        .format(measurement=Tags[i],
                        contrib=Tags[i],
                        sta=valores[i][2],
                        value= valor_atualizado,
                        timestamp=time_iflx ))
            time_past[i] = time_iflx            #Atualizacao do TimeStamp


    client.write_points(data,  time_precision = 'ms', database = 'Dados', protocol='line') 
    data = []
    print("Escrita Realizada")
    time.sleep(int(time_scan))

opc.close()