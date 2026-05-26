# ✨ AI Content Summarizer

A powerful, beginner-friendly web application for intelligent content summarization using Python, Streamlit, and Groq API. Perfect for students, professionals, and content creators.

![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-FF4B4B?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776ab?style=for-the-badge&logo=python)
![Groq API](https://img.shields.io/badge/Groq%20API-Enabled-00D9FF?style=for-the-badge)

---

## 🎯 Features

### Input Methods
- ✍️ **Plain Text**: Paste content directly
- 📄 **PDF Files**: Upload and summarize PDF documents
- 📝 **Text Files**: Upload `.txt` files
- 🌐 **Website URLs**: Scrape and summarize web content

### Summary Types
- **Short**: Quick 2-3 sentence overview
- **Detailed**: Comprehensive multi-paragraph analysis
- **Bullet**: Key points in bullet format (5-8 points)

### Tone Selection
- **Professional**: Formal business tone
- **Simple**: Easy-to-understand language
- **Academic**: Scholarly and technical language
- **Casual**: Friendly and conversational

### Additional Features
- 📊 Word and character count statistics
- 📈 Text compression ratio calculation
- 💾 Download summaries as `.txt` files
- 📋 Copy-to-clipboard functionality
- 🎨 Modern, responsive UI design
- 🚀 Fast processing with Groq API
- 🔄 Clear/reset functionality
- ✅ Comprehensive error handling

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python** | Backend programming language |
| **Streamlit** | Web application framework |
| **Groq API** | AI model for summarization |
| **LangSmith** | Observability & tracing (optional) |
| **PyPDF2** | PDF text extraction |
| **BeautifulSoup4** | Web scraping |
| **Requests** | HTTP client for web requests |
| **python-dotenv** | Environment variable management |

---

## 🔍 LangSmith Integration (Observability & Tracing)

**What is LangSmith?**
LangSmith provides comprehensive observability and tracing for AI applications. It tracks every API call, response, error, and execution time, allowing you to monitor and debug your AI workflows in real-time.

**Why Use LangSmith?**
- 📊 **Monitor Performance**: Track API response times and success rates
- 🐛 **Debug Errors**: View complete execution traces with context
- 📈 **Analyze Usage**: Understand usage patterns and identify improvements
- ✅ **Production-Ready**: Enterprise-grade monitoring for deployed applications
- 🔐 **Data Security**: Traces are encrypted and stored securely

**Tracked Data in LangSmith:**
- Input prompts and parameters
- AI model responses and outputs
- Execution latency and performance metrics
- Errors and exceptions with full context
- Complete call stack and execution traces

**View Your Traces:**
All traces are available in your LangSmith dashboard at: https://smith.langchain.com/projects/

---

## 📋 Project Structure

```
ai-content-summarizer/
│
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── .env                        # API credentials (NOT in git)
├── .env.example                # Example environment file
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
│
└── utils/
    ├── __init__.py             # Package initialization
    ├── summarizer.py           # Groq API integration
    ├── pdf_reader.py           # PDF extraction logic
    ├── web_scraper.py          # URL scraping logic
    └── helpers.py              # Utility functions
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Groq API key (free tier available)
- Internet connection

### Step 1: Clone or Download the Project

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-content-summarizer.git
cd ai-content-summarizer
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Get Groq API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up for a free account
3. Navigate to the **API Keys** section
4. Generate a new API key
5. Copy the API key

### Step 4.5: (Optional) Set Up LangSmith Tracing

LangSmith provides observability and tracing for all AI operations. It's optional but highly recommended for monitoring and debugging.

1. Visit [LangSmith](https://smith.langchain.com/)
2. Sign up for a free account
3. Navigate to **Settings** → **API Keys**
4. Create a new API key and copy it

### Step 5: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys:
# GROQ_API_KEY=your_actual_groq_key_here
#
# For LangSmith (optional):
# LANGSMITH_TRACING=true
# LANGSMITH_API_KEY=your_langsmith_key_here
# LANGSMITH_ENDPOINT=https://api.smith.langchain.com
# LANGSMITH_PROJECT=AI_Summarizer
```

**On Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
# Then edit .env with your API keys
```

**Your .env file should look like:**
```ini
# Required: Groq API Key
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
GROQ_MODEL=llama-3.3-70b-versatile

# Optional: LangSmith Tracing (for observability)
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=ls_xxxxxxxxxxxxxxxxxxxxxxxxxxx
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=AI_Summarizer
```

### Step 6: Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

---

## 📖 How to Use

### Text Summarizer Tab
1. Paste your content in the text area
2. Select summary type (Short, Detailed, or Bullet)
3. Choose your preferred tone
4. Click "🚀 Generate Summary"
5. Copy or download the summary

### File Summarizer Tab
1. Upload a PDF or TXT file
2. Optionally preview the content
3. Configure summary preferences
4. Click "🚀 Generate Summary"
5. Download the results

### URL Summarizer Tab
1. Enter a website URL
2. Preview the webpage content (optional)
3. Set summary options
4. Click "🚀 Generate Summary"
5. Download or copy the summary

---

## 🌐 Deployment on Streamlit Cloud

### Prerequisites
- GitHub account with repository containing this project
- Streamlit account

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Connect your GitHub repository
4. Select the repo and branch
5. Set the main file path: `app.py`

### Step 3: Add API Keys as Secrets
1. In Streamlit Cloud dashboard, go to **Settings** → **Secrets**
2. Add your API keys:
```ini
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_MODEL = "llama-3.3-70b-versatile"

# Optional: Add LangSmith tracing (for observability)
LANGSMITH_TRACING = "true"
LANGSMITH_API_KEY = "ls_xxxxxxxxxxxxxxxxxxxxxxxxxxx"
LANGSMITH_ENDPOINT = "https://api.smith.langchain.com"
LANGSMITH_PROJECT = "AI_Summarizer"
```

3. Deploy!

**Your app is now live! 🎉**

---

## 🔐 Security Best Practices

### ✅ Do's
- ✓ Store API keys in `.env` file
- ✓ Add `.env` to `.gitignore`
- ✓ Use environment variables for secrets
- ✓ Never commit `.env` files
- ✓ Use Streamlit Secrets for cloud deployment

### ❌ Don'ts
- ✗ Hardcode API keys in source files
- ✗ Commit `.env` files to GitHub
- ✗ Share API keys in public forums
- ✗ Use development keys in production

---

## 📚 Code Documentation

### Key Modules

#### `summarizer.py`
Handles all Groq API calls for content summarization.

```python
from utils import ContentSummarizer

# Initialize
summarizer = ContentSummarizer()

# Generate summary
summary = summarizer.generate_summary(
    text="Your content here",
    summary_type="short",
    tone="professional"
)
```

#### `pdf_reader.py`
Extract text from PDF files.

```python
from utils import extract_text_from_pdf

# Extract text
text = extract_text_from_pdf("document.pdf")
```

#### `web_scraper.py`
Scrape and extract text from websites.

```python
from utils import scrape_url_content

# Get content
content = scrape_url_content("https://example.com")
```

#### `helpers.py`
Utility functions for text processing.

```python
from utils import count_words, count_characters, format_for_download

# Count words
words = count_words(text)

# Download format
formatted = format_for_download("Title", text)
```

---

## ⚙️ Configuration

### Available Groq Models
- `llama-3.3-70b-versatile` (Recommended) - Most capable, best quality
- `mixtral-8x7b-32768` - Fast and powerful
- `llama3-8b-8192` - Lightweight and fast
- `gemma-7b-it` - Instruction-tuned

To change the model, edit your `.env` file:
```env
GROQ_MODEL=llama-3.3-70b-versatile
```

Then restart the app:
```bash
streamlit run app.py
```

---

## � LangSmith Observability Guide

### Quick Setup

1. **Sign Up for LangSmith** (Free)
   - Visit: https://smith.langchain.com/
   - Create a free account
   - Navigate to **Settings** → **API Keys**
   - Generate an API key

2. **Add to `.env`**
   ```ini
   LANGSMITH_TRACING=true
   LANGSMITH_API_KEY=your_api_key_from_smith
   LANGSMITH_ENDPOINT=https://api.smith.langchain.com
   LANGSMITH_PROJECT=AI_Summarizer
   ```

3. **Restart the App**
   ```bash
   streamlit run app.py
   ```

4. **View Your Traces**
   - Go to: https://smith.langchain.com/projects/
   - Select your project: "AI_Summarizer"
   - Watch traces appear in real-time as you use the app

### What Gets Tracked?

Every time you generate a summary, LangSmith automatically captures:

- **Input Data**: The text you're summarizing
- **Parameters**: Summary type and tone selected
- **Prompts**: The exact prompt sent to Groq
- **Responses**: The full AI response
- **Latency**: How long the API call took
- **Errors**: Any exceptions or failures
- **Metadata**: Timestamps and execution context

### Example Trace View

In your LangSmith dashboard, you'll see:
```
Project: AI_Summarizer
├── Call 1: generate_summary
│   ├── Input: summary_type="short", tone="professional"
│   ├── Prompt: "You are an expert content summarizer..."
│   ├── Output: "This is the generated summary..."
│   ├── Latency: 2.34 seconds
│   └── Status: Success ✓
│
├── Call 2: generate_summary
│   ├── Input: summary_type="detailed", tone="academic"
│   ├── Prompt: "You are an expert content summarizer..."
│   ├── Output: "Comprehensive multi-paragraph summary..."
│   ├── Latency: 4.12 seconds
│   └── Status: Success ✓
```

### Debugging with LangSmith

**Problem**: Summary is not what you expected
- **Solution**: Go to LangSmith and check the exact prompt and response

**Problem**: API calls are slow
- **Solution**: Check latency in LangSmith for pattern analysis

**Problem**: Errors when generating summaries
- **Solution**: LangSmith shows full error traces with context

### Disabling LangSmith

If you want to disable tracing:
```ini
LANGSMITH_TRACING=false
```

The app will still work normally, just without observability traces.

### Production Deployment

On Streamlit Cloud, add to **Secrets** (Settings → Secrets):
```toml
LANGSMITH_TRACING = "true"
LANGSMITH_API_KEY = "ls_your_key_here"
LANGSMITH_ENDPOINT = "https://api.smith.langchain.com"
LANGSMITH_PROJECT = "AI_Summarizer"
```

---

## �🐛 Troubleshooting

### Groq API Issues

### Error: "GROQ_API_KEY not found"
- Solution: Check that `.env` file exists and contains `GROQ_API_KEY=your_key`

### Error: "Invalid PDF file"
- Solution: Ensure the PDF is not corrupted. Try with a different PDF.

### Error: "Connection error"
- Solution: Check internet connection. Verify Groq API status.

### Error: "No readable content found"
- Solution: Ensure the input is not empty. Try with different content.

### Slow Processing
- Solution: Try "Short" summary type for faster results.

### LangSmith Tracing Issues

### Error: "⚠️ LangSmith tracing is enabled but LANGSMITH_API_KEY is not set"
- **Solution**: Either disable tracing or add your LangSmith API key:
  ```ini
  LANGSMITH_TRACING=true
  LANGSMITH_API_KEY=your_api_key
  ```

### Traces not appearing in LangSmith dashboard
- **Check**: Ensure `LANGSMITH_TRACING=true` in `.env`
- **Check**: Ensure `LANGSMITH_API_KEY` is valid
- **Check**: Wait a few seconds; traces appear with slight delay
- **Check**: Verify you're viewing the correct project in dashboard

### "Invalid LangSmith API key" error
- **Solution**: Go to https://smith.langchain.com/settings/api-keys
- **Solution**: Generate a new API key and update `.env`

### LangSmith slowing down the app
- **Solution**: This is minimal; LangSmith tracing is lightweight
- **Solution**: If concerned, disable with `LANGSMITH_TRACING=false`

---

## 💡 Tips & Tricks

### For Best Results
1. Use "Detailed" for long documents needing comprehensive summary
2. Use "Bullet" for quick key points
3. Use "Professional" tone for business documents
4. Use "Simple" tone for general audience
5. Preview large PDFs before summarizing

### Performance Optimization
- Summarize documents < 10,000 words for faster results
- Use "Short" summary for quick summaries
- Batch process multiple documents

### Cost Optimization (Groq Free Tier)
- Short summaries use fewer tokens
- Bullet points are more cost-effective
- Use text input instead of URLs when possible

---

## 📸 Screenshots

### Main Interface
![Main Interface](./screenshots/main.png)

### Text Summarizer
![Text Tab](./screenshots/text-tab.png)

### File Summarizer
![File Tab](./screenshots/file-tab.png)

### URL Summarizer
![URL Tab](./screenshots/url-tab.png)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🎓 Perfect For

- 📚 **College Projects**: AI/ML demonstrations
- 📋 **Resume Projects**: Showcase your skills
- 🚀 **Internship Showcases**: Impress your interviewers
- 💼 **Portfolio**: Add to your professional portfolio
- 🔬 **Research**: Content analysis tool

---

## 📞 Support & Contact

- 📧 Email: your.email@example.com
- 🐦 Twitter: [@yourhandle](https://twitter.com)
- 💬 Discord: YourServer#1234

---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [Groq](https://groq.com/) - For the powerful API
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - For web scraping
- Community contributors and users

---

## 📊 Roadmap

### Planned Features
- [ ] Multi-language support
- [ ] Dark mode theme
- [ ] Advanced filtering options
- [ ] History/saved summaries
- [ ] Export to multiple formats (PDF, DOCX)
- [ ] Integration with cloud storage (Google Drive, OneDrive)
- [ ] Browser extension
- [ ] Mobile app

---

## 📄 Changelog

### Version 1.0.0 (2024)
- Initial release
- Text summarization
- PDF support
- URL scraping
- Multiple summary types
- Tone selection
- Download functionality

---

## ⭐ Star & Fork

If you found this project helpful, please consider:
- ⭐ Starring the repository
- 🔀 Forking for your own use
- 📢 Sharing with others
- 🐛 Reporting issues

---

**Made with ❤️ for the community**

*Happy Summarizing! 🚀*
