"""
Configuration Module
Centralized configuration for the AI Content Summarizer application.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# ============================================================================
# API CONFIGURATION
# ============================================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

# Available Groq models
AVAILABLE_MODELS = {
    "llama-3.3-70b": "llama-3.3-70b-versatile",
    "mixtral": "mixtral-8x7b-32768",
    "llama3-8b": "llama3-8b-8192",
    "gemma": "gemma-7b-it",
}


# ============================================================================
# STREAMLIT CONFIGURATION
# ============================================================================

# Page configuration
PAGE_CONFIG = {
    "page_title": "AI Content Summarizer",
    "page_icon": "✨",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
}

# App metadata
APP_NAME = "AI Content Summarizer"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Transform your content into intelligent summaries powered by Groq AI"


# ============================================================================
# SUMMARIZATION CONFIGURATION
# ============================================================================

# Summary types
SUMMARY_TYPES = {
    "short": "Concise 2-3 sentence overview",
    "detailed": "Comprehensive multi-paragraph summary",
    "bullet": "Key points in bullet format (5-8 points)",
}

# Available tones
TONES = {
    "professional": "Formal business tone",
    "simple": "Easy-to-understand language",
    "academic": "Scholarly and technical tone",
    "casual": "Friendly and conversational tone",
}

# Default selections
DEFAULT_SUMMARY_TYPE = "short"
DEFAULT_TONE = "professional"

# API parameters
MAX_TOKENS = 1024
TEMPERATURE = 0.7
REQUEST_TIMEOUT = 30


# ============================================================================
# FILE UPLOAD CONFIGURATION
# ============================================================================

# Maximum file sizes (in bytes)
MAX_PDF_SIZE = 50 * 1024 * 1024  # 50 MB
MAX_TEXT_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# Allowed file extensions
ALLOWED_PDF_EXTENSIONS = [".pdf"]
ALLOWED_TEXT_EXTENSIONS = [".txt"]

# Text extraction settings
PDF_ENCODING = "utf-8"
MAX_PAGES_TO_PROCESS = 100


# ============================================================================
# WEB SCRAPING CONFIGURATION
# ============================================================================

# Request headers
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Scraping settings
SCRAPING_TIMEOUT = 10  # seconds
MAX_CONTENT_LENGTH = 1000000  # 1 MB

# Blocked elements for web scraping
BLOCKED_TAGS = ["script", "style", "nav", "footer", "iframe", "noscript"]


# ============================================================================
# TEXT PROCESSING CONFIGURATION
# ============================================================================

# Reading speed
WORDS_PER_MINUTE = 200

# Text processing
MIN_WORDS_FOR_SUMMARIZATION = 10
MAX_WORDS_FOR_SUMMARIZATION = 100000


# ============================================================================
# UI CONFIGURATION
# ============================================================================

# Colors
COLOR_PRIMARY = "#1f77b4"
COLOR_SUCCESS = "#28a745"
COLOR_ERROR = "#dc3545"
COLOR_WARNING = "#ffc107"
COLOR_INFO = "#17a2b8"

# Sidebar features
SIDEBAR_FEATURES = [
    "📄 Text Summarization",
    "📑 PDF File Upload",
    "📝 Text File Upload",
    "🌐 URL Web Scraping",
    "🎯 Multiple Summary Types",
    "🎨 Tone Selection",
    "📊 Word & Character Count",
    "💾 Download Summaries",
    "⚡ Fast Processing",
]

# Use cases
USE_CASES = [
    "🎓 College Projects",
    "📋 Resume Projects",
    "🚀 Internship Showcases",
]


# ============================================================================
# ERROR MESSAGES
# ============================================================================

ERROR_MESSAGES = {
    "no_api_key": "GROQ_API_KEY not found. Please add it to your .env file.",
    "api_connection_error": "Failed to connect to Groq API. Check your internet and API key.",
    "empty_input": "Please provide some content to summarize.",
    "invalid_url": "Invalid URL format. Please enter a valid website URL.",
    "invalid_pdf": "Invalid PDF file. Please ensure the file is a valid PDF.",
    "invalid_text_file": "Invalid text file. Please ensure the file is UTF-8 encoded.",
    "file_too_large": "File is too large. Please upload a smaller file.",
    "no_content_extracted": "Could not extract content from the file or URL.",
    "timeout": "Request timed out. The operation took too long. Please try again.",
}

# Success messages
SUCCESS_MESSAGES = {
    "summary_generated": "✅ Summary generated successfully!",
    "file_uploaded": "✅ File uploaded successfully!",
    "content_extracted": "✅ Content extracted successfully!",
}


# ============================================================================
# VALIDATION CONFIGURATION
# ============================================================================

# URL validation
VALID_URL_SCHEMES = ("http://", "https://")

# Text validation
MIN_INPUT_LENGTH = 10
MAX_INPUT_LENGTH = 100000


# ============================================================================
# ENVIRONMENT VALIDATION
# ============================================================================

def validate_configuration():
    """
    Validate that all required configuration is present.
    
    Returns:
        tuple: (is_valid, error_message)
    """
    if not GROQ_API_KEY:
        return False, ERROR_MESSAGES["no_api_key"]
    
    if GROQ_MODEL not in AVAILABLE_MODELS.values():
        return False, f"Unknown Groq model: {GROQ_MODEL}"
    
    return True, "Configuration is valid"


# ============================================================================
# EXPORT CONFIGURATION
# ============================================================================

def get_config(key):
    """
    Get configuration value by key.
    
    Args:
        key: Configuration key
    
    Returns:
        Configuration value or None
    """
    config_dict = {
        "api_key": GROQ_API_KEY,
        "model": GROQ_MODEL,
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "summary_types": SUMMARY_TYPES,
        "tones": TONES,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
    }
    return config_dict.get(key)


if __name__ == "__main__":
    # Test configuration validation
    is_valid, message = validate_configuration()
    print(f"Configuration valid: {is_valid}")
    print(f"Message: {message}")
    print(f"App: {APP_NAME} v{APP_VERSION}")
    print(f"Model: {GROQ_MODEL}")
