@echo off
echo ================================
echo Verifying LangChain Imports...
echo ================================

python -c "from langchain_community.embeddings import BedrockEmbeddings; print('BedrockEmbeddings OK')"
python -c "from langchain_community.llms import Bedrock; print('Bedrock OK')"
python -c "from langchain_community.document_loaders import PyPDFDirectoryLoader; print('PyPDFDirectoryLoader OK')"
python -c "from langchain_text_splitters import RecursiveCharacterTextSplitter; print('TextSplitter OK')"
python -c "from langchain_community.vectorstores import FAISS; print('FAISS OK')"
python -c "from langchain_core.prompts import PromptTemplate; print('PromptTemplate OK')"
python -c "from langchain_classic.chains import RetrievalQA; print('RetrievalQA OK')"
python -c "from langchain_aws import BedrockLLM; print('import BedrockLLM OK')"
python -c "from langchain_aws import ChatBedrock; print('ChatBedrock OK')"


echo ================================
echo Verification Complete!
echo ================================
pause
