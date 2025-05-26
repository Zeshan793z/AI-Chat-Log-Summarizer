import os
import re
import string
from collections import Counter, defaultdict
from typing import List, Tuple, Dict

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure nltk stopwords are available
nltk.download('stopwords')
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))


def parse_chat(file_path: str) -> Tuple[List[str], List[str]]:
    """Parses a chat log into user and AI messages."""
    user_msgs, ai_msgs = [], []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith("User:"):
                user_msgs.append(line[5:].strip())
            elif line.startswith("AI:"):
                ai_msgs.append(line[3:].strip())
    return user_msgs, ai_msgs


def count_messages(user_msgs: List[str], ai_msgs: List[str]) -> Dict[str, int]:
    return {
        "total": len(user_msgs) + len(ai_msgs),
        "user": len(user_msgs),
        "ai": len(ai_msgs)
    }


def extract_keywords_freq(messages: List[str], top_k=5) -> List[str]:
    words = re.findall(r"\b\w+\b", ' '.join(messages).lower())
    filtered = [w for w in words if w not in STOP_WORDS and w not in string.punctuation]
    counter = Counter(filtered)
    return [word for word, _ in counter.most_common(top_k)]


def extract_keywords_tfidf(messages: List[str], top_k=5) -> List[str]:
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(messages)
    scores = X.sum(axis=0).A1
    vocab = vectorizer.get_feature_names_out()
    keyword_scores = list(zip(vocab, scores))
    keyword_scores.sort(key=lambda x: x[1], reverse=True)
    return [kw for kw, _ in keyword_scores[:top_k]]


def generate_summary(file_path: str, use_tfidf=False) -> str:
    user_msgs, ai_msgs = parse_chat(file_path)
    stats = count_messages(user_msgs, ai_msgs)
    combined_msgs = user_msgs + ai_msgs
    keywords = extract_keywords_tfidf(combined_msgs) if use_tfidf else extract_keywords_freq(combined_msgs)
    topic = ", ".join(keywords[:2]) if keywords else "general topics"

    summary = (
        f"Summary for '{os.path.basename(file_path)}':\n"
        f"- The conversation had {stats['total']} exchanges.\n"
        f"- The user asked mainly about {topic}.\n"
        f"- Most common keywords: {', '.join(keywords)}.\n"
    )
    return summary


def summarize_folder(folder_path: str, use_tfidf=False):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            print(generate_summary(file_path, use_tfidf))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Summarize chat logs.")
    parser.add_argument("folder", help="Path to folder containing chat logs")
    parser.add_argument("--tfidf", action="store_true", help="Use TF-IDF for keyword extraction")
    args = parser.parse_args()
    summarize_folder(args.folder, args.tfidf)
