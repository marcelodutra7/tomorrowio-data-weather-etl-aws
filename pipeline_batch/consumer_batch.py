# importando bibliotecas
import json
import boto3
import base64
import os
from datetime import datetime

# cliente do S3
s3_client = boto3.client('s3')

# nome do bucket S3
BUCKET_NAME = os.getenv('BUCKET_NAME')

def lambda_handler(event, context):
    for record in event['Records']:
        # decodifica o registro do Kinesis
        payload = base64.b64decode(record['kinesis']['data'])
        data = json.loads(payload)
        
        # obtém a data atual para criar partições no S3
        now = datetime.utcnow()
        year = now.year
        month = now.month
        day = now.day

        # cria um nome de arquivo único com partições year, month, day
        file_name = f"raw/year={year}/month={month}/day={day}/weather_data_{now.isoformat()}.json"
        
        # salva o dado no bucket S3
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=json.dumps(data)
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Dados salvos no S3 com sucesso')
    }
