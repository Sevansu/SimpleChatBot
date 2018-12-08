# SimpleChatBot

## Description of files
* ChatBotTrainer.py file trains the data of conversation.txt. Once it is trained , the result will be stored as db.sqlite3.
* ChatBot.py uses this db.sqlite3 to generate responses for user queries.
* server.py sends back message to the client.

## How to run
* install the python packages.
  Required pakages:
   (1)ChatterBot-0.8.4
   (2)simple-websocket-server
  
  use pip3(for python 3.x) or pip(for python 2.x) 
  
  -->pip3 install ChatterBot
  
  -->pip3 install simple-websocket-server
* Run python server.py.
* Right click the index.html page and open with brower. In chat window you can start the chat.
