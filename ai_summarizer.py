from transformers import pipeline

def ai_summarize(text):
    summarizer = pipeline(
        task="summarization",
        model="facebook/bart-large-cnn"
    )
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]['summary_text']