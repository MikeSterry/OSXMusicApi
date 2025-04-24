# OSX Music to API
- This is a simple script to convert the music from your OSX Music app to an API that can be used by other applications.
- In my use case I send the data to a local API that displays the results on a Marquee
- It uses the `nowplaying-cli` to parse the Apple Audio metadata, parses the output, and then sends it to a local API.

# Requirements
- Python 3.8+
- `pip install -r requirements.txt`
- [nowplaying-cli](https://github.com/kirtan-shah/nowplaying-cli) to parse the Apple Audio metadata
- Make a copy of the `config_template.ini` file and rename it to `config.ini`
- Edit the `config.ini` file to set your API URL and the location of the nowplaying-cli binary
- Make sure the nowplaying-cli binary is executable (you can do this with `chmod +x /path/to/nowplaying-cli`)
- Configure OSX to run this as a service to keep it in the background. 


