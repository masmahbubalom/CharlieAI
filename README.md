# Charlie AI

Charlie AI is a voice-controlled AI assistant developed by Mahbub Alom using Python. It utilizes various libraries and APIs to provide a range of functionalities, including web browsing, application launching, retrieving information from Wikipedia, and engaging in conversation using OpenAI's GPT-3.5 language model.

## Features

- Voice-controlled AI assistant
- Open websites by name
- Open applications by name
- Retrieve current time and date
- Open YouTube channels by username
- Search and retrieve information from Wikipedia
- Chat with the AI assistant using natural language

## Prerequisites

To run Charlie AI, you'll need the following:

- Python 3 or latest version installed on your system
- Required Python libraries: `win32com.client`, `speech_recognition`, `webbrowser`, `openai`, `datetime`, `wikipedia`
- An OpenAI API key (sign up on OpenAI's website to obtain one)
- Configuration file (`config.py`) containing API key, website URLs, and application paths

## Setup

1. Install the required Python libraries by running the following command:
   ```
   pip install pywin32 speechrecognition webbrowser openai datetime wikipedia
   ```

2. Set the OpenAI API key in the config.py file. To get API  [Click Here](https://platform.openai.com/account/api-keys).
3. Only MacOS User : remove/comment 'say' function in 'For Windows' section and remove 'say' function comment in 'For macOS' secion from `config.py` file.

## Usage

1. Run the `CharlieAI.py` script using the following command:

   ```
   python CharlieAI.py
   ```

2. Use a IDE or Code Editor for better experience(e.g. PyCharm).

3. Once the script is running, the AI assistant will greet you and wait for your input.

4. You can give commands to the AI assistant using voice input.

   Examples of commands:

   - "Open github(You can add website list from config.py file)"
   - "Open Calculator((You can add applications list from config.py file))"
   - "What's the time?"
   - "'Open (website name with domain) website'. eg say-'open nbc news website' it's opens 'nbcnews .com'"
   - "'Open (username) YouTube channel'. eg say-'open m r beast youtube channel ' it's opens 'youtube .com/@mrbeast'"
   - "'according to wikipedia (Ask for information)'. eg say- 'according to wikipedia what is python'"

5. The AI assistant will respond to your commands, execute the requested actions, and provide the necessary information.

6. You can engage in a conversation with the AI assistant by asking questions or making statements. It will respond based on its training with the GPT-3.5 language model.

## Customization

- You can modify the list of websites in the `sites` variable within the `config.py` file to add or remove websites that you frequently visit.

- Similarly, you can modify the list of applications in the `apps` variable to add or remove applications that you want to open using the AI assistant.

## Note

- The `config.py` file and the `CharlieAI.py` script should be in the same directory.

- Make sure you have a working microphone connected to your system to use the voice recognition feature.

- The speech recognition is based on Google's Speech Recognition API, so an internet connection is required for voice commands.

## Conclusion

Charlie AI is an AI assistant created by Mahbub Alom that can help you perform various tasks, retrieve information and engage in conversations. It provides a convenient and interactive way to interact with your computer using voice commands. Feel free to explore the code and customize it according to your needs. Enjoy your interaction with Charlie AI!
