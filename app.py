"""
AI-Powered Content Summarizer Web Application
Built with Streamlit and Groq API
Author: Your Name
Created: 2024
"""

import streamlit as st
import os
from io import BytesIO
from dotenv import load_dotenv

# Import utility modules
from utils.summarizer import ContentSummarizer
from utils.pdf_reader import extract_text_from_pdf, get_pdf_page_count
from utils.web_scraper import scrape_url_content, is_valid_url
from utils.helpers import (
    count_words,
    count_characters,
    clean_text,
    format_for_download,
    get_summary_type_description,
    get_tone_description,
)

# Load environment variables
load_dotenv()

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="AI Content Summarizer",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .header-title {
        color: #1f77b4;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    
    /* Success message styling */
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Info box styling */
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Output container styling */
    .output-container {
        background-color: #f8f9fa;
        border-left: 4px solid #1f77b4;
        padding: 1.5rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    /* Statistics styling */
    .stats-container {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    
    .stat-box {
        background-color: #e7f3ff;
        padding: 1rem;
        border-radius: 5px;
        flex: 1;
        min-width: 150px;
    }
    
    /* Button styling */
    .button-group {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================

with st.sidebar:
    st.markdown("---")
    
    # Project Title and Info
    st.markdown("""
    # ✨ AI Content Summarizer
    
    **An intelligent content summarization tool powered by Groq AI**
    """)
    
    st.markdown("---")
    
    # Features Section
    st.markdown("### 📋 Features")
    features = [
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
    for feature in features:
        st.markdown(f"• {feature}")
    
    st.markdown("---")
    
    # Summary Types Info
    st.markdown("### 📚 Summary Types")
    st.markdown("""
    - **Short**: Quick 2-3 sentence overview
    - **Detailed**: Comprehensive analysis
    - **Bullet**: Key points in bullet format
    """)
    
    st.markdown("---")
    
    # Tone Options Info
    st.markdown("### 🎭 Tone Options")
    st.markdown("""
    - **Professional**: Formal business tone
    - **Simple**: Easy to understand
    - **Academic**: Scholarly tone
    - **Casual**: Friendly conversation
    """)
    
    st.markdown("---")
    
    # API Status
    st.markdown("### 🔌 API Status")
    try:
        summarizer = ContentSummarizer()
        if summarizer.check_api_status():
            st.success("✅ Groq API - Connected")
        else:
            st.error("❌ Groq API - Disconnected")
            st.warning("""
            **Troubleshooting:**
            1. Verify your GROQ_API_KEY in .env file
            2. Check your internet connection
            3. Visit https://console.groq.com/keys to verify API key is valid
            4. Ensure GROQ_MODEL is set correctly (mixtral-8x7b-32768 recommended)
            """)
    except ValueError as e:
        st.error(f"❌ Configuration Error: {str(e)}")
    except Exception as e:
        error_msg = str(e)
        st.error(f"❌ API Error: {error_msg[:100]}")
        if "authentication" in error_msg.lower() or "unauthorized" in error_msg.lower():
            st.warning("Invalid or expired API key. Please check your GROQ_API_KEY in .env")
        elif "connection" in error_msg.lower() or "timeout" in error_msg.lower():
            st.warning("Connection issue. Check your internet and try again.")
    
    st.markdown("---")
    
    # Developer Info
    st.markdown("### 👨‍💻 Developer Info")
    st.markdown("""
    Built with ❤️ using:
    - **Streamlit** - Web Framework
    - **Groq API** - AI Model
    - **Python** - Backend
    
    Perfect for:
    - 🎓 College Projects
    - 📋 Resume Projects
    - 🚀 Internship Showcases
    """)
    
    st.markdown("---")
    
    # Instructions
    st.markdown("### 📖 How to Use")
    st.markdown("""
    1. Select a tab (Text, File, or URL)
    2. Enter or upload your content
    3. Choose summary type & tone
    4. Click "Generate Summary"
    5. Copy or download the result!
    """)
    
    st.markdown("---")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; color: #888; font-size: 0.85rem; margin-top: 2rem;">
    <p>Made with Streamlit & Groq API</p>
    <p>© 2024 AI Content Summarizer</p>
    </div>
    """, unsafe_allow_html=True)


# ============================================================================
# MAIN HEADER
# ============================================================================

st.markdown("""
<div class="header-title">✨ AI Content Summarizer</div>
<div class="header-subtitle">
Transform your content into concise, intelligent summaries powered by advanced AI
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# TABS INTERFACE
# ============================================================================

tab1, tab2, tab3 = st.tabs(["📝 Text Summarizer", "📄 File Summarizer", "🌐 URL Summarizer"])


# ============================================================================
# TAB 1: TEXT SUMMARIZER
# ============================================================================

with tab1:
    st.markdown("### 📝 Summarize Plain Text")
    st.markdown("Paste your text below to generate a summary.")
    
    # Input area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        text_input = st.text_area(
            label="Enter text to summarize",
            height=250,
            placeholder="Paste your text here...",
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown("### ⚙️ Options")
        summary_type_1 = st.selectbox(
            "Summary Type",
            ["short", "detailed", "bullet"],
            format_func=get_summary_type_description,
            key="text_summary_type"
        )
        
        tone_1 = st.selectbox(
            "Tone",
            ["professional", "simple", "academic", "casual"],
            format_func=get_tone_description,
            key="text_tone"
        )
    
    # Buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        generate_btn_1 = st.button(
            "🚀 Generate Summary",
            key="text_generate",
            use_container_width=True,
            type="primary"
        )
    
    with col2:
        clear_btn_1 = st.button(
            "🔄 Clear",
            key="text_clear",
            use_container_width=True
        )
    
    with col3:
        info_btn_1 = st.button(
            "ℹ️ Info",
            key="text_info",
            use_container_width=True
        )
    
    # Handle clear button
    if clear_btn_1:
        st.rerun()
    
    # Handle info button
    if info_btn_1:
        st.info("""
        **How to use:**
        1. Paste your text in the text area
        2. Select your preferred summary type and tone
        3. Click 'Generate Summary'
        4. Use the action buttons to copy or download
        """)
    
    # Generate summary
    if generate_btn_1:
        if not text_input or not text_input.strip():
            st.error("❌ Please enter some text to summarize.")
        else:
            try:
                with st.spinner("🔄 Generating summary..."):
                    # Initialize summarizer
                    summarizer = ContentSummarizer()
                    
                    # Generate summary
                    summary = summarizer.generate_summary(
                        text=text_input,
                        summary_type=summary_type_1,
                        tone=tone_1
                    )
                    
                    # Store in session state for download
                    st.session_state.last_summary_text = summary
                    st.session_state.last_input_text = text_input
                
                # Display success message
                st.success("✅ Summary generated successfully!")
                
                # Display summary
                st.markdown("### 📋 Generated Summary")
                st.markdown(f"""
                <div class="output-container">
                {summary}
                </div>
                """, unsafe_allow_html=True)
                
                # Display statistics
                input_words = count_words(text_input)
                output_words = count_words(summary)
                compression_ratio = round((1 - output_words / input_words) * 100, 1) if input_words > 0 else 0
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Input Words", f"{input_words:,}")
                with col2:
                    st.metric("Summary Words", f"{output_words:,}")
                with col3:
                    st.metric("Compression", f"{compression_ratio}%")
                with col4:
                    st.metric("Characters", f"{count_characters(summary):,}")
                
                # Action buttons
                st.markdown("### 💾 Actions")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("")  # Spacing
                    # Copy to clipboard button
                    st.button(
                        "📋 Copy Summary",
                        key="text_copy",
                        help="Copy summary to clipboard",
                        use_container_width=True
                    )
                
                with col2:
                    # Download button
                    download_text = format_for_download(
                        "Text Summary",
                        summary,
                        metadata={
                            "Type": get_summary_type_description(summary_type_1),
                            "Tone": get_tone_description(tone_1),
                            "Input Words": input_words,
                            "Output Words": output_words,
                        }
                    )
                    
                    st.download_button(
                        label="⬇️ Download as TXT",
                        data=download_text,
                        file_name="summary.txt",
                        mime="text/plain",
                        key="text_download",
                        use_container_width=True
                    )
                
                with col3:
                    st.write("")  # Spacing
                    st.button(
                        "📧 Share",
                        key="text_share",
                        help="Share summary",
                        use_container_width=True
                    )
            
            except ValueError as e:
                st.error(f"❌ Input Error: {str(e)}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("Please check your Groq API key and internet connection.")


# ============================================================================
# TAB 2: FILE SUMMARIZER
# ============================================================================

with tab2:
    st.markdown("### 📄 Summarize Files")
    st.markdown("Upload a PDF or TXT file to generate a summary.")
    
    # File uploader
    uploaded_file = st.file_uploader(
        label="Choose a file",
        type=["pdf", "txt"],
        label_visibility="collapsed"
    )
    
    if uploaded_file:
        file_type = uploaded_file.type
        file_name = uploaded_file.name
        
        # Display file info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📋 File Name", file_name[:30] + "..." if len(file_name) > 30 else file_name)
        with col2:
            st.metric("📊 File Size", f"{uploaded_file.size / 1024:.1f} KB")
        with col3:
            st.metric("📝 Type", "PDF" if "pdf" in file_type else "Text")
        
        # Options
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Options")
            preview = st.checkbox(
                "Preview file content (first 500 chars)",
                value=False,
                key="file_preview"
            )
        
        with col2:
            st.markdown("### ⚙️ Settings")
            summary_type_2 = st.selectbox(
                "Summary Type",
                ["short", "detailed", "bullet"],
                format_func=get_summary_type_description,
                key="file_summary_type"
            )
            
            tone_2 = st.selectbox(
                "Tone",
                ["professional", "simple", "academic", "casual"],
                format_func=get_tone_description,
                key="file_tone"
            )
        
        # Preview content
        if preview:
            try:
                if "pdf" in file_type:
                    text_content = extract_text_from_pdf(uploaded_file)
                    page_count = get_pdf_page_count(uploaded_file)
                    st.info(f"📖 PDF has {page_count} pages")
                else:
                    text_content = uploaded_file.read().decode("utf-8")
                
                # Show preview
                preview_text = text_content[:500] + "..." if len(text_content) > 500 else text_content
                st.markdown("#### Preview")
                st.code(preview_text, language="text")
            
            except Exception as e:
                st.error(f"❌ Error reading file: {str(e)}")
        
        # Buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            generate_btn_2 = st.button(
                "🚀 Generate Summary",
                key="file_generate",
                use_container_width=True,
                type="primary"
            )
        
        with col2:
            clear_btn_2 = st.button(
                "🔄 Clear",
                key="file_clear",
                use_container_width=True
            )
        
        with col3:
            info_btn_2 = st.button(
                "ℹ️ Info",
                key="file_info",
                use_container_width=True
            )
        
        if clear_btn_2:
            st.rerun()
        
        if info_btn_2:
            st.info("""
            **Supported formats:**
            - **PDF**: Any PDF document (multi-page supported)
            - **TXT**: Plain text files (UTF-8 encoded)
            
            **Tips:**
            - Larger files may take longer to process
            - Use Preview to check content before summarizing
            """)
        
        # Generate summary
        if generate_btn_2:
            try:
                with st.spinner("📖 Reading file..."):
                    if "pdf" in file_type:
                        text_content = extract_text_from_pdf(uploaded_file)
                    else:
                        text_content = uploaded_file.read().decode("utf-8")
                
                # Clean the text
                text_content = clean_text(text_content)
                
                if not text_content or not text_content.strip():
                    st.error("❌ No readable content found in the file.")
                else:
                    with st.spinner("🔄 Generating summary..."):
                        summarizer = ContentSummarizer()
                        summary = summarizer.generate_summary(
                            text=text_content,
                            summary_type=summary_type_2,
                            tone=tone_2
                        )
                        st.session_state.last_summary_file = summary
                        st.session_state.last_input_file = text_content
                    
                    st.success("✅ Summary generated successfully!")
                    
                    # Display summary
                    st.markdown("### 📋 Generated Summary")
                    st.markdown(f"""
                    <div class="output-container">
                    {summary}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display statistics
                    input_words = count_words(text_content)
                    output_words = count_words(summary)
                    compression_ratio = round((1 - output_words / input_words) * 100, 1) if input_words > 0 else 0
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Input Words", f"{input_words:,}")
                    with col2:
                        st.metric("Summary Words", f"{output_words:,}")
                    with col3:
                        st.metric("Compression", f"{compression_ratio}%")
                    with col4:
                        st.metric("Characters", f"{count_characters(summary):,}")
                    
                    # Action buttons
                    st.markdown("### 💾 Actions")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.button(
                            "📋 Copy Summary",
                            key="file_copy",
                            help="Copy to clipboard",
                            use_container_width=True
                        )
                    
                    with col2:
                        download_text = format_for_download(
                            f"File Summary - {file_name}",
                            summary,
                            metadata={
                                "Original File": file_name,
                                "Type": get_summary_type_description(summary_type_2),
                                "Tone": get_tone_description(tone_2),
                                "Input Words": input_words,
                                "Output Words": output_words,
                            }
                        )
                        
                        st.download_button(
                            label="⬇️ Download as TXT",
                            data=download_text,
                            file_name=f"summary_{file_name.split('.')[0]}.txt",
                            mime="text/plain",
                            key="file_download",
                            use_container_width=True
                        )
                    
                    with col3:
                        st.button(
                            "📧 Share",
                            key="file_share",
                            help="Share summary",
                            use_container_width=True
                        )
            
            except ValueError as e:
                st.error(f"❌ File Error: {str(e)}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("Please ensure the file is valid and try again.")


# ============================================================================
# TAB 3: URL SUMMARIZER
# ============================================================================

with tab3:
    st.markdown("### 🌐 Summarize Website Content")
    st.markdown("Enter a URL to scrape and summarize web content.")
    
    # URL input
    url_input = st.text_input(
        label="Enter URL",
        placeholder="https://example.com or example.com",
        label_visibility="collapsed"
    )
    
    if url_input:
        # Options
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Options")
            preview = st.checkbox(
                "Preview webpage content (first 500 chars)",
                value=False,
                key="url_preview"
            )
        
        with col2:
            st.markdown("### ⚙️ Settings")
            summary_type_3 = st.selectbox(
                "Summary Type",
                ["short", "detailed", "bullet"],
                format_func=get_summary_type_description,
                key="url_summary_type"
            )
            
            tone_3 = st.selectbox(
                "Tone",
                ["professional", "simple", "academic", "casual"],
                format_func=get_tone_description,
                key="url_tone"
            )
        
        # Preview content
        if preview:
            try:
                with st.spinner("🔗 Fetching webpage..."):
                    web_content = scrape_url_content(url_input)
                    preview_text = web_content[:500] + "..." if len(web_content) > 500 else web_content
                    
                st.markdown("#### Preview")
                st.code(preview_text, language="text")
            
            except Exception as e:
                st.error(f"❌ Error fetching URL: {str(e)}")
        
        # Buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            generate_btn_3 = st.button(
                "🚀 Generate Summary",
                key="url_generate",
                use_container_width=True,
                type="primary"
            )
        
        with col2:
            clear_btn_3 = st.button(
                "🔄 Clear",
                key="url_clear",
                use_container_width=True
            )
        
        with col3:
            info_btn_3 = st.button(
                "ℹ️ Info",
                key="url_info",
                use_container_width=True
            )
        
        if clear_btn_3:
            st.rerun()
        
        if info_btn_3:
            st.info("""
            **How to use:**
            1. Paste or type a website URL
            2. Optionally preview the content
            3. Choose summary type and tone
            4. Click Generate Summary
            
            **Tips:**
            - Works with most websites
            - JavaScript content may not be captured
            - Large pages take longer to process
            """)
        
        # Generate summary
        if generate_btn_3:
            if not is_valid_url(url_input):
                st.error("❌ Invalid URL format. Please enter a valid website URL.")
            else:
                try:
                    with st.spinner("🔗 Fetching webpage..."):
                        web_content = scrape_url_content(url_input)
                    
                    # Clean the text
                    web_content = clean_text(web_content)
                    
                    if not web_content or not web_content.strip():
                        st.error("❌ No content could be extracted from the URL.")
                    else:
                        with st.spinner("🔄 Generating summary..."):
                            summarizer = ContentSummarizer()
                            summary = summarizer.generate_summary(
                                text=web_content,
                                summary_type=summary_type_3,
                                tone=tone_3
                            )
                            st.session_state.last_summary_url = summary
                            st.session_state.last_input_url = web_content
                        
                        st.success("✅ Summary generated successfully!")
                        
                        # Display URL info
                        st.info(f"📍 Source: [{url_input}]({url_input})")
                        
                        # Display summary
                        st.markdown("### 📋 Generated Summary")
                        st.markdown(f"""
                        <div class="output-container">
                        {summary}
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Display statistics
                        input_words = count_words(web_content)
                        output_words = count_words(summary)
                        compression_ratio = round((1 - output_words / input_words) * 100, 1) if input_words > 0 else 0
                        
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Input Words", f"{input_words:,}")
                        with col2:
                            st.metric("Summary Words", f"{output_words:,}")
                        with col3:
                            st.metric("Compression", f"{compression_ratio}%")
                        with col4:
                            st.metric("Characters", f"{count_characters(summary):,}")
                        
                        # Action buttons
                        st.markdown("### 💾 Actions")
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.button(
                                "📋 Copy Summary",
                                key="url_copy",
                                help="Copy to clipboard",
                                use_container_width=True
                            )
                        
                        with col2:
                            download_text = format_for_download(
                                f"URL Summary - {url_input}",
                                summary,
                                metadata={
                                    "Source URL": url_input,
                                    "Type": get_summary_type_description(summary_type_3),
                                    "Tone": get_tone_description(tone_3),
                                    "Input Words": input_words,
                                    "Output Words": output_words,
                                }
                            )
                            
                            st.download_button(
                                label="⬇️ Download as TXT",
                                data=download_text,
                                file_name="summary_url.txt",
                                mime="text/plain",
                                key="url_download",
                                use_container_width=True
                            )
                        
                        with col3:
                            st.button(
                                "📧 Share",
                                key="url_share",
                                help="Share summary",
                                use_container_width=True
                            )
                
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.info("Please check the URL and try again.")
    
    else:
        st.info("""
        👆 **Enter a URL above to get started!**
        
        Examples:
        - https://wikipedia.org/wiki/Artificial_Intelligence
        - https://news.ycombinator.com
        - https://medium.com
        """)


# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.85rem; margin-top: 2rem; margin-bottom: 1rem;">
<p>🚀 <strong>AI Content Summarizer</strong> | Powered by Streamlit & Groq API</p>
<p>Made with ❤️ for students, professionals, and content creators</p>
<p>© 2024 - All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)
