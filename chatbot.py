import nltk
from nltk.chat.util import Chat, reflections

# Sample conversation pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created by my master rapholic."]
    ],
    [
        r"how are you ?",
        ["I'm good, thank you!", "Doing well! How can I assist you?"]
    ],
    [
        r"what can you do ?",
        ["I can answer simple questions. Try asking about my name or how I am."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "See you later!", "Bye! Have a nice day."]
    ]
]

chatbot = Chat(pairs, reflections)
print("🤖 Chatbot: Hi! Type 'bye' to exit.")
chatbot.converse()