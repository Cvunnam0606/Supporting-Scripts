import boto3
import json

prompt_data = """
Act as Shakespeare and write a poem on Generative AI
"""

# Create Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Payload for Llama2
payload = {
    "prompt": "[INST]" + prompt_data + "[/INST]",
    "max_gen_len": 512,
    "temperature": 0.5,
    "top_p": 0.9
}

body = json.dumps(payload)
##model_id = "meta.llama2-70b-chat-v1"
##model_id = "meta.llama3-8b-instruct-v1"
##model_id = "meta.llama2-13b-chat-v1"
model_id = "amazon.nova-lite-v1:0"

# Invoke model
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

# Parse response
response_body = json.loads(response["body"].read())

# Different models return slightly different keys
if "generation" in response_body:
    response_text = response_body["generation"]
elif "outputs" in response_body:
    response_text = response_body["outputs"][0]["text"]
else:
    response_text = str(response_body)

print(response_text)
