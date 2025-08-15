import os
import openai
import json
from aws_lambda_powertools import Logger

logger = Logger()

openai.api_key = os.getenv('OPENAI_API_KEY')

def handler(event, context):
    logger.info("Received event: " + str(event))
    
    message = event['body']  # body should contain the user's message
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    messages = [
        {
            "role": "user",
            "content": message
        },
        {
            "role": "assistant",
            "content": response['choices'][0]['message']['content']
        }
    ]

    return {
        'statusCode': 200,
        'body': json.dumps({"messages": messages}),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
    }
