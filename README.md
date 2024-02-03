# ProTranslate Application

ProTranslate is a simple translation application utilising Python and the Tkinter library. This application allows users to translate text from one language to another, utilize speech recognition for input, and even generate audio output of the translated text through a simple, easy-to-use UI.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

ProTranslate is a language translation tool that leverages the Google Translate API, speech recognition capabilities, and text-to-speech conversion. With a user-friendly graphical user interface (GUI) built using Tkinter, users can easily input text, select target languages, and receive translated results in real-time.

## Features

- **Text Translation:** Enter the text you want to translate and select the target language from the dropdown menu. The application will promptly provide the translated text.

- **Speech Recognition:** Users can opt for speech input using the "Record" button, which converts spoken words into text for translation.

- **Text-to-Speech:** ProTranslate can generate audio output for the translated text, allowing users to listen to the pronunciation of the translated content.

- **Fun Facts:** Selecting a language triggers the display of interesting facts related to that language and its respective country.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/ProTranslate.git
   ```

2. Install the required Python packages using pip:

   ```bash
   pip install googletrans==4.0.0-rc1
   pip install SpeechRecognition
   pip install gtts
   ```

3. Run the application:

   ```bash
   python protranslate.py
   ```

## Usage

1. Launch the application using the provided installation instructions.

2. Type the text you wish to translate in the text entry field.

3. Select the target language from the dropdown menu.

4. Click the "Confirm" button to translate the text and view the result in the output area.

5. To use speech recognition, click the "Record" button, speak your text, and see the converted text appear in the input field.

6. Click the "Audio" button to hear the translated text as audio.

7. The application also displays fun facts related to selected languages. These facts provide insights into various cultures and languages.

8. The "Clear" button can be used to remove text from both the input and output fields.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for enhancements, feel free to submit a pull request. Please ensure that you adhere to the [code of conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
