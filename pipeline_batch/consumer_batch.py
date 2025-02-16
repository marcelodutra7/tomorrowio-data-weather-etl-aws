# importando bibliotecas
import json
import boto3
import base64
import os
from datetime import datetime

# Cliente do S3 para armazenamento de dados
s3_client = boto3.client('s3')

# Nome do bucket S3 obtido da variável de ambiente
BUCKET_NAME = os.getenv('BUCKET_NAME')

def lambda_handler(event, context):
    # Itera sobre cada registro recebido no evento do Kinesis
    for record in event['Records']:
        # Decodifica os dados do Kinesis que estão em Base64
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        
        # Obtém a data atual para criar partições no S3
        now = datetime.utcnow()
        year = now.year
        month = now.month
        day = now.day

        # Cria um nome de arquivo único com partições year, month, day
        file_name = f"raw/year={year}/month={month}/day={day}/weather_data_{now.isoformat()}.json"
        
        # Salva o dado no bucket S3
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data)
        )
    
    # Retorna uma resposta indicando que os dados foram salvos no S3
    return {
        'statusCode': 200,
        'body': json.dumps('Dados salvos no S3 com sucesso')
    }
