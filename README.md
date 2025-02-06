# tomorrowio-data-weather-etl-aws

### Introdução

Este é um projeto de ETL usando API do Tomorrow.io para coletar dados meteorológicos e usará as ferramentas de nuvem da AWS para execução de uma pipeline real time e outra em batch. Na pipeline real time os dados coletados deverão enviar SMS e um e-mail caso informações pré-estabelecidas representem um alerta metereológico. Já na pipeline batch os mesmos dados coletados serão armazenados para consulta quando necessário. 

### Sobre o Tomorrow.io/API

O Tomorrow.io Free API fornece aos desenvolvedores acesso flexível a dados meteorológicos, garantindo ao mesmo tempo um uso justo. O plano gratuíto permite aos usuários um número grande de solicitações de API, segmentadas em limites diários, horários e por segundo. Discriminação dos limites de taxa: 500 solicitações por dia. Maiores informações em [Tomorrow.io API](https://docs.tomorrow.io/reference/welcome).

### Serviços AWS usados

- **Lambda:** Lambda é um serviço de computação sem servidor que permite que você execute seu código sem gerenciar servidores. Você pode usar o Lambda para executar código em resposta a eventos como alterações no S3, DynamoDB ou outros serviços da AWS.
- **IAM Role:** Uma IAM Role é uma identidade que pode ser criada no AWS Identity and Access Management (AWS IAM) e ter permissões atribuídas a ela diretamente ou via políticas do IAM.
- **CloudWatch:** o Amazon CloudWatch coleta e visualiza logs, métricas e dados de eventos em tempo real em painéis automatizados para otimizar sua infraestrutura e manutenção de aplicativos.
- **Kinesis:** o Amazon Kinesis é um serviço de streaming de dados totalmente gerenciado pela AWS. Ele permite a ingestão, processamento e análise em tempo real de grandes volumes de dados de streaming.
- **SNS:** o SNS (Simple Notification Service), provê um serviço de notificações. É uma forma de publicar mensagens destinadas a um ou mais inscritos na forma de endpoints.
- **S3 (Simple Storage Service):** O Amazon S3 é um serviço de armazenamento de objetos altamente escalável que pode armazenar e recuperar qualquer quantidade de dados de qualquer lugar na web. Ele é comumente usado para armazenar e distribuir grandes arquivos de mídia, backups de dados e arquivos estáticos de sites.
- **Glue Crawler:** O Glue Crawler é um serviço totalmente gerenciado que rastreia automaticamente suas fontes de dados, identifica formatos de dados e infere esquemas para criar um AWS Glue Data Catalog.
- **Glue:** o AWS Glue é um serviço de integração de dados com tecnologia sem servidor que facilita aos usuários de análise a descoberta, preparação, transferência e integração de dados de várias fontes.
- **Athena:** o Amazon Athena é um serviço de consulta interativo que facilita a análise de dados no Amazon S3 usando SQL padrão. Você pode usar o Athena para analisar dados no seu Glue Data Catalog ou em outros buckets do S3.

### Arquitetura

<img width="1163" alt="aws_pipeline_realtime_and_pipeline_batch" src="https://github.com/marcelodutra7/my-repository/blob/cda4f607fde1c24276d6793a5921e6f2713936ee/images/aws_pipeline_realtime_and_pipeline_batch.jpg">
