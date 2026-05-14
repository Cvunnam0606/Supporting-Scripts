import boto3

bedrock = boto3.client("bedrock", region_name="us-east-1")

response = bedrock.list_foundation_models()

print("Filtered Bedrock Text Models (Meta & Anthropic):")
for model in response["modelSummaries"]:
    provider = model.get("providerName", "")
    input_modalities = model.get("inputModalities", [])
    if "TEXT" in input_modalities and provider in ["Meta", "Anthropic"]:
        print(f"- {model['modelId']} ({provider})")
