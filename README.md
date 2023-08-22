# ProTranslate

ProTranslate is a language translation tool that leverages the Google Translate API, speech recognition capabilities, and text-to-speech conversion. With a user-friendly graphical user interface (GUI) built using Tkinter, users can easily input text, select target languages, and receive translated results in real-time.

Features
Text Translation: Enter the text you want to translate and select the target language from the dropdown menu. The application will promptly provide the translated text.

Speech Recognition: Users can opt for speech input using the "Record" button, which converts spoken words into text for translation.

Text-to-Speech: ProTranslate can generate audio output for the translated text, allowing users to listen to the pronunciation of the translated content.

Fun Facts: Selecting a language triggers the display of interesting facts related to that language and its respective country.

Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/ProTranslate.git
Install the required Python packages using pip:

bash
Copy code
pip install googletrans==4.0.0-rc1
pip install SpeechRecognition
pip install gtts
Run the application:

bash
Copy code
python protranslate.py

Usage
Launch the application using the provided installation instructions.

Type the text you wish to translate in the text entry field.

Select the target language from the dropdown menu.

Click the "Confirm" button to translate the text and view the result in the output area.

To use speech recognition, click the "Record" button, speak your text, and see the converted text appear in the input field.

Click the "Audio" button to hear the translated text as audio.

The application also displays fun facts related to selected languages. These facts provide insights into various cultures and languages.

The "Clear" button can be used to remove text from both the input and output fields.
