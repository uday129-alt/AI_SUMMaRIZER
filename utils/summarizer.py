"""
Groq API Integration for Content Summarization
This module handles all API calls to Groq for AI-powered summarization.
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class ContentSummarizer:
    """
    A class to handle content summarization using Groq API.
    
    Attributes:
        client: Groq API client
        model: The AI model to use for summarization
    """
    
    def __init__(self):
        """
        Initialize the ContentSummarizer with Groq API credentials.
        Reads both API key and model from environment variables (.env file).
        """
        # Get API key from environment variables
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables. "
                "Please add it to your .env file."
            )
        
        # Get model from environment variables (default: mixtral-8x7b-32768)
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        
        # Initialize Groq client
        self.client = Groq(api_key=api_key)
    
    def generate_summary(
        self,
        text: str,
        summary_type: str = "short",
        tone: str = "professional"
    ) -> str:
        """
        Generate a summary of the given text using Groq API.
        
        Args:
            text: The text to summarize
            summary_type: Type of summary - 'short', 'detailed', or 'bullet'
            tone: Tone of summary - 'professional', 'simple', 'academic', or 'casual'
        
        Returns:
            The generated summary as a string
        
        Raises:
            ValueError: If text is empty
            Exception: If API call fails
        """
        # Validate input
        if not text or not text.strip():
            raise ValueError("Input text cannot be empty")
        
        # Define summary type instructions
        summary_instructions = {
            "short": "Generate a concise summary in 2-3 sentences.",
            "detailed": "Generate a comprehensive summary with multiple paragraphs, covering all key points.",
            "bullet": "Generate a bullet-point summary with 5-8 key points.",
        }
        
        # Define tone instructions
        tone_instructions = {
            "professional": "Use a formal, business-appropriate tone.",
            "simple": "Use simple, easy-to-understand language.",
            "academic": "Use an academic, scholarly tone with proper terminology.",
            "casual": "Use a friendly, conversational tone.",
        }
        
        # Get instructions based on selections
        summary_instruction = summary_instructions.get(summary_type, summary_instructions["short"])
        tone_instruction = tone_instructions.get(tone, tone_instructions["professional"])
        
        # Construct the prompt
        prompt = f"""You are an expert content summarizer. Your task is to create a high-quality summary.

SUMMARY TYPE: {summary_instruction}
TONE: {tone_instruction}

CONTENT TO SUMMARIZE:
{text}

Please provide the summary now. Ensure it captures the main ideas and is appropriate for the specified tone."""
        
        try:
            # Call Groq API using chat completions
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                # Set reasonable limits for response
                max_tokens=1024,
                temperature=0.7,  # Balance between creativity and consistency
            )
            
            # Extract and return the summary
            return completion.choices[0].message.content
        
        except Exception as e:
            raise Exception(f"Error calling Groq API: {str(e)}")
    
    def check_api_status(self) -> bool:
        """
        Check if the Groq API is accessible and API key is valid.
        
        Returns:
            True if API is accessible, False otherwise
        """
        try:
            # Make a minimal API call to check status
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "test"}],
                max_tokens=1,
                temperature=0,
            )
            return True
        except Exception as e:
            # Debug: print the error for troubleshooting
            error_msg = str(e).lower()
            
            # Check for common error patterns
            if "authentication" in error_msg or "unauthorized" in error_msg or "invalid" in error_msg:
                print(f"API Authentication Error: {e}")
            elif "connection" in error_msg or "timeout" in error_msg or "network" in error_msg:
                print(f"API Connection Error: {e}")
            else:
                print(f"API Status Check Error: {e}")
            
            return False
