#!/usr/bin/env python3

import logging
import time

from clients.AppleMusicClient import AppleMusicClient
from clients.MarqueeApiClient import MarqueeApiClient
from models.AppleMusicNowPlayingMetadata import AppleMusicNowPlayingMetadata
from models.MarqueeMessages import MarqueeMessages

"""
    Main function to update the marquee messages based on the current playing song
    from OSX's Audio Framework; which can be any audio playing - Music, YouTube, etc....
    It checks the current playing song every 5 seconds and updates the marquee
    message if the song has changed.
    :return: None
"""
def main():
    logging.basicConfig(level=logging.INFO)
    while True:
        logging.info("Getting current playing song...")
        currently_playing = _get_current_playing_song()

        if currently_playing.get_currently_playing_status() == 1:
            artist = currently_playing.get_currently_playing_artist()
            title = currently_playing.get_currently_playing_title()

            logging.info("Getting current messages...")
            current_marquee_artist, current_marquee_title = _get_current_marquee_artist_and_song_title()

            if current_marquee_artist != artist or current_marquee_title != title:
                logging.info("Current marquee message is different from the current playing song. Updating marquee message...")

                logging.info("Clearing current messages...")
                _clear_marquee_messages()

                logging.info("Adding new messages...")
                _add_new_marquee_message(artist, title)
            else:
                logging.info("Current marquee message is the same as the current playing song. Will not update marquee message.")
        else:
            logging.info("Not currently playing anything... Nothing to update.")

        time.sleep(5)

"""
    Gets the current marquee artist and song title from the marquee
    :return: A tuple containing the current marquee artist and song title
"""
def _get_current_marquee_artist_and_song_title(self) -> tuple:
    current_marquee_artist = ""
    current_marquee_title = ""
    try:
        messages = _get_current_marquee_messages().get_messages()
        message = messages[0]
        current_marquee_artist, current_marquee_title = message.extract_artist_and_song_title_from_marquee_message() if message else ("", "")
    except IndexError:
        logging.error("No current marquee messages found. Will create new marquee message.")

    return current_marquee_artist, current_marquee_title

"""
    Gets the current marquee messages from the marquee
    :return: The current marquee messages
"""
def _get_current_marquee_messages() -> MarqueeMessages:
    try:
        return MarqueeApiClient().get_current_marquee_messages()
    except Exception as e:  # Catch all exceptions to prevent the script from crashing
        logging.error(f"Error getting current marquee messages: {e}")
        return MarqueeMessages()

"""
    Clears the current messages from the marquee
"""
def _clear_marquee_messages():
    try:
        MarqueeApiClient().clear_marquee_messages()
    except Exception as e:  # Catch all exceptions to prevent the script from crashing
        logging.error(f"Error clearing marquee messages: {e}")

"""
    Adds a new marquee message to the marquee
    :param artist: The artist name
    :param songTitle: The song title
"""
def _add_new_marquee_message(artist, songTitle):
    try:
        MarqueeApiClient().add_new_marquee_message(artist, songTitle)
    except Exception as e:  # Catch all exceptions to prevent the script from crashing
        logging.error(f"Error adding new marquee message: {e}")

"""
    Gets the current playing song from Apple Music.
    :return: The current playing song
"""
def _get_current_playing_song() -> AppleMusicNowPlayingMetadata:
    try:
        return AppleMusicClient().get_current_playing_song()
    except Exception as e: # Catch all exceptions to prevent the script from crashing
        logging.error(f"Error getting current playing song: {e}")
        return AppleMusicNowPlayingMetadata("", "", 0)

if __name__ == '__main__':
    main()
