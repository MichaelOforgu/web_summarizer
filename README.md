# Web Summarizer

A web application that summarizes website content using OpenAI's GPT-4 model and presents it through a beautiful Gradio interface.

## Features

- Extract and clean website content
- Generate concise summaries using OpenAI's GPT-4
- Beautiful and intuitive Gradio interface
- Environment variable support for API keys

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

Run the application:
```bash
python src/interface.py
```

Then open your browser to the URL shown in the terminal (typically http://127.0.0.1:7860)

## Project Structure

```
web_summarizer/
├── src/
│   ├── __init__.py
│   ├── summarizer.py
│   └── interface.py
├── requirements.txt
├── README.md
└── .env
``` 