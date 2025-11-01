from transformers import pipeline

# BART 모델 기반 요약
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, chunk_size=1000):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)
        summaries.append(summary[0]['summary_text'])
    return "\n".join(summaries)
