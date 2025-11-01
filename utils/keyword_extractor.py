from keybert import KeyBERT
from wordcloud import WordCloud
from io import BytesIO

kw_model = KeyBERT()

def extract_keywords(text, top_n=20):
    keywords = kw_model.extract_keywords(text, top_n=top_n)
    return [kw[0] for kw in keywords]

def make_wordcloud(keywords):
    wc = WordCloud(width=800, height=400, background_color="white").generate(" ".join(keywords))
    buf = BytesIO()
    wc.to_image().save(buf, format="PNG")
    return buf.getvalue()
