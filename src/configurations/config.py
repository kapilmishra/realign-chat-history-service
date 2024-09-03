"""
This module defines configurations settings for various services using Pydantic BaseSettings.
It includes settings for Azure and Pinecone.

Classes:
    AzureSettings: Configuration settings for Azure services.
    PineconeSettings: Configuration settings for Pinecone service.
    OriginalUrlSettings: Configuration settings for url for the backend call.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class AzureSettings(BaseSettings):
    """
    Configuration settings for Azure services.

    Attributes:
        OPENAI_APIKEY (str): The API key for accessing Azure services.
        OPENAI_BASE_URI (str): The base URI for Azure services.
        OPENAI_EMBEDDINGS_MODEL_NAME (str): The model name for Azure embeddings.
        OPENAI_GPT4_MODEL_NAME (str): The model name for Azure GPT-4.
        OPENAI_GPT_35_MODEL_NAME (str): The model name for Azure GPT-3.5.
    """

    model_config = SettingsConfigDict(env_prefix="AZURE_")

    OPENAI_APIKEY: str
    OPENAI_BASE_URI: str
    OPENAI_EMBEDDINGS_MODEL_NAME: str
    OPENAI_GPT4_MODEL_NAME: str
    OPENAI_GPT_35_MODEL_NAME: str


class PineconeSettings(BaseSettings):
    """
    Configuration settings for Pinecone service.

    Attributes:
        PINECONE_API_KEY (str): The API key for accessing Pinecone service.
        PINECONE_INDEX (str): The index for Pinecone service.
    """

    PINECONE_API_KEY: str
    PINECONE_INDEX: str


class OriginUrlSettings(BaseSettings):
    """
    Configuration settings for url for the backend call.

    Attributes:
        AZURE_API_URL (str): The API URL for Azure services.
        LOCAL_URL (str): The local URL for backend call.
    """

    AZURE_API_URL: str
    LOCAL_URL: str


class BlobSettings(BaseSettings):
    """
    Configuration settings for Blob storage service.

    Attributes:
        BLOB_CONNECTION_STRING (str): The connection string for accessing Blob storage.
        BLOB_CONTAINER_NAME (str): The name of the Blob container.
    """

    BLOB_CONNECTION_STRING: str
    BLOB_CONTAINER_NAME: str


class OpenAISettings(BaseSettings):
    """
    Configuration settings for OpenAI services.

    Attributes:
        OPENAI_API_KEY (str): The API key for accessing OpenAI services.
        OPENAI_MODEL_NAME (str): The model name for OpenAI services.
        OPENAI_EMBEDDINGS_MODEL_NAME (str): The model name for OpenAI embeddings.
    """

    OPENAI_API_KEY: str
    OPENAI_MODEL_NAME: str
    OPENAI_EMBEDDINGS_MODEL_NAME: str
