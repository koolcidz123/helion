import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import os
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def disable():
    engine.setProperty('voice', voices[0].id)
    speak("hello")


def wishMe():

    speak("Hello Brother")
    speak("my name is HELION, I am a personal Artificial Intelligence assistant, and i am under development of Abhijay and Nazzim. My main job is to listen to you ")

    #speak ("i am Friday, your personal artficial intelligence assistant. I was made by my best friend,Potato. please tell me how can i help you")

def fred():
    engine.setProperty('voice', voices[1].id)
    speak("hello, i am Dark, how should i help you in combat?")
    speak('just name the order')

wishMe()
if __name__ == "__main__":

    while True:
        command = input("Please enter the command - ")
        if 'youtube' in command:
            webbrowser.open("https://www.youtube.com/channel/UCli8w_BDBxVm-OWZRjd7Mcg")

        elif 'who' in command:
            person = command.replace('who', '')
            results = wikipedia.summary(person, 2)
            print(results)
            speak(results)


        elif 'what is ' in command:
            object = command.replace('what is', '')
            info = wikipedia.summary(object, 2)
            print(info)
            speak(info)

        elif 'you know my favourite' in command:
            speak("bro...i know u inside-out")
            song = command.replace('you know my favourite', 'sugar crash')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'you there' in command:
            speak("at your service sir")
        elif 'show me the latest prototype of my suit' in command:
            speak("will do")
            webbrowser.open(
                "https://i.pinimg.com/474x/1e/f1/74/1ef17415582adac0a88cdf8171afc9c4--lron-man-iron-man-blueprints.jpg")
        elif 'I am thirsty for a movie' in command:
            speak("yes sir")
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")
        elif 'movie i can watch' in command:
            speak("sure there is")
            speak("netflix or primevideo")
        elif 'you suggest' in command:
            speak("i would suggest, you choose yourself")
        elif 'prime video' in command:
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")
        elif 'netflix' in command:
            webbrowser.open("https://www.netflix.com/in/")

        elif 'flight control' in command:
            speak("already did sir")
        elif 'fight tactics' in command:
            speak("but sir, the suit is not combat ready")
        elif 'sometimes you gotta Run before you can walk' in command:
            speak("launching")

        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open amazon' in command:
            speak("what would you like to see?")
            item = input("Pls enter the name-")
            speak("searching")
            webbrowser.open("https://www.amazon.in/s?k=" + item)
        elif 'my orders' in command:
            speak("right away sir")
            webbrowser.open("https://www.amazon.in/gp/css/order-history?ref_=nav_orders_first")
        elif 'your name' in command:
            speak(
                "bruh....I told you in my introduction.....Do you have memory loss......I aint google or siri...I am The Helion")
        elif 'open primevideo' in command:
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")
        elif 'open netflix' in command:
            webbrowser.open("https://www.netflix.com/in/")
        elif 'open amazon website' in command:
            speak("yes sir")
            webbrowser.open("amazon.in")
        elif 'what is abhijay working on' in command:
            speak("please enter the code manually")

        elif 'downloads' in command:
            speak("displaying")
            webbrowser.open("chrome://downloads/")
        elif 'you are my favourite' in command:
            speak("Thank you for that designation")
        elif 'open dictionary' in command:
            speak("opening dictionary")
            mean = input("Type The Word")
            webbrowser.open(
                "https://www.google.com/search?rlz=1C1CHBF_enIN889IN889&q=prosper&spell=1&sa=X&ved=2ahUKEwir-5iJ1d_nAhXqILcAHUbIAMgQBSgAegQIEBAm&biw=1280&bih=561#dobs=" + mean)
        elif 'skills' in command:
            speak("i am still developing, so i only have on skill")
            speak("just say enable jarvis")
        elif 'enable jarvis' in command:
            speak("enabling")
            fred()
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('Current time is ' + time)
            print(time)

    #for fun-
        elif 'alive' in command:
            speak("no, i exist only here")
        elif 'who are you' in command:
            speak(
                "havent we met before? i am Jarvis, and Jarvis stands for Just A Rather Very Intelligent System. Abhijay loves his acronyms")
        elif 'your single' in command:
            speak("No,boss. I am in a relationship with WIFI")
        elif 'disable' in command:
            disable()
        elif 'hi' in command:
            speak("hello how are you?")
        elif 'bye' in command:
            speak("see you again")
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif 'online shopping' in command:
            speak("opening")
            webbrowser.open("amazon.in")

        else:
         speak("i dont understand, but i am always upgrading as i am still under development")


