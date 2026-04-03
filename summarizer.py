import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

def summarize(text, num_sentences=3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    word_freq = Counter(
        w for w in words if w.isalnum() and w not in stop_words
    )

    sentences = sent_tokenize(text)
    sentence_scores = {}

    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]

    summary_sentences = sorted(
        sentence_scores, key=sentence_scores.get, reverse=True
    )[:num_sentences]

    return " ".join(summary_sentences)

def extract_keywords(text, num_keywords=5):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())

    keywords = [
        w for w in words if w.isalnum() and w not in stop_words
    ]

    freq = Counter(keywords)
    return [word for word, _ in freq.most_common(num_keywords)]
