import boto3
import os
import json
from shared.utils import upload_files_to_s3, invoke_rag_llm

s3_client = boto3.client('s3')
bedrock_client = boto3.client('bedrock')

def lambda_handler(event, context):
    try:
        # Parse the API Gateway event body
        body = json.loads(event['body'])
        files = body['files']
        knowledgebase_id = os.environ['KNOWLEDGEBASE_ID'] 
        bucket_name = os.environ['BUCKET_NAME']
        
        # Step 1: Upload files to S3
        uploaded_files = upload_files_to_s3(s3_client, bucket_name, files)
        
        # Step 2: Invoke RAG LLM with the uploaded documents
        rag_response = invoke_rag_llm(bedrock_client, knowledgebase_id, uploaded_files)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'uploaded_files': uploaded_files,
                'rag_response': rag_response
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }