import os
import google.generativeai as genai
from pydantic import BaseModel, Field


class GoogleGeminiLLM(BaseModel):
    model_name: str = Field(default="gemini-2.0-flash-exp", description="The Gemini model to use.")
    generation_config: dict = Field(
        default_factory=lambda: {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
    )
    chat_session: genai.ChatSession = None

    class Config:
        arbitrary_types_allowed = True  # Allow arbitrary types

    def __init__(self, **data):
        super().__init__(**data)
        # Configure the API key from the environment variable
        api_key = "AIzaSyAZepiNxbeDssIlKbzZjXqOXrcaLCvVBu0"
        if not api_key:
            raise ValueError("Google API key is missing. Please set the 'GEMINI_API_KEY' environment variable.")
        genai.configure(api_key=api_key)

        # Initialize the model
        model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config,
        )

        # Start a chat session
        self.chat_session = model.start_chat(history=[])

    def _generate(self, input_text: str, context=None) -> str:
        try:
            # Include context if provided
            message = f"Context: {context}\n{input_text}" if context else input_text
            
            # Send the message to the chat session
            response = self.chat_session.send_message(message)
            
            # Extract and return the text response
            return response.text
        except Exception as e:
            raise ValueError(f"Error calling Gemini API: {str(e)}")

    def call(self, input_text: str, context=None) -> str:
        return self._generate(input_text, context)
