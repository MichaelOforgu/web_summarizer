# 🌐 Web Summarizer - Beginner's Guide

This project creates a web application that can summarize any website's content using AI. It's perfect for beginners who want to learn about web scraping, AI integration, and building web interfaces.

## 🎯 What This Project Does

- Takes a website URL as input
- Extracts the main content from the website
- Uses OpenAI's GPT-4 to generate a concise summary
- Presents the summary in a beautiful web interface

## 🚀 Step-by-Step Setup Guide

### 1. Prerequisites
Before you start, make sure you have:
- Python 3.8 or higher installed
- A code editor (like VS Code or PyCharm)
- An OpenAI API key (get one at https://platform.openai.com)

### 2. Clone and Setup
```bash
# Create a new directory for your project
mkdir web_summarizer
cd web_summarizer

# Clone this repository (if using git)
git clone <repository-url> .
```

### 3. Create a Virtual Environment
A virtual environment keeps your project's dependencies isolated from other Python projects.

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt
```

### 5. Set Up Your API Key
1. Create a new file named `.env` in the project root
2. Add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## 🏗️ Project Structure Explained

```
web_summarizer/
├── src/                    # Source code directory
│   ├── __init__.py        # Makes the directory a Python package
│   ├── summarizer.py      # Core functionality for website scraping and summarization
│   └── interface.py       # Gradio web interface
├── requirements.txt        # Project dependencies
├── README.md              # This file
└── .env                   # Your API keys (not in git)
```

## 🚀 Running the Application

1. Make sure your virtual environment is activated
2. Run the application:
```bash
python src/interface.py
```
3. Open your browser and go to: http://127.0.0.1:7860

## 💡 How to Use

1. Enter a website URL in the input box (e.g., "cnn.com")
2. Click "Generate Summary" or press Enter
3. Wait for the AI to process the website
4. Read the generated summary!

## 🔍 Understanding the Code

### Key Components:

1. **Website Scraping** (`summarizer.py`):
   - Uses `BeautifulSoup` to extract content from websites
   - Removes unnecessary elements like scripts and styles
   - Cleans and formats the text

2. **AI Integration** (`summarizer.py`):
   - Uses OpenAI's GPT-4 model
   - Sends the website content to the AI
   - Receives and formats the summary

3. **Web Interface** (`interface.py`):
   - Built with Gradio
   - Provides a user-friendly input form
   - Displays the summary in a clean format

## 🛠️ Troubleshooting

Common issues and solutions:

1. **API Key Not Working**
   - Check if your `.env` file exists
   - Verify the API key is correct
   - Make sure there are no spaces in the API key

2. **Website Not Loading**
   - Check your internet connection
   - Verify the URL is correct
   - Some websites might block scraping

3. **Module Not Found Errors**
   - Make sure your virtual environment is activated
   - Try running `pip install -r requirements.txt` again

## 📚 Learning Resources

- [Python Documentation](https://docs.python.org/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [OpenAI API Documentation](https://platform.openai.com/docs/api-reference)
- [Gradio Documentation](https://gradio.app/docs/)