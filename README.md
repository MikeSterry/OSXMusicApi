# OSX Music to API
- This is a simple script to convert the music from your OSX Music app to an API that can be used by other applications.
- In my use case I send the data to a local API that displays the results on a Marquee
- It uses the `now-playing.scpt` AppleScript to parse the Apple Audio metadata, parses the output, and then sends it to a local API.

# Installation
- Python 3.8+
- Clone repository
- Install python virtual environment and install requirements:
  - `python3 -m venv venv`
  - `source venv/bin/activate`
  - `pip install -r requirements.txt`
- Copy the now-playing.scpt to a location of your choosing to parse the Apple Audio metadata
- Make a copy of the `config_template.ini` file and rename it to `config.ini`
- Edit the `config.ini` file to set your API URL and the location of the now-playing.scpt file.
- Configure OSX to run this as a service to keep it in the background. 
  - First copy the `com.music.metadata.marquee.updater.plist` file to your LaunchAgents directory
    - `cp com.music.metadata.marquee.updater.plist $HOME/Library/LaunchAgents/com.music.metadata.marquee.updater.plist`
  - Now you can load and start the service with launchctl
    - `launchctl load $HOME/Library/LaunchAgents/com.music.metadata.marquee.updater.plist`
    - `launchctl start $HOME/Library/LaunchAgents/com.music.metadata.marquee.updater.plist`

### Note: If you want to stop the service, you can create a script from the following code snippet
- First create a file with whatever name you want, for example `restart_service.sh`
- Make the file executable with `chmod +x restart_service.sh`
- Paste the following code into the file:
```
#!/bin/bash

echo stopping app...
launchctl stop $HOME/Library/LaunchAgents/com.music.metadata.marquee.updater.plist

echo unloading app...
launchctl unload $HOME/Library/LaunchAgents/com.music.metadata.marquee.updater.plist

echo loading app...
launchctl load $HOME/Library/LaunchAgents/com.music.metadata.marquee.updater.plist

echo starting app...
launchctl start $HOME/Library/LaunchAgents/com.music.metadata.marquee.updater.plist
```