# AI Chat Log Summarizer

A Python-based tool to parse and summarize chat logs between a user and an AI. It provides message statistics, keyword analysis, and generates concise conversation summaries.

## 🚀 Features

- Parses `.txt` chat logs between User and AI.
- Counts total, user, and AI messages.
- Extracts most common keywords using:
  - Frequency-based method
  - (Optional) TF-IDF method
- Summarizes conversations.
- Supports summarizing multiple logs in a folder.
- Includes unit tests.

## 📁 Project Structure

```
AI_CHAT_SUMMARIZER/
│
├── chat_summarizer/
│   └── main.py
├── sample_chats/
│   └── (your .txt chat log files)
├── requirements.txt
└── README.md
```

## 🛠 Installation

```bash
# Clone the repo
$ git clone https://github.com/Zeshan793z/ai-chat-log-summarizer.git
$ cd ai-chat-log-summarizer

# Create a virtual environment
$ python -m venv venv
$ source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
$ pip install -r requirements.txt
```

## 📄 Requirements
```
nltk
scikit-learn
```


## ▶️ Usage

1. **Prepare your chat logs:**  
   Place `.txt` files in the `sample_chats` folder. Each line should start with `User:` or `AI:`.

2. **Run the summarizer:**
    ```sh
    python -m chat_summarizer.main sample_chats
    ```

    To use TF-IDF for keyword extraction:
    ```sh
    python -m chat_summarizer.main sample_chats --tfidf
    ```

## Example Chat Log

```
User: How do I install Python?
AI: You can download Python from the official website.
User: What is a virtual environment?
AI: A virtual environment is an isolated Python environment.
```

## Output Example

```
Summary for 'example.txt':
- The conversation had 4 exchanges.
- The user asked mainly about python, environment.
- Most common keywords: python, environment, install, virtual, official.
```

## 📌 Assumptions
- Chat files are properly formatted with "User:" and "AI:" prefixes.
- Each message appears on its own line.

## 📎 Notes
- No hardcoded values are used; all paths and settings are dynamic.
- Output is printed to console for simplicity.


## License

MIT License
