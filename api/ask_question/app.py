import boto3
import json
import os
from shared.utils import get_rag_response

bedrock_client = boto3.client('bedrock')

def lambda_handler(event, context):
    try:
        # Parse the API Gateway event body
        body = json.loads(event['body'])
        knowledgebase_id = os.environ['KNOWLEDGEBASE_ID'] 
        question = body['question']
        
        # Get the RAG response
        response = get_rag_response(bedrock_client, knowledgebase_id, question)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': response
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }