from simple_websocket_server import WebSocketServer, WebSocket
from ChatBot import get_response

class ChatServer(WebSocket):

    def handleMessage(self):
        message = self.data
        response = get_response(message)
        self.sendMessage(response)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')



server = WebSocketServer('', 8000, ChatServer)
server.serve_forever()