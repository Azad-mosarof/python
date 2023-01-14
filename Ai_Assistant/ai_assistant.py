import pyttsx3
import speech_recognition as sr
import datetime
import ssl
import smtplib
import vlc
import pywhatkit
from playsound import playsound
import pyaudio
from email.message import EmailMessage
import wikipedia 
import webbrowser
import sys
#import vlc

engin=pyttsx3.init()
voices=engin.getProperty("voices")
engin.setProperty('voice',voices[3].id)
#print(voices[1].id)

current_time = datetime.datetime.now()
player = vlc.MediaPlayer("/home/azadm/Music/Piya O Re Piya Lyrical mp3")

#send Email
def sendEmail(text):
    email_sender='naturelover7908@gmail.com'
    email_pass='tyyiqadlboxefwei'
    email_rec=['misarofazad@gmail.com','am.21u10052@btech.nitdgp.ac.in']
    subject='check this out'

    for i in range(len(email_rec)):
        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_rec[i]
        em['Subject']=subject
        em.set_content(text)
        context=ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.ehlo()
            smtp.login(email_sender, email_pass)
            smtp.send_message(em)
            print("Email Successfully sent")
            smtp.quit()

#sent Whatsapp messages
def sentWhatsappMsg(msg):
    pywhatkit.sendwhatmsg('+916291574545',msg,current_time.hour,(current_time.minute)+2,15,tab_close=True)

def speak(audio):
    engin.say(audio)
    engin.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=4 and hour<=12:
        speak("Good morning")
    elif hour>=12 and hour<=17:
        speak("Good after noon")
    elif hour>17 and hour<=19:
        speak("good evaning")
    else:
        speak("good night")
    speak("I am your assistant sir.how may i help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source=source)
    
    try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-us') #Using google for voice recognition.
            print(f"User said: {query}\n")  #User query will be printed.
            
    except Exception as e:
        # print(e)    
        speak("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
if __name__=="__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case
        webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("/home/azadm/Desktop/firefox"))
        #p=vlc.MediaPlayer("Mujhko Barsaat Bana Lo.MP3")
        # Logic for executing tasks based on query
        if 'open' and 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak("Sure")
            webbrowser.get('firefox').open("https://www.wikipedia.org/")
        
        elif 'open' and 'youtube' in query:
            
            speak("sure")
            webbrowser.get('firefox').open("youtube.com")
        
        elif 'open' and 'google' in query:
            speak("sure")
            webbrowser.get('firefox').open("google.com")
        
        elif 'time' and 'now' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
                
        elif 'thank you' in query:
            speak("welcome sir")
            
        elif 'some time you are late' in query:
            speak("sorry sir for this inconvenient I will improve myself and I hope in future it will not happen!")

        elif 'send' and 'email' in query:
            speak("please sir tell the message:")
            msg = takeCommand()
            sendEmail(msg)
        
        elif ('search' and 'online') in query:
            speak("Please sir tell me what you want to search:")
            search = takeCommand()
            new = 2 
            tabUrl = "http://www.google.com/search?q="
            webbrowser.open(tabUrl+search,new=new)
            # webbrowser.get('firefox').open(search)
        
        elif 'send' and 'whatsapp' in query:
            # print("please sir tell me the sender's Whatsapp number")
            # number = takeCommand()
            speak("please sir tell the message:")
            msg = takeCommand()
            sentWhatsappMsg(msg)
            
        elif 'play' in query:
            player.play()
            print('playing sound using  playsound')
        
        elif 'pause' in query:
            player.pause()

        elif 'stop' in query:
            player.stop()
           
        # if 'stop the music' in query:
               
                
        elif 'sleep' in query:
            speak("ok sir,i hope i helped you")
            sys.exit(0)
