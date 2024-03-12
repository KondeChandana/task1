import pyttsx3
import speech_recognition as chandana
import datetime
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("good morning chandana$")
    elif hour>=12 and hour<18:
        speak("chandu good afternoon$")
    else:
        speak("good evining")
    speak("Iam deekshu mam.please tell me how can i help you mam....")
def takecommand():
    r=chandana.Recognizer()
    with chandana.Microphone()as source :
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en_in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say that again please....")
        return "None"
    return query
if __name__=="__main__":
    wish_me()
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube'in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            music_dir="C:\\Users\\chand\\Downloads"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, the time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\chand\\OneDrive\\Desktop\\chandana.py"
            os.startfile(codepath)