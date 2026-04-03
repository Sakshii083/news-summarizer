from transformers import pipeline

summarizer = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def ai_summarize(text):
    prompt = "Summarize this article: " + text
    result = summarizer(prompt, max_length=150)
    return result[0]['generated_text']