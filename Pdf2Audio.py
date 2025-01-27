"""Lets Import the required modules to run this programme"""
import PyPDF2    
from gtts import gTTS
import pygame

# Step 1: Extract text from the PDF
def Textfrompdf():
    with open("C:\\Users\\rbodasingu\\Music\\Demystifying the pi network.pdf", mode='rb') as file:
        file_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in file_reader.pages:
            text += page.extract_text()
    return text

# Step 2: Clean up the extracted text
def removechar(text):
    text = text.replace('\n', ' ').replace('\r', '').strip()  # Remove unwanted line breaks and extra spaces
    return text

# Step 3: Convert the cleaned text to audio
def text_to_audio(text, audio_file):
    tts = gTTS(text, lang='en')  # Language can be changed to your preference
    tts.save(audio_file)  # Save the audio file

# Step 4: Save/Play the audio file
text = Textfrompdf()  # Extract the text
formatted_text = removechar(text)  # Clean up the text
text_to_audio(formatted_text, "output.mp3")  # Convert text to audio

# Playing the audio (using pygame)
pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
