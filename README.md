# Open PIMS para a Indústria 4.0

O objetivo é difundir o Desenvolvimento de uma Aplicação de Gerenciamento de Informações da Planta (PIMS) para Indústria 4.0, em que ocorre a coleta de dados operacionais, a escrita desses dados em um banco de dados temporal, em que o utilizado foi o InfluxDB, a leitura desses dados através de uma planilha padrão no excel e a criação de painéis de observação no Grafana. O sistema criado possui licença livre, o que torna-o acessível para ser implementado em empresas menores e laboratórios de universidades.

Dentre as principais vantagens da aplicação proposta destaca-se a facilidade de execução e a possibilidade de adaptação dos procedimentos, é possível por exemplo, realizar a construção de diferentes painéis de observação, extrair os dados industriais para análises mais robustas, além de outras funcionalidades de gerenciamento que proporcionam um aumento do conhecimento acerca de toda a cadeia de produção do negócio, apresentando um maior acompanhamento da linha de produção e uma maior segurança em plantas industriais. Ainda, a solução permite concentrar em um só lugar os dados originados de todos os dispositivos e equipamentos, sendo um item importante para a Indústria 4.0, afinal é necessário recolher e obter informações dessa grande quantidade de dados que é gerada pelas novas tecnologias.

De uma forma geral conclui-se que os resultados pretendidos neste trabalho foram alcançados, pois o sistema apresentado possibilita
melhorias em toda a organização, uma vez que a adoção de uma infraestrutura de dados é a base para a inovação de novas tecnologias, o que revoluciona a forma em que os processos operam.

## Etapas de Execução

Antes da execução do sistema, instale os seguintes programas:
- Versão 32 bits do Python;
- Interface automática para OPC DA. Link: [OPC DA Interface](http://gray-box.net/download_daawrapper.php?lang=en)
- Inicie o _prompt do _Windows_ como administrador, acesse o diretório _'x86'_ da pasta instalada e execute o comando _regsvr32 gbda\_aut.dll_.
- Instale a biblioteca _pywin32_ que é disponibilizada em [PyWin32](https://github.com/mhammond/pywin32/releases/), de acordo com a licença do Python instalada.

Com as configurações realizadas, basta realizar os procedimentos abaixo:
1. Preencher o arquivo _config.txt_ com as informações necessárias como estão abaixo:

Itens necessários | config.txt
--------- | ------:
Servidor OPC | Matrikon.OPC.Simulation.1  		                          
Perído de atualização em segundos | 10                        
Endereço OPC | Bucket Brigade.Real4,Bucket Brigade.String
Tags | Caminhao1_MinerioSP,Caminhao1_MotoristaID          
Descrição das Tags | Qtde. Minerio SP,Motorista do Caminhao 1          
Unidade de Engenharia das Tags | ton,-

2. Iniciar a aplicação InfluxDB e criar os _Databases Definicoes_ e _Dados_ através do comando _CREATE DATABASE_;
3. Executar a aplicação _definicoes.py_, responsável pela escrita das informações relevantes das _Tags_ no _Database Definicoes_;
4. Iniciar o _MatrikonOPC Explorer_, conectar ao servidor, criar um grupo com a taxa de atualização desejada e inserir os endereços OPC disponíveis no servidor;
5. Executar a aplicação _opc.py_, responsável pela escrita dos valores coletados no servidor no _Database Dados_;
6. Iniciar o _Grafana_, configurando a aplicação e criando os _dashboards_.
7. Utilizar a planilha padrão _extract.xlsm_, para exportar cálculos e valores para o _Microsoft Excel_.
