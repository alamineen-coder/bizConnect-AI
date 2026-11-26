import streamlit as st
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="BizConnect AI", page_icon="💬")
st.title("💬 BizConnect AI – Multilingual Support Chatbot")
st.caption("Supports English, বাংলা (Bengali) & 한국어 (Korean) | TF-IDF + Sentiment + HITL")

df = pd.read_csv("business_faq.csv")
vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4))
tfidf_matrix = vectorizer.fit_transform(df["Question"])

neg_words = {
    "angry", "bad", "worst", "delay", "late", "broken", "frustrated", "upset", "terrible", "poor", "issue", "problem", "cancel", "refund",
    "রাগ", "খারাপ", "দেরি", "ভাঙা", "নষ্ট", "বিরক্ত", "সমস্যা", "বাতিল", "ফেরত", "বাজে", "অভিযোগ",
    "화나", "짜증", "늦어", "지연", "고장", "불만", "문제", "취소", "환불", "최악", "별로"
}

pos_words = {
    "good", "great", "fast", "thanks", "thank", "love", "amazing", "excellent", "helpful", "nice",
    "ভালো", "ধন্যবাদ", "দ্রুত", "দারুণ", "চমৎকার", "সাহায্য", "খুশি",
    "좋아", "감사", "빠르", "최고", "친절", "훌륭", "고마워"
}

def detect_language(text):
    if re.search(r"[\u0980-\u09FF]", text):
        return "bn"
    elif re.search(r"[\uAC00-\uD7AF]", text):
        return "ko"
    return "en"

def get_response(user_query):
    lang = detect_language(user_query)
    q_lower = user_query.lower()

    is_neg = any(word in q_lower for word in neg_words)
    is_pos = any(word in q_lower for word in pos_words)

    if is_neg:
        sentiment = "Negative (Frustrated/Angry)"
    elif is_pos:
        sentiment = "Positive"
    else:
        sentiment = "Neutral"

    query_vec = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    best_idx = similarities.argmax()
    conf = similarities[best_idx]

    if conf < 0.22:
        fallback_msg = {
            "bn": "দুঃখিত, এই বিষয়ে আমার কাছে নিশ্চিত তথ্য নেই। আপনার প্রশ্নটি একজন হিউম্যান এজেন্টের রিভিউয়ের জন্য পাঠানো হয়েছে।",
            "ko": "죄송합니다. 해당 내용에 대한 정확한 정보가 없습니다. 상담원 연결을 위해 질문을 전달했습니다.",
            "en": "I am not completely sure about that. I have flagged your query for a Human Review agent."
        }
        return fallback_msg[lang], round(float(conf) * 100, 1), sentiment, True

    elif "Negative" in sentiment:
        empathy_note = {
            "bn": "\n\n*(নোট: মনে হচ্ছে আপনি কিছুটা বিরক্ত। আমি কি আপনাকে সরাসরি একজন হিউম্যান এজেন্টের সাথে যুক্ত করে দেব?)*",
            "ko": "\n\n*(참고: 불편을 겪으신 것 같습니다. 바로 전문 상담원과 연결해 드릴까요?)*",
            "en": "\n\n*(Note: I noticed you seem upset. Would you like me to connect you to a human agent?)*"
        }
        return df["Answer"].iloc[best_idx] + empathy_note[lang], round(float(conf) * 100, 1), sentiment, True

    else:
        return df["Answer"].iloc[best_idx], round(float(conf) * 100, 1), sentiment, False

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask in English, বাংলা, or 한국어..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply, conf, sent, human = get_response(prompt)
    out = f"{reply}\n\n---\n*Confidence: {conf}% | Sentiment: {sent} | Human Review Flag: {human}*"
    st.session_state.messages.append({"role": "assistant", "content": out})
    with st.chat_message("assistant"):
        st.markdown(out)
