import gradio as gr
from summarizer import summarize

def process_url(url):
    """
    Process the URL and return the summary
    """
    if not url:
        return "Please enter a URL"
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    return summarize(url)

# Create the Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🌐 Web Summarizer
    Enter a URL below to get an AI-generated summary of the website's content.
    """)
    
    with gr.Row():
        with gr.Column(scale=4):
            url_input = gr.Textbox(
                label="Website URL",
                placeholder="Enter a URL (e.g., cnn.com)",
                lines=1
            )
            submit_btn = gr.Button("Generate Summary", variant="primary")
        
    with gr.Row():
        with gr.Column():
            output = gr.Markdown(label="Summary")
    
    # Set up the event handlers
    submit_btn.click(
        fn=process_url,
        inputs=url_input,
        outputs=output
    )
    
    url_input.submit(
        fn=process_url,
        inputs=url_input,
        outputs=output
    )

if __name__ == "__main__":
    demo.launch() 