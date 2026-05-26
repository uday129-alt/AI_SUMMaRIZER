"""
Groq API Integration for Content Summarization
This module handles all API calls to Groq for AI-powered summarization.

LangSmith Integration:
- Provides comprehensive tracing and observability for AI calls
- Tracks prompts, responses, latency, and errors in LangSmith dashboard
- Enable by setting LANGSMITH_TRACING=true in .env
- Visit https://smith.langchain.com/ to view traces
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Import LangSmith tracing decorator
try:
    from langsmith import traceable
    LANGSMITH_AVAILABLE = True
except ImportError:
    LANGSMITH_AVAILABLE = False
    # Fallback: create a no-op decorator if langsmith is not installed
    def traceable(func):
        return func

# Load environment variables from .env file
load_dotenv()


class ContentSummarizer:
    """
    A class to handle content summarization using Groq API with LangSmith tracing.
    
    Attributes:
        client: Groq API client
        model: The AI model to use for summarization
        langsmith_enabled: Boolean indicating if LangSmith tracing is enabled
        langsmith_api_key: API key for LangSmith (if available)
    """
    
    def __init__(self):
        """
        Initialize the ContentSummarizer with Groq API credentials.
        Reads both API key and model from environment variables (.env file).
        Configures LangSmith tracing if enabled.
        """
        # Get API key from environment variables
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables. "
                "Please add it to your .env file."
            )
        
        # Get model from environment variables (default: llama-3.3-70b-versatile)
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        
        # Initialize Groq client
        self.client = Groq(api_key=api_key)
        
        # ====================================================================
        # LangSmith Tracing Configuration
        # ====================================================================
        # LangSmith provides observability for all AI operations
        # This includes: prompts, responses, latency, errors, and execution traces
        
        self.langsmith_enabled = (
            os.getenv("LANGSMITH_TRACING", "false").lower() == "true"
        )
        self.langsmith_api_key = os.getenv("LANGSMITH_API_KEY")
        
        # Log warning if tracing is enabled but no API key is set
        if self.langsmith_enabled and not self.langsmith_api_key:
            print(
                "⚠️  LangSmith tracing is enabled but LANGSMITH_API_KEY is not set. "
                "Traces will not be recorded. Get an API key from: "
                "https://smith.langchain.com/settings/api-keys"
            )
    
    @traceable
    def generate_summary(
        self,
        text: str,
        summary_type: str = "short",
        tone: str = "professional"
    ) -> str:
        """
        Generate a summary of the given text using Groq API.
        
        This method is decorated with @traceable from LangSmith to provide
        comprehensive observability. When enabled, every call is traced with:
        - Input parameters (text, summary_type, tone)
        - Generated prompt
        - Groq API response
        - Execution time
        - Any errors or exceptions
        
        Traces can be viewed in the LangSmith dashboard:
        https://smith.langchain.com/projects/
        
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
            # This API call is traced by LangSmith (if enabled)
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
            summary = completion.choices[0].message.content
            return summary
        
        except Exception as e:
            # LangSmith will automatically capture this error in the trace
            error_message = f"Error calling Groq API: {str(e)}"
            raise Exception(error_message)
    
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
