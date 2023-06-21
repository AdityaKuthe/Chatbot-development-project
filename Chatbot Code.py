# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 09:00:34 2023

@author: HP
"""

import nltk
from nltk.chat.util import Chat, reflections
import time

current=time.ctime()
# Define the chatbot's rules
chatbot_rules = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ['I am good, thanks!', 'I am doing well!', 'I am fine.']),
    (r'quit', ['Bye!', 'Goodbye!', 'It was nice talking to you.']),
    (r'what time is it now',[current]),
    (r'What can you do',['I can provide you everything except physical activities']),
    (r'tell me a joke',['Sure Here is joke for you'
                        'Why dont skeletons fight each other?'
                        'They dont have the guts!']),
    (r'how old are you',['I am 20 years Old']),
    (r'what is weather like today?',['It is nice weather today']),
]

# Create a chatbot using the defined rules
chatbot = Chat(chatbot_rules, reflections)

# Start the conversation
print("Chatbot: Hi! How can I help you today?")
while True:
    user_input = input("User: ")
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
    else:
        print("Chatbot:", chatbot.respond(user_input))
