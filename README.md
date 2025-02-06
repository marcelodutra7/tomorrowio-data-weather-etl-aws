# tomorrowio-data-weather-etl-aws

### Introdução

Este é um projeto de ETL usando API do Tomorrow.io para coletar dados meteorológicos e usará as ferramentas de nuvem da AWS para execução de uma pipeline real time e outra em batch. Na pipeline real time os dados coletados deverão enviar SMS e um e-mail caso informações pré-estabelecidas representem um alerta metereológico. Já na pipeline batch os mesmos dados coletados serão armazenados para consulta quando necessário. 

### Sobre o Tomorrow.io/API

O Tomorrow.io Free API fornece aos desenvolvedores acesso flexível a dados meteorológicos, garantindo ao mesmo tempo um uso justo. O plano gratuíto permite aos usuários um número grande de solicitações de API, segmentadas em limites diários, horários e por segundo. Discriminação dos limites de taxa: 500 solicitações por dia. Maiores informações em [Tomorrow.io API](https://docs.tomorrow.io/reference/welcome).

### Serviços AWS usados

- **Lambda:** serviço de computação serverless que executa código em resposta a eventos sem necessidade de gerenciar servidores.
- **IAM Role:** é uma identidade que pode ser criada no AWS Identity and Access Management (AWS IAM). São permissões temporárias para serviços ou usuários acessarem recursos da AWS com segurança.
- **CloudWatch:** serviço de monitoramento e observabilidade para logs, métricas e alarmes de aplicações e infraestrutura.
- **Kinesis:** plataforma para coleta, processamento e análise de dados em tempo real via streaming.
- **SNS (Simple Notification Service):** é um serviço de mensagens para publicação e assinatura (pub/sub) entre aplicações e usuários.
- **S3 (Simple Storage Service):** Armazenamento escalável e seguro de objetos, como arquivos, logs e backups.
- **Glue Crawler:** ferramenta que detecta e infere automaticamente esquemas de dados armazenados em diversas fontes.
- **Glue:** serviço de ETL (Extração, Transformação e Carga) serverless para preparar e mover dados.
- **Athena:** serviço de consulta interativa que usa SQL para analisar dados diretamente no S3.

### Arquitetura

<img width="1200" alt="aws_pipeline_realtime_and_pipeline_batch" src="https://github.com/marcelodutra7/my-repository/blob/b64ad6cdd64dc31407b729a4d39a02d35d09e0e9/images/aws_pipeline_realtime_and_pipeline_batch.png">

### Pipeline Real time - Steps

- Use o AWS Lambda (producer) para extrair os dados metereológicos da API do Tomorrow.io.
- Use o AWS CloudWatch para implantar o gatilho que ativará o código Python presente no AWS Lambda (producer) em uma periodicidade pré-estabelecida.
- Use o AWS IAM Role para atribuir as permissões que o AWS Lambda (producer) deve ter.
- Use o AWS Kinesis para coletar os dados extraídos pelo AWS Lambda
- Use o AWS Lambda (consumer) para consumir os dados coletados pelo AWS Kinesis.
- Use o AWS IAM Role novamente para atribuir as permissões que o AWS Lambda (consumer) deve ter.
- Use o AWS SNS para enviar alertas na periodicidade estabelecida por SMS e e-mail.

### Pipeline Batch - Steps
