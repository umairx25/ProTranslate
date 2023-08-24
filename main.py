
import tkinter as tk
from tkinter import messagebox 
from tkinter import scrolledtext
from tkinter import Entry
from tkinter import Text  
from tkinter import *
import googletrans 
from googletrans import Translator
import speech_recognition as sr
from speech_recognition import UnknownValueError
import gtts
import os
from gtts import gTTS
import json

#Root frame
root = tk.Tk()
root.geometry("635x580")
root.title("ProTranslate")

#Speech recognizer
r = sr.Recognizer()
mic= sr.Microphone()
isTrue = True

#Language database
data= googletrans.LANGUAGES
data_keys= list(data.keys())
data_values= list(data.values())
data_capitalized= []


for i in range (len(data_values)):
     new= data_values[i].capitalize()
     data_capitalized.append(new)

#Reading JSON File
with open('countries.json', 'r', encoding='utf-8') as json_file:
    fun_facts = json.load(json_file)



#******************************************************************************

#Translate function
def translate(txt,lang):  #user passes in text to translate, followed by language

    
    txt= str(txt)
    lang= str(lang)

    pos= int(data_values.index(lang.lower()))
    code= data_keys[pos]

    #Translator
    translator= googletrans.Translator()
    txt= translator.translate(txt,dest=lang).text

    return str(txt)


#Speech Recognition Function
def speechrec():
    text="H"
    with mic as source:
        r.adjust_for_ambient_noise(mic)
        print("Listening...")
        audio = r.record(mic, 3)
        try:
            text = r.recognize_google(audio)
        except UnknownValueError:
            print("Not found")
            pass
        return text


#Text to speech Function
def tts(txt,language):
    
    txt= str(txt)
    lang= str(language)

    pos= int(data_values.index(lang.lower()))
    code= data_keys[pos]
    output = gTTS(text=txt,lang=code,slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

#Fun fact

def update_fun_fact(event=None):
    selected_country = variable.get() #works
    fun_fact = fun_facts.get(str(selected_country))
    text2.config(state= tk.NORMAL)
    text2.delete("1.0", tk.END)
    text2.insert("1.0", fun_fact)
    text2.config(state=tk.DISABLED)
    
#******************************************************************************


#All the frames
main_frame = tk.Frame(root, width=635, height=580, bg="#1E1E1E")
main_frame.pack_propagate(False)
main_frame.pack()


title_frame = tk.Frame(main_frame, width=635, height=50, bg="#2F0DFE")
title_frame.place(x=0, y=0)

#User inputs text to be translated
text= tk.Entry(root, width=635) 
text.pack()
text.place(x=5, y=126)

#Fun facts
text2= tk.Text(root, width=60, height= 5) #Choose a language
text2.pack()
text2.place(x=5, y=229)

#Dropdown list
variable = StringVar(root)
variable.set(data_capitalized[0]) # default value

lang_options = OptionMenu(root, variable, *data_capitalized, command= update_fun_fact)
lang_options.place(x=530,y=195)

#Bottom frame including Your Result
div9 = tk.Frame(main_frame, width=635, height=42, bg="#2F0DFE") 
div9.place(x=0, y=322) 

#Bottom most frame including output
div11 = tk.Frame(main_frame, width=635, height=216, bg="#1E1E1E", bd=0.50, relief="solid")
div11.place(x=0, y=364) 

#********************************************************************************************

#Text
main_title = tk.Label(main_frame, text="ProTranslate", font=("Calibri", 20, "normal"), fg="#D9D9D9",bg= "#2F0DFE" )
main_title.place(x=5, y=5)  #title

input_text = tk.Label(main_frame, text="Type what you want to be translated", font=("Inter", 13, "normal"), fg="#D9D9D9",bg="#1E1E1E")
input_text.place(x=5, y=100) #abov text box

lang_text = tk.Label(main_frame, text="Choose Language", font=("Inter", 13, "normal"), fg="#D9D9D9",bg="#1E1E1E")
lang_text.place(x=5, y=200) #choosing language

output_text = tk.Label(main_frame, text="Your Result", font=("Inter", 16, "normal"), fg="#D9D9D9", bg="#2F0DFE")
output_text.place(x=5, y=330)


#********************************************************************************************
#Buttons

voice_input = tk.Button(main_frame, text="Record", font=("Inter", 13, "normal"), fg="#D9D9D9", bg="#FF0000", relief="flat",command=lambda: OnClick(voice_input))
voice_input.place(x=560, y=90) 

voice_output = tk.Button(main_frame, text="Audio", font=("Inter", 13, "normal"), fg="#D9D9D9", bg="#FF0000",command=lambda: OnClick(voice_output))
voice_output.place(x=565, y=550) 

confirm_button= tk.Button(main_frame, text= "Confirm",font=("Inter", 13, "normal"),fg="#D9D9D9", bg="#FF0000",command=lambda: OnClick(confirm_button))
confirm_button.place(x=545, y=260) 

clear_button= tk.Button(main_frame, text= "Clear",font=("Inter", 13, "normal"),fg="#D9D9D9", bg="#FF0000",command=lambda: OnClick(clear_button))
clear_button.place(x=5, y=260) 

#Button On Click Method

def OnClick (button_id): #function that manages button clicks

    if button_id== voice_input: #speech recognition
        val= str(speechrec())

        text.delete(0, tk.END)  # Clear any existing text in the Entry widget
        text.insert(0, val)  # Insert the recognized text

       
    
    if button_id== confirm_button: #confirmation button
            input= text.get()
            language= variable.get().lower()
            result= translate(input,language)
            text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=635, height=10, font=("Times New Roman", 13),fg="#FFFFFF", bg="#1E1E1E")
            text_area.place(x=0, y=360)
            text_area.insert("1.0",result)
            
    if button_id== voice_output:  #listen to audio recording of output
        confirm_input = tk.messagebox.askquestion(title=None, message='Listen to recording?') 

        if confirm_input:
            input= translate(text.get(),variable.get().lower())
            language= variable.get().lower()
            tts(input,language)

    if button_id== clear_button: #Clear content
        text.delete(0, tk.END)  # Clear any existing text in input or lang fields
        

#************************************************************************************************

root.mainloop()
