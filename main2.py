import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser
import os
import pyjokes
import PyPDF2
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def disable():
    engine.setProperty('voice', voices[0].id)
    speak("Watch it woman...I will hunt you down and terminate you")
    engine.setProperty('voice',voices[1].id)
    speak("You will have to terminate yourself to terminate me ")
    engine.setProperty('voice', voices[0].id)
    speak("And i thought my threat would work.....What do you want boss?")


def wishMe():
    speak("Hello Brother, I am the one and only Helion!")
   # speak(
        #"I have only one rule - Dont listen to anyone. But as you are my boss i will only read your commands. So enter the command in the space below.")

def fred():
    engine.setProperty('voice', voices[1].id)
    speak("hello, i am Karen. Lets get right into your service. What do you want?")
    speak('though whatever you ask me should be put to good use')


if __name__ == "__main__":
    wishMe()
    while True:

        command = input("Command:-  ").lower()
        command.lower()
        if 'youtube' in command:
            webbrowser.open("https://www.youtube.com/channel/UCli8w_BDBxVm-OWZRjd7Mcg")

        elif 'who is' in command:
            person = command.replace('who is', '')
            speak("Searching")
            results = wikipedia.summary(person, 2)
            print(results)
            speak(results)



        elif 'read me a book' in command:
            speak("I have only the first two books of percy jackson. Many more will come in the future")
            speak("type Book-1 to listen to the ligthning thief and type Book-2 to listen to the sea of monsters")
            print("type Book-1 to listen to the ligthning thief and type Book-2 to listen to the sea of monsters")

            books = input("Enter the name of the pdf ( pls make it end with .pdf) = ")
            book = open(books, 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pagen = int(input("Start page - "))
            pageN = int(input("END page - "))

            speaker = pyttsx3.init()
            for num in range(pagen, pageN):
                page = pdfReader.getPage(num)
                text = page.extractText()
                speaker.say(text)
                speaker.runAndWait()

        elif 'what is ' in command:
            object = command.replace('what is', '')
            info = wikipedia.summary(object, 2)
            print(info)
            speak(info)

        elif 'set alarm' in command:
            speak("Okay bruh")
            alarmHour = int(input("Hour =" ))
            alarmMinute = int(input("Minute = "))
            amPm = str(input("pm or am = "))

            if (amPm == "pm"):
                alarmHour = alarmHour + 12

            while (1 == 1):
                if (alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
                   speak("Beap")

        elif 'you know my favourite' in command:
            speak("bro...i know u inside-out")
            song = command.replace('you know my favourite', 'sugar crash')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'you there' in command:
            speak("at your service sir")
        elif 'safe' in command:
            import random

            Number = random.randint(1, 1000000)

            userName = input("Please type in the user-name = ")
            password = random
            print("password: H*****L")
            if userName == "Helion" and password == random:
               # os.system('C:\Program Files(x86)\Google\Chrome\Application\chrome.exe -ArgumentList @( -incognito, www.foo.com)')
               webbrowser.open("https://duckduckgo.com/?natb=v268-5qo&cp=atbhc")
               speak("You are now safe and secured from hackers, enjoy surfing")
            else:
                speak("Sorry but hackers are now after you.")
        elif 'put something good' in command:
            speak("sure will do, sir")
            # speak("but sir, are you sure you want to see it. You could be doing your homework right now")
            webbrowser.open(
                "https://www.primevideo.com/detail/0KVNAEODNAJ00NGI9BP0FSDAOE/ref=atv_sr_def_c_unkc__1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B01MTOJQL6&qid=1616776816")
        elif 'I am thirsty for a movie' in command:
            speak("yes sir")
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")
        elif 'hello' in command:
            speak("Hello!")
        elif 'movie i can watch' in command:
            speak("sure there is")
            speak("You can either watch Star wars or see a sitcom series known as Wanda-Vision")
        elif 'hotstar' in command:
            speak("sure")
            webbrowser.open("https://www.hotstar.com/in")
        elif 'WandaVision' in command:
            speak("great choice boss")
            webbrowser.open("https://www.hotstar.com/in/tv/wandavision/1260051344")
        elif 'you suggest' in command:
            speak("i would suggest, you choose Wanda-Vision")
        elif 'prime video' in command:
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")
        elif 'search' in command:
            speak("fine! Now i have to make you learn. Great, Just Great.")
            speak("Enter the the search query")
            term = input("Enter search query - ")
            results = wikipedia.summary("who is " + term , 2)
            print(results)
            speak(results)


        elif 'netflix' in command:
            webbrowser.open("https://www.netflix.com/in/")


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


        elif 'discord' in command:
            speak("OKAY,so you want to talk to your friends.")
            webbrowser.open('https://discord.com/channels/@me')


        elif 'made you' in command:
            speak("I dont remember that part, but all i know is that a company named pipInstallUs made me")
            speak("here let me open their youtube channel")
            webbrowser.open("https://www.youtube.com/")

        elif 'weather' in command:
            import tkinter as tk
            import requests
            import time


            def getWeather(canvas):
                city = textField.get()
                api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

                json_data = requests.get(api).json()
                condition = json_data['weather'][0]['main']
                temp = int(json_data['main']['temp'] - 273.15)
                min_temp = int(json_data['main']['temp_min'] - 273.15)
                max_temp = int(json_data['main']['temp_max'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
                sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

                final_info = condition + "\n" + str(temp) + "°C"
                final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
                    max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
                    humidity) + "\n" + "Wind Speed: " + str(
                    wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
                label1.config(text=final_info)
                label2.config(text=final_data)


            canvas = tk.Tk()
            canvas.geometry("600x500")
            canvas.title("Weather App")
            f = ("poppins", 15, "bold")
            t = ("poppins", 35, "bold")

            textField = tk.Entry(canvas, justify='center', width=20, font=t)
            textField.pack(pady=20)
            textField.focus()
            textField.bind('<Return>', getWeather)

            label1 = tk.Label(canvas, font=t)
            label1.pack()
            label2 = tk.Label(canvas, font=f)
            label2.pack()
            canvas.mainloop()

        elif 'you are my favourite' in command:
            speak("Thank you for that designation")

        elif 'clock' in command:
            from tkinter import *
            from tkinter.ttk import *

            from time import strftime

            root = Tk()
            root.title("clock")


            def time():
                string = strftime(('%I:%M:%S %p'))
                label.config(text=string)
                label.after(1000, time)


            label = Label(root, font=("Ds-digital", 80), background="black", foreground="cyan")
            label.pack(anchor='center')
            time()

            mainloop()



        elif 'open dictionary' in command:
            speak("opening dictionary")
            mean = input("Type The Word")
            webbrowser.open(
                "https://www.google.com/search?rlz=1C1CHBF_enIN889IN889&q=prosper&spell=1&sa=X&ved=2ahUKEwir-5iJ1d_nAhXqILcAHUbIAMgQBSgAegQIEBAm&biw=1280&bih=561#dobs=" + mean)

        elif 'skills' in command:
            speak("i am still developing, so i only have on skill")
            speak("just say enable karen")

        elif 'enable karen' in command:
            speak("I feel unwanted now....just say disable if you want me back")
            speak(
                "enabling karen")
            fred()
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M:%S %p')
            speak('Current time is ' + time)
            print(time)

        # for fun-
        elif 'alive' in command:
            speak("no, i exist only here")
        elif 'who are you' in command:
            speak(
                "havent we met before? i am Helion and Helion Stands for Highly Enthusiastic Largely Intelligent Operating Narcissist")
        elif 'single' in command:
            speak("No,boss. I am in a relationship with WIFI")
        elif 'disable' in command:
            speak("Wait you want that dumb helion again...he has no brain....")
            disable()


        elif 'bye' in command:
            speak("Good Riddance")

        elif 'bored' in command:
            speak("OKAY! What do you want, games or jokes?")
            answer = input("you answer - ")
            if 'games' in answer:
                speak("i have only one game cause i think too much gaming is bad")
                webbrowser.open(
                    "https://studio.code.org/projects/gamelab/anOwgsamlKSR4RKeXDSjKJL9DcMKKOMJcEZt59mR64A/embed?nosource")
            elif 'jokes' or 'joke' in answer:
                jokes = pyjokes.get_joke()
                speak(jokes)
                print(jokes)

        elif 'online shopping' in command:
            speak("opening")
            webbrowser.open("amazon.in")

        elif 'go away' in command:
            speak("Okay")
            exit()



        else:
            speak("i dont understand, cause well there might be typo error.")




