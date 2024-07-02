import nltk
from chatbot.responses import get_response

def get_bot_response(user_message):
    response = get_response(user_message)
    return response
