import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text):
    return summarizer(text, max_length=200, min_length=10, do_sample=True)[0]['summary_text']

iface = gr.Interface(fn=summarize, inputs="text", outputs="text", title="Text Summarizer")
iface.launch(share =True)
