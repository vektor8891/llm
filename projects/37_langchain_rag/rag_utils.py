"""
RAG utilities for document processing and question answering.
This module contains all the helper functions for the RAG chatbot.
"""

import os
from dotenv import load_dotenv
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from langchain_ibm.llms import WatsonxLLM
from langchain_ibm.embeddings import WatsonxEmbeddings
from langchain_community.document_loaders import (
    TextLoader,
    PyMuPDFLoader,
    UnstructuredMarkdownLoader,
    JSONLoader,
    CSVLoader,
    UnstructuredCSVLoader,
    WebBaseLoader,
    Docx2txtLoader,
    UnstructuredFileLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA


def get_llm():
    """Initialize and return a WatsonxLLM instance with specified parameters."""
    load_dotenv("../../.env")

    # Updated to use the recommended non-deprecated model
    model_id = 'mistralai/mistral-small-3-1-24b-instruct-2503'
    parameters = {
        GenParams.MAX_NEW_TOKENS: 256,
        GenParams.TEMPERATURE: 0.5,
    }
    watsonx_llm = WatsonxLLM(
        model_id=model_id,
        url=os.getenv("WATSONX_URL"),
        apikey=os.getenv('IBM_CLOUD_API_KEY'),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        params=parameters
    )
    return watsonx_llm


def document_loader(file):
    """Load various document types and return their content."""
    # Get file extension
    _, extension = os.path.splitext(file.name)
    extension = extension.lower()

    # Select appropriate loader based on file extension
    if extension == '.pdf':
        loader = PyMuPDFLoader(file.name)
    elif extension == '.txt':
        loader = TextLoader(file.name)
    elif extension in ['.md', '.markdown']:
        loader = UnstructuredMarkdownLoader(file.name)
    elif extension == '.json':
        loader = JSONLoader(file.name, jq_schema='.', text_content=False)
    elif extension == '.csv':
        try:
            loader = CSVLoader(file.name)
        except Exception:
            loader = UnstructuredCSVLoader(file.name)
    elif extension in ['.doc', '.docx']:
        loader = Docx2txtLoader(file.name)
    elif extension in ['.html', '.htm']:
        loader = UnstructuredFileLoader(file.name)
    else:
        try:
            loader = UnstructuredFileLoader(file.name)
        except Exception as e:
            raise ValueError(
                f"Unsupported file type: {extension}. "
                f"Supported formats: .pdf, .txt, .md, .json, .csv, .doc, .docx, .html. "
                f"Error: {str(e)}"
            )

    # Load the document using the selected loader
    try:
        loaded_document = loader.load()
        return loaded_document
    except Exception as e:
        raise ValueError(f"Failed to load document {file.name}: {str(e)}")


def text_splitter(data):
    """Split the loaded document into manageable chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        length_function=len,
    )
    chunks = text_splitter.split_documents(data)
    return chunks


def watsonx_embedding():
    """Initialize and return a WatsonxEmbeddings instance."""
    load_dotenv("../../.env")

    embed_params = {
        EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
        EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True},
    }
    watsonx_embedding = WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr",
        url=os.getenv("WATSONX_URL"),
        apikey=os.getenv('IBM_CLOUD_API_KEY'),
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        params=embed_params,
    )
    return watsonx_embedding


def vector_database(chunks):
    """Create a vector database from the document chunks."""
    embedding_model = watsonx_embedding()
    vectordb = Chroma.from_documents(chunks, embedding_model)
    return vectordb


def retriever(file):
    """Create a retriever from the document file."""
    splits = document_loader(file)
    chunks = text_splitter(splits)
    vectordb = vector_database(chunks)
    retriever = vectordb.as_retriever()
    return retriever


def retriever_qa(file, query):
    """Retrieve answers from the document using a retriever and a language model."""
    llm = get_llm()
    retriever_obj = retriever(file)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever_obj,
        return_source_documents=False
    )
    response = qa.invoke(query)
    return response['result']
