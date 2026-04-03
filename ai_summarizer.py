from transformers import pipeline

# load model once
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def ai_summarize(text):
    result = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return result[0]['summary_text']