import os
from dotenv import load_dotenv

# Load environment variable from .env file
load_dotenv()

# Retrieve the API key from environment variables
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Instantiate Cohere Client using the API key
co = cohere.Client(COHERE_API_KEY)