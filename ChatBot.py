from chatterbot import ChatBot #this imports chatbot
from chatterbot.trainers import ListTrainer #for training the ChatBot

##cahtbot = ChatBot("MyChatBot")
##chatbot.set_trainer(ListTrainer)
##conversation = open('conversation.txt','r').readlines()
##chatbot.train(conversation)

def get_response(usrInput):
    chatbot = ChatBot("MyChatBot",storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.75,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip() != 'Bye':
            result = bot.get_response(usrInput)
            reply = str(result)
            return (reply)
        if usrText.strip() == 'Bye':
            return ('Bye')
            break
