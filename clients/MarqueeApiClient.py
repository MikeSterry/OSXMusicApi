import json
from configparser import ConfigParser

import requests
from requests import Response

from models.MarqueeMessage import MarqueeMessage
from models.MarqueeMessages import MarqueeMessages


class MarqueeApiClient:
    def __init__(self, config_file='config.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)
        self.base_url = self.config.get('MarqueeApi', 'base_url')

    """
        Gets the current marquee messages from the marquee
        :return: The current marquee messages
    """
    def get_current_marquee_messages(self) -> MarqueeMessages:
        url = f"http://{self.base_url}/messages"
        print(f"Using URL: {url}")
        headers = self._create_request_headers()
        response = requests.get(url, headers=headers)
        print(f"response: {response.json}")
        return self._unpack_response(response.json)

    """
        Clears the current messages from the marquee
        :return: The response from the API
    """
    def clear_marquee_messages(self):
        url = f"http://{self.base_url}/_clear_db"
        requests.post(url)

    """
        Adds a new marquee message to the marquee
        :return: The response from the API
    """
    def add_new_marquee_message(self, artist, songTitle) -> MarqueeMessages:
        url = f"http://{self.base_url}/messages"
        headers = self._create_request_headers()

        marquee_messsage_text = MarqueeMessage().create_marquee_message_from_artist_and_song_title(artist, songTitle)
        marquee_message = MarqueeMessage(str(marquee_messsage_text))
        response = requests.post(url, headers=headers, data=marquee_message.get_marquee_message())
        print(f"response: {response}")
        return self._unpack_response(response)

    """
        Creates the request headers for the API
        :return: The request headers
    """
    def _create_request_headers(self) -> dict:
        """
        Creates the request headers for the API
        :return: The request headers
        """
        headers = {
            'Content-Type': 'application/json'
        }
        return headers
    
    def _unpack_response(self, response) -> MarqueeMessages:
        """
        Unpacks the response from the API
        :param response: The response from the API
        :return: MarqueeMessages
        """
        marquee_messages = MarqueeMessages(**response)
        return marquee_messages