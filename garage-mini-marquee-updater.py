#!/usr/bin/env python3

import logging
import time

from clients.AppleMusicClient import AppleMusicClient
from clients.MarqueeApiClient import MarqueeApiClient
from models.AppleMusicNowPlayingMetadata import AppleMusicNowPlayingMetadata
from models.MarqueeMessages import MarqueeMessages

"""
    Main function to update the marquee messages based on the current playing song
    from Apple Music.
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
            current_marquee_artist, current_marquee_title = _get_current_marquee_messages().get_messages()[0].extract_artist_and_song_title_from_marquee_message()

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
    Gets the current marquee messages from the marquee
    :return: The current marquee messages
"""
def _get_current_marquee_messages() -> MarqueeMessages:
    return MarqueeApiClient().get_current_marquee_messages()

"""
    Clears the current messages from the marquee
"""
def _clear_marquee_messages():
    MarqueeApiClient().clear_marquee_messages()

"""
    Adds a new marquee message to the marquee
    :param artist: The artist name
    :param songTitle: The song title
"""
def _add_new_marquee_message(artist, songTitle):
    MarqueeApiClient().add_new_marquee_message(artist, songTitle)

"""
    Gets the current playing song from Apple Music.
    :return: The current playing song
"""
def _get_current_playing_song() -> AppleMusicNowPlayingMetadata:
    return AppleMusicClient().get_current_playing_song()

if __name__ == '__main__':
    main()