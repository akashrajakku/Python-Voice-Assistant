import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<=18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    
    speak("I am jarvis Please tell me how may i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio =r.listen(source)



    try:
        print("Recognizing your speech...")
        query =r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
       # print(e)

        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia for you...')
            query = query.replace("wikipedi","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'introduce yourself' in query:
            speak("Hello Everyone MY name is Hazel, I am a voice assistant ready to serve you,I can open any website you ask for, I can email for you,open your camera ,and what not Feel free to ask anything ,I am always there for you")
        elif 'what is your name' in query:
            speak("Hello Everyone MY name is Hazel, I am a voice assistant ready to serve you,I can open any website you ask for, I can email for you,open your camera ,and what not Feel free to ask anything ,I am always there for you")
        elif 'play music' in query:
            music_dir = 'D:\songs'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'thank you' in query:
            speak(f"you are welcome")
        elif 'open vs code' in query:
            codepath="D:\\Microsoft VS Code\\code.exe" 
            os.startfile(codepath)
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")  
        