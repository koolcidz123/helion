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
    engine.setProperty('voice', voices[1].id)
    speak("You will have to terminate yourself to terminate me ")
    engine.setProperty('voice', voices[0].id)
    speak("And i thought my threat would work.....What do you want boss?")


def wishMe():
    speak("hi,i am helion and i will be your best friend")
    # speak(
    # "I have only one rule - Dont listen to anyone. But as you are my boss i will only read your commands. So enter the command in the space below.")


def female():
    engine.setProperty('voice', voices[1].id)
    speak("Enabled ")
    speak("hello, i am selen. Lets get right into your service. What do you want?")
    speak('though whatever you ask me should be put to good use')


if __name__ == "__main__":
    wishMe()
    while True:

        command = input("Command:-  ").lower()
        command.lower()

        if 'who is' in command:
            person = command.replace('who is', '')
            speak("Searching")
            results = wikipedia.summary(person, 2)
            print(results)
            speak(results)



        # Features
        elif 'read me a book' in command:
            speak("I have only the first two books of percy jackson. Many more will come in the future")
            speak("type Book-1 to listen to the lightning thief and type Book-2 to listen to the sea of monsters")
            print("type Book-1 to listen to the lightning thief and type Book-2 to listen to the sea of monsters")

            books = input("Enter the name of the pdf  = ")
            book = open(books + ".pdf", 'rb')
            pdfReader = PyPDF2.PdfFileReader(book)
            pagen = int(input("Start page - "))
            pageN = int(input("END page - "))

            speaker = pyttsx3.init()
            for num in range(pagen, pageN):
                page = pdfReader.getPage(num)
                text = page.extractText()
                speaker.say(text)
                speaker.runAndWait()

        elif 'set alarm' in command:
            speak("Okay bruh")
            alarmHour = int(input("Hour ="))
            alarmMinute = int(input("Minute = "))
            amPm = str(input("pm or am = "))

            if (amPm == "pm"):
                alarmHour = alarmHour + 12

            while (1 == 1):
                if (alarmHour == datetime.datetime.now().hour and alarmMinute == datetime.datetime.now().minute):
                    speak("Beap")


        elif 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)


        elif 'what is ' in command:
            object = command.replace('what is', '')
            info = wikipedia.summary(object, 2)
            print(info)
            speak(info)


        elif 'skills' in command:
            speak("i am still developing, so i only have on skill")
            speak("just say enable enable selen")
            print("enable via ")


        elif 'enable selen' in command:
            speak("I feel unwanted now....just say disable if you want me back")
            speak(
                "enabling selen")
            female()


        elif 'disable' in command:
            speak("Wait you want that dumb helion again...he has no brain....")
            disable()


        elif 'open dictionary' in command:
            speak("opening dictionary")
            mean = input("Type The Word")
            webbrowser.open(
                "https://www.google.com/search?rlz=1C1CHBF_enIN889IN889&q=prosper&spell=1&sa=X&ved=2ahUKEwir-5iJ1d_nAhXqILcAHUbIAMgQBSgAegQIEBAm&biw=1280&bih=561#dobs=" + mean)


        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M:%S %p')
            speak('Current time is ' + time)
            print(time)


        elif 'you know my favourite' in command:
            speak("bro...i know u inside-out")
            song = command.replace('you know my favourite', 'sugar crash')
            speak('playing ' + song)
            pywhatkit.playonyt(song)


        elif 'online shopping' in command:
            speak("opening")
            webbrowser.open("amazon.in")


        elif 'put something good' in command:
            speak("sure will do, sir")
            # speak("but sir, are you sure you want to see it. You could be doing your homework right now")
            webbrowser.open(
                "https://www.primevideo.com/detail/0KVNAEODNAJ00NGI9BP0FSDAOE/ref=atv_sr_def_c_unkc__1_1_1?sr=1-1&pageTypeIdSource=ASIN&pageTypeId=B01MTOJQL6&qid=1616776816")


        elif 'I am thirsty for a movie' in command:
            speak("yes sir")
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")


        elif 'movie i can watch' in command:
            speak("sure there is")
            speak("You can either watch THE MANDOLORIAN or see a sitcom series known as Wanda-Vision")


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
            # speak("fine! Now i have to make you learn. Great, Just Great.")
            speak("Enter the search query")
            term = input("Enter search query - ")
            results = wikipedia.summary("who is " + term, 2)
            print(results)
            speak(results)


        elif 'you there' in command:
            speak("at your service sir")


        elif 'netflix' in command:
            webbrowser.open("https://www.netflix.com/in/")


        elif 'open amazon' in command:
            speak("what would you like to see?")
            item = input("Pls enter the name-")
            speak("searching")
            webbrowser.open("https://www.amazon.in/s?k=" + item)


        elif 'my orders' in command:
            speak("right away sir")
            webbrowser.open("https://www.amazon.in/gp/css/order-history?ref_=nav_orders_first")

        elif 'open primevideo' in command:
            webbrowser.open("https://www.primevideo.com/ref=av_auth_return_redir")


        elif 'open netflix' in command:
            webbrowser.open("https://www.netflix.com/in/")


        elif 'discord' in command:
            speak("OKAY,so you want to talk to your friends.")
            webbrowser.open('https://discord.com/channels/@me')



        # elif 'bad' or 'idiot' in command:
        # speak("You bad and idiot!")

        # APPS - / In built screens- / functions-

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

        elif 'stop watch' in command:

            # Python program to illustrate a stop watch
            # using Tkinter
            # importing the required libraries
            import tkinter as Tkinter
            from datetime import datetime

            counter = 66600
            running = False


            def counter_label(label):
                def count():
                    if running:
                        global counter

                        # To manage the intial delay.
                        if counter == 66600:
                            display = "Starting..."
                        else:
                            tt = datetime.fromtimestamp(counter)
                            string = tt.strftime("%H:%M:%S")
                            display = string

                        label['text'] = display  # Or label.config(text=display)

                        # label.after(arg1, arg2) delays by
                        # first argument given in milliseconds
                        # and then calls the function given as second argument.
                        # Generally like here we need to call the
                        # function in which it is present repeatedly.
                        # Delays by 1000ms=1 seconds and call count again.
                        label.after(1000, count)
                        counter += 1

                # Triggering the start of the counter.
                count()

                # start function of the stopwatch


            def Start(label):
                global running
                running = True
                counter_label(label)
                start['state'] = 'disabled'
                stop['state'] = 'normal'
                reset['state'] = 'normal'


            # Stop function of the stopwatch
            def Stop():
                global running
                start['state'] = 'normal'
                stop['state'] = 'disabled'
                reset['state'] = 'normal'
                running = False


            # Reset function of the stopwatch
            def Reset(label):
                global counter
                counter = 66600

                # If rest is pressed after pressing stop.
                if running == False:
                    reset['state'] = 'disabled'
                    label['text'] = 'Welcome!'

                # If reset is pressed while the stopwatch is running.
                else:
                    label['text'] = 'Starting...'


            root = Tkinter.Tk()
            root.title("Stopwatch")

            # Fixing the window size.
            root.minsize(width=250, height=70)
            label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
            label.pack()
            f = Tkinter.Frame(root)
            start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
            stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
            reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
            f.pack(anchor='center', pady=5)
            start.pack(side="left")
            stop.pack(side="left")
            reset.pack(side="left")
            root.mainloop()




        elif 'weather' in command:
            speak("Okay, pls type in your city name in the box that will open now")

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

                # speak min_temp
                speak("Minimum Temperature is")
                speak(min_temp)
                speak("degrees celcius")

                # speak max_temp
                speak("maximum temperature is")
                speak(max_temp)
                speak("degrees celcius")

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





        elif 'calculator' in command:
            from tkinter import *


            def iCalc(source, side):
                storeObj = Frame(source, borderwidth=4, bd=4, bg="powder blue")
                storeObj.pack(side=side, expand=YES, fill=BOTH)
                return storeObj


            def button(source, side, text, command=None):
                storeObj = Button(source, text=text, command=command)
                storeObj.pack(side=side, expand=YES, fill=BOTH)
                return storeObj


            class app(Frame):
                def __init__(self):
                    Frame.__init__(self)
                    self.option_add('*Font', 'arial 20 bold')
                    self.pack(expand=YES, fill=BOTH)
                    self.master.title('Calculator')

                    display = StringVar()
                    Entry(self, relief=RIDGE, textvariable=display,
                          justify='right'
                          , bd=30, bg="powder blue").pack(side=TOP,
                                                          expand=YES, fill=BOTH)

                    for clearButton in (["C"]):
                        erase = iCalc(self, TOP)
                        for ichar in clearButton:
                            button(erase, LEFT, ichar, lambda
                                storeObj=display, q=ichar: storeObj.set(''))

                    for numButton in ("789/", "456*", "123-", "0.+"):
                        FunctionNum = iCalc(self, TOP)
                        for iEquals in numButton:
                            button(FunctionNum, LEFT, iEquals, lambda
                                storeObj=display, q=iEquals: storeObj
                                   .set(storeObj.get() + q))

                    EqualButton = iCalc(self, TOP)
                    for iEquals in "=":
                        if iEquals == '=':
                            btniEquals = button(EqualButton, LEFT, iEquals)
                            btniEquals.bind('<ButtonRelease-1>', lambda e, s=self,
                                                                        storeObj=display: s.calc(storeObj), '+')


                        else:
                            btniEquals = button(EqualButton, LEFT, iEquals,
                                                lambda storeObj=display, s=' %s ' % iEquals: storeObj.set
                                                (storeObj.get() + s))

                def calc(self, display):
                    try:
                        display.set(eval(display.get()))
                    except:
                        display.set("ERROR, your problem is problematic")


            if __name__ == '__main__':
                app().mainloop()




        elif 'safe' in command:
            from tkinter import *

            speak("Type the credentials")
            root = Tk()
            root.geometry("500x300")

            Label(root, text="Secure", font="arial 15 bold").grid(row=0, column=3)


            def getvals():

                webbrowser.open("https://duckduckgo.com/?natb=v268-5qo&cp=atbhc")
                speak("Secured access")


            UserName = Label(root, text="UserName", font="arial 10 bold")
            Passwords = Label(root, text="Password", font="arial 10 bold")

            UserName.grid(row=1, column=2)
            Passwords.grid(row=2, column=2)

            Uservalue = StringVar
            Passwordvalue = StringVar
            checkvalue = StringVar

            Userentry = Entry(root, textvariable=Uservalue)
            Passwordsentry = Entry(root, textvariable=Passwordvalue)

            # CheckBox
            # checkbtn = Checkbutton(text="remember me", variable = checkvalue)
            # checkbtn.grid(row=4, column =3)

            Userentry.grid(row=1, column=3)
            Passwordsentry.grid(row=2, column=3)

            Button(text="Enter", command=getvals).grid(row=4, column=3)

            root.mainloop()




        elif 'translate' in command:
            from tkinter import *
            from tkinter import ttk
            from googletrans import Translator, LANGUAGES

            root = Tk()
            root.geometry('1080x400')
            root.resizable(0, 0)
            root.config(bg='ghost white')

            root.title("Project Gurukul--Language Translator")

            Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='white smoke').pack()

            Label(root, text="Project Gurukul", font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')

            Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)

            Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
            Input_text.place(x=30, y=100)

            Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=60)

            Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
            Output_text.place(x=600, y=100)

            language = list(LANGUAGES.values())

            src_lang = ttk.Combobox(root, values=language, width=22)
            src_lang.place(x=20, y=60)
            src_lang.set('')

            dest_lang = ttk.Combobox(root, values=language, width=22)
            dest_lang.place(x=890, y=60)
            dest_lang.set('')


            def Translate():
                translator = Translator()
                translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(),
                                                  dest=dest_lang.get())

                Output_text.delete(1.0, END)
                Output_text.insert(END, translated.text)


            trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate,
                               bg='royal blue1', activebackground='sky blue')

            trans_btn.place(x=490, y=180)

            root.mainloop()







        # for fun-

        elif 'your name' in command:
            speak(
                "bruh....I told you in my introduction.....Do you have memory loss......I aint google or siri...I am The Helion")


        elif 'made you' in command:
            speak("I dont remember that part, but all i know is that a company named pipInstallUs made me")
            speak("here let me open their youtube channel")
            webbrowser.open("https://www.youtube.com/")


        elif 'you are my favourite' in command:
            speak("Thank you for that designation")


        elif 'alive' in command:
            speak("no, i exist only here")


        elif 'stupid' in command:
            speak("You stupid")
            print("You stupid")


        elif 'who are you' in command:
            speak(
                "havent we met before? i am Helion and Helion Stands for Highly Enthusiastic Largely Intelligent Operating Narcissist")


        elif 'single' in command:
            speak("No,boss. I am in a relationship with WIFI")


        elif 'lol' in command:
            speak("My jokes are always the best.")


        elif 'hey' in command:
            speak("Hey!")


        elif 'help me' in command:
            speak("How? I am not jarvis. I cant send suits. I aint EDITH or FRIDAY. I cant help, sorry.")


        elif 'bye' in command:
            speak("Good Riddance")


        elif 'bored' in command:
            speak("OKAY! What do you want, games or jokes?")
            answer = input("you answer - ")
            if 'games' in answer:
                speak("i have only one game cause my memory is very low")
                webbrowser.open(
                    "https://studio.code.org/projects/gamelab/anOwgsamlKSR4RKeXDSjKJL9DcMKKOMJcEZt59mR64A/embed?nosource")
            elif 'jokes' or 'joke' in answer:
                jokes = pyjokes.get_joke()
                speak(jokes)
                print(jokes)

        elif 'jokes' in command:
            jokes = pyjokes.get_joke()
            speak(jokes)
            print(jokes)

        elif 'games' in command:
            speak("Sure gamer boss!")
            webbrowser.open(
                "https://studio.code.org/projects/gamelab/anOwgsamlKSR4RKeXDSjKJL9DcMKKOMJcEZt59mR64A/embed?nosource")





        # Quit Helion
        elif 'go away' in command:
            speak("Okay")
            exit()



        else:
            speak("i dont understand, cause well there might be typo error.")
