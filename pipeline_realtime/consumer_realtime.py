# importando bibliotecas
import json
import base64
import os
import boto3

# Instancia o serviço do SNS para envio de notificações
sns_client = boto3.client('sns')

# Substituir pelo ARN do seu tópico SNS para onde as notificações serão enviadas
SNS_TOPIC_ARN = '<<_ARN_SNS_>>'

# Define os limites para os alertas meteorológicos a partir de variáveis de ambiente
PRECIPITATION_PROBABILITY_THRESHOLD = int(os.environ.get('PRECIPITATION_PROBABILITY', 10))
WIND_SPEED_THRESHOLD = int(os.environ.get('WIND_SPEED', 10))
WIND_GUST_THRESHOLD = int(os.environ.get('WIND_GUST', 10))
RAIN_INTENSITY_THRESHOLD = int(os.environ.get('RAIN_INTENSITY', 10))

def lambda_handler(event, context):
    # Verifica se há registros no evento recebido pelo Lambda
    if 'Records' not in event:
        print("No records found in the event.")
        return {
            'statusCode': 400,
            'body': json.dumps('No records found in the event')
        }

    # Itera sobre cada registro recebido no evento
    for record in event['Records']:
        # Decodifica os dados do Kinesis que estão em Base64
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        data = json.loads(payload)

        # Extrai os valores relevantes do JSON recebido
        precipitation_probability = data['data']['values'].get('precipitationProbability', 0)
        wind_speed = data['data']['values'].get('windSpeed', 0)
        wind_gust = data['data']['values'].get('windGust', 0)
        rain_intensity = data['data']['values'].get('rainIntensity', 0)

        # Verifica se algum dos valores extraídos excede os limites configurados
        if (precipitation_probability >= PRECIPITATION_PROBABILITY_THRESHOLD or
                wind_speed >= WIND_SPEED_THRESHOLD or
                wind_gust >= WIND_GUST_THRESHOLD or
                rain_intensity >= RAIN_INTENSITY_THRESHOLD):
            
            # Monta a mensagem de alerta meteorológico
            message = (
                f"Probabilidade de Chuva: {precipitation_probability}%\n"
                f"Velocidade do Vento: {wind_speed} m/s\n"
                f"Rajada de Vento: {wind_gust} m/s\n"
                f"Intensidade da Chuva: {rain_intensity} mm/h\n"
            )
            
            # Publica a mensagem no tópico SNS configurado
            response = sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=message,
                Subject='Alerta Meteorológico'
            )
            
            # Exibe a resposta da publicação no SNS
            print(f"SNS response: {response}")

    # Retorna uma resposta indicando que os registros foram processados
    return {
        'statusCode': 200,
        'body': json.dumps('Processed Kinesis records and sent to SNS if thresholds exceeded')
    }