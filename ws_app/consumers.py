from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # There are client-side improvements to the back-end websocket Automatically triggered on request
        # The server allows the execution of downlink code , If not allowed, you can use raise StopConsumner() Reject the client's connection request
        self.accept()
    def websocket_receive(self, message):
        # Triggered when the client sends data ,message It is the data sent by the client （ A dictionary ）
        print(message)
        self.send(" Server side content ")# Send data to client
    def websocket_disconnect(self, message):
        # Triggered when disconnected
        raise StopConsumer()