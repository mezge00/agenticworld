import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API key
api_key = "AIzaSyAHqUtYrqDgz1d8eZoBtF7mvAtFQMwDPZE"
if not api_key:
    raise ValueError("API key is missing. Please check your .env file.")

genai.configure(api_key=api_key)
