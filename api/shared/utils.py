import os

def upload_files_to_s3(s3_client, bucket_name, files):
    """
    Uploads multiple files to the specified S3 bucket.
    """
    uploaded_files = []
    for file in files:
        file_name = os.path.basename(file)
        s3_client.upload_file(file, bucket_name, file_name)
        uploaded_files.append(f"s3://{bucket_name}/{file_name}")
        print(f"Uploaded {file_name} to {bucket_name}")
    return uploaded_files

def invoke_rag_llm(bedrock_client, knowledgebase_id, documents):
    """
    Invokes the RAG LLM with the provided knowledge base ID and documents.
    """
    response = bedrock_client.invoke_model(
        knowledgebaseId=knowledgebase_id,
        documents=documents,
        modelId='your-model-id'  # Replace with your model ID
    )
    return response

def get_rag_response(bedrock_client, knowledgebase_id, question):
    """
    Invokes the RAG LLM to get a response for the given question.
    """
    response = bedrock_client.invoke_model(
        knowledgebaseId=knowledgebase_id,
        question=question,
        modelId='your-model-id'  # Replace with your model ID
    )
    return response