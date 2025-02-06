# tomorrowio-data-weather-etl-aws

### Introdução

Este é um projeto de ETL usando API do Tomorrow.io para coletar dados meteorológicos e usará as ferramentas de nuvem da AWS para execução de uma pipeline real time e outra em batch. Na pipeline real time os dados coletados deverão enviar SMS e um e-mail caso informações pré-estabelecidas representem um alerta metereológico. Já na pipeline batch os mesmos dados coletados serão armazenados para consulta quando necessário. 

### Sobre o Tomorrow.io/API

O Tomorrow.io Free API fornece aos desenvolvedores acesso flexível a dados meteorológicos, garantindo ao mesmo tempo um uso justo. O plano gratuíto permite aos usuários um número grande de solicitações de API, segmentadas em limites diários, horários e por segundo. Discriminação dos limites de taxa: 500 solicitações por dia. Maiores informações em [Tomorrow.io API](https://docs.tomorrow.io/reference/welcome).
