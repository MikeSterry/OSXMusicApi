import json

from models.MarqueeMessage import MarqueeMessage


class MarqueeMessages:
    def __init__(self):
        self.messages = []

    def __repr__(self):
        return json.dumps(self.__dict__)

    def add_message(self, message: MarqueeMessage):
        """
        Adds a message to the list of messages
        :param message: The message to add
        """
        self.messages.append(message)
        return self.messages

    def get_messages(self):
        """
        Returns the list of messages
        :return: The list of messages
        """
        return self.messages
    
    def get_body(self):
        """
        Returns the list of messages
        :return: The list of messages
        """
        return {
            "messages": self.messages
        }