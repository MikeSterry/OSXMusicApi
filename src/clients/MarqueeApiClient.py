
import json
import logging
from configparser import ConfigParser

import requests
from requests import Response, RequestException

from src.models.MarqueeMessage import MarqueeMessage
from src.models.MarqueeMessages import MarqueeMessages

logging.basicConfig(level=logging.INFO)

class MarqueeApiClient:
    def __init__(self, config_file: str = 'config.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)
        self.base_url = self.config.get('MarqueeApi', 'base_url')

    def get_current_marquee_messages(self) -> MarqueeMessages:
        url = self._build_url("/messages")
        logging.info(f"Fetching messages from URL: {url}")
        headers = self._create_request_headers()

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return self._unpack_response(response.json())
        except RequestException as e:
            logging.error(f"Failed to fetch marquee messages: {e}")
            return MarqueeMessages()

    def clear_marquee_messages(self) -> None:
        url = self._build_url("/_clear_db")
        logging.info("Clearing marquee messages.")
        try:
            response = requests.post(url)
            response.raise_for_status()
        except RequestException as e:
            logging.error(f"Failed to clear messages: {e}")

    def add_new_marquee_message(self, artist: str, song_title: str) -> MarqueeMessages:
        url = self._build_url("/messages")
        headers = self._create_request_headers()
        message_text = MarqueeMessage().create_marquee_message_from_artist_and_song_title(artist, song_title)
        message_json = json.dumps(message_text)

        try:
            response = requests.post(url, headers=headers, data=message_json)
            response.raise_for_status()
            return self._unpack_response(response.json())
            # return None # Assuming the response is a single message
        except RequestException as e:
            logging.error(f"Failed to add new message: {e}")
            return MarqueeMessages()

    def _create_request_headers(self) -> dict:
        return {
            "Content-Type": "application/json"
        }

    def _build_url(self, path: str) -> str:
        return f"http://{self.base_url}/{path.lstrip('/')}"

    def _unpack_response(self, json_messages) -> MarqueeMessages:
        # Assuming response_data is a list of messages; adjust as needed.
        messages = MarqueeMessages()
        try:
            # json_messages = json.dumps(response_data)
            for json_message in json_messages['messages']:
                message = MarqueeMessage()
                message_color = json_message['color']
                message_font = json_message['font']
                message_mode = json_message['mode']
                message_text = json_message['text']
                message.set_marquee_message(message_text, message_color, message_font, message_mode)
                messages.add_message(message)
        except Exception as e:
            logging.error(f"Error unpacking Marquee API response: {e}")
            return messages

        return messages
