import os
from chatterbot import ChatBot #this imports chatbot
from chatterbot.trainers import ListTrainer #for training the ChatBot

def setup():
    chatbot = ChatBot('MyChatBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    conversation = open('conversation.txt','r').readlines()
    chatbot.set_trainer(ListTrainer)
    chatbot.train(conversation)

setup()