"""
This file runs the GUI
"""

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import googletrans
import speech_recognition as sr
import os
from gtts import gTTS
import json


def translate(txt: str, lang: str = 'en') -> str:
    """
    Translates given text to a language of the user's choice, defaults to English
    """

    translator = googletrans.Translator()
    translated = translator.translate(txt, dest=lang).text

    return translated


def speechrec():
    """
    Listens to the user input and returns back their speech in text format
    :return:
    """
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(mic)
        print("Listening...")
        audio = r.record(mic, 3)

        try:
            return r.recognize_sphinx(audio)

        except sr.UnknownValueError:
            print("Not found")
            return ''


def tts(txt: str, dest_lang: str):
    """
    Given a certain text, perform a text to speech operation. Save the resulting file in the
    language the user picks (dest_lang).
    :param txt:
    :param dest_lang:
    :return:
    """

    lang_code = [d for d in googletrans.LANGUAGES if googletrans.LANGUAGES[d] == dest_lang.lower()]  # can only return 1
    output = gTTS(text=txt, lang=lang_code[0], slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")


def update_fun_fact(text2: tk.Text, selected_language: str, filename: str = 'countries.json'):
    """
    Display a fun fact about the language selected from the given filename
    """

    # Reading JSON File
    with open(filename, 'r', encoding='utf-8') as json_file:
        fun_facts = json.load(json_file)

    fun_fact = fun_facts[selected_language.capitalize()]

    text2.config(state=tk.NORMAL)
    text2.delete("1.0", tk.END)
    text2.insert("1.0", fun_fact)
    text2.config(state=tk.DISABLED)

    return fun_fact


def run_gui():
    """
    Run the gui using the tkinter library
    :return:
    """

    root = tk.Tk()
    root.title("ProTranslate")

    # All the frames
    main_frame = tk.Frame(root, width=635, height=580, bg="#1E1E1E")
    main_frame.pack_propagate(False)
    main_frame.pack()

    title_frame = tk.Frame(main_frame, width=635, height=50, bg="#2F0DFE")
    title_frame.place(x=0, y=0)

    # User inputs text to be translated
    # text= tk.Entry(root, width=635)
    text = tk.Text(root, width=60, height=2, wrap=tk.WORD, font=("Times New Roman", 13), state=tk.NORMAL)
    scrollbar = tk.Scrollbar(root, command=text.yview)
    text.config(yscrollcommand=scrollbar.set)
    text.pack()
    text.place(x=5, y=126)
    scrollbar.place(x=540, y=126, height=42.3)

    # Fun facts
    text2 = tk.Text(root, width=60, height=5)  # Choose a language
    print(text2)
    text2.pack()
    text2.place(x=5, y=229)

    # Dropdown list
    variable = tk.StringVar(root)
    all_langs = [g.capitalize() for g in googletrans.LANGUAGES.values()]
    variable.set(all_langs[0])  # default value

    lang_options = tk.OptionMenu(root, variable, *all_langs)
    lang_options.place(x=170, y=195)

    if variable:  #############################################################
        update_fun_fact(text2, variable.get())

    # Bottom frame including Your Result
    div9 = tk.Frame(main_frame, width=635, height=42, bg="#2F0DFE")
    div9.place(x=0, y=322)

    # Bottom most frame including output
    div11 = tk.Frame(main_frame, width=635, height=216, bg="#1E1E1E", bd=0.50, relief="solid")
    div11.place(x=0, y=364)

    # ********************************************************************************************

    # Text
    main_title = tk.Label(main_frame, text="ProTranslate", font=("Calibri", 20, "normal"), fg="#D9D9D9", bg="#2F0DFE")
    main_title.place(x=5, y=5)  # title

    input_text = tk.Label(main_frame, text="Type what you want to be translated", font=("Inter", 13, "normal"),
                          fg="#D9D9D9", bg="#1E1E1E")
    input_text.place(x=5, y=100)  # abov text box

    lang_text = tk.Label(main_frame, text="Choose Language", font=("Inter", 13, "normal"), fg="#D9D9D9", bg="#1E1E1E")
    lang_text.place(x=5, y=200)  # choosing language

    output_text = tk.Label(main_frame, text="Your Result", font=("Inter", 16, "normal"), fg="#D9D9D9", bg="#2F0DFE")
    output_text.place(x=5, y=330)

    fun_fact_label = tk.Label(main_frame, text="", font=("Inter", 12, "italic"), fg="#FFFFFF", bg="#1E1E1E")
    fun_fact_label.place(x=5, y=250)

    # ********************************************************************************************
    # Buttons

    voice_input = tk.Button(main_frame, text="Record", font=("Inter", 13, "normal"), fg="#D9D9D9", bg="#FF0000",
                            relief="flat", command=lambda: on_click(voice_input))
    voice_input.place(x=560, y=90)

    voice_output = tk.Button(main_frame, text="Audio", font=("Inter", 13, "normal"), fg="#D9D9D9", bg="#FF0000",
                             command=lambda: on_click(voice_output))
    voice_output.place(x=565, y=550)

    confirm_button = tk.Button(main_frame, text="Confirm", font=("Inter", 13, "normal"), fg="#D9D9D9", bg="#FF0000",
                               command=lambda: on_click(confirm_button))
    confirm_button.place(x=500, y=229)

    clear_button = tk.Button(main_frame, text="Clear", font=("Inter", 13, "normal"), fg="#D9D9D9", bg="#FF0000",
                             command=lambda: on_click(clear_button))
    clear_button.place(x=500, y=270)

    # Button On Click Method

    def on_click(button_id: tk.Button) -> None:  # function that manages button clicks
        """
        Determines the actions that happen when a button is clicked
        :param button_id:
        :return:
        """

        if button_id == voice_input:  # speech recognition
            val = str(speechrec())

            text.delete("1.0", tk.END)  # Clear any existing text in the Entry widget
            text.insert("1.0", val)  # Insert the recognized text

        if button_id == confirm_button:  # confirmation button
            user_input = text.get("1.0", "end-1c")
            language = variable.get().lower()
            result = translate(user_input, language)
            text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=635, height=10,
                                                  font=("Times New Roman", 13), fg="#FFFFFF", bg="#1E1E1E")
            text_area.place(x=0, y=360)
            text_area.insert("1.0", result)

        if button_id == voice_output:  # listen to audio recording of output
            confirm_input = tk.messagebox.askquestion(title=None, message='Listen to recording?')

            if confirm_input:
                user_input = translate(text.get("1.0", "end-1c"), variable.get().lower())
                language = variable.get().lower()
                tts(user_input, language)

        if button_id == clear_button:  # Clear content
            text.delete("1.0", tk.END)  # Clear any existing text in input or lang fields

    root.mainloop()


if __name__ == '__main__':
    run_gui()
