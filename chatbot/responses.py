import random

def get_response(user_message):
    responses = [
        "I'm here to listen.",
        "Tell me more about how you're feeling.",
        "It's okay to feel this way.",
        "How can I help you today?",
        "Let's try a guided meditation. Close your eyes and take a deep breath."
    ]
    return random.choice(responses)
