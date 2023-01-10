import speech_recognition as sr
import smtplib
import ssl
import pywhatkit
import datetime
from email.message import EmailMessage

recognizer = sr.Recognizer()

current_time = datetime.datetime.now()
print(type(current_time.minute))

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
    pywhatkit.sendwhatmsg('+41798931892',msg,current_time.hour,current_time.minute + 2,10,tab_close=True)

def record_audio():
    text = ''
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1) #clearing the background noise
        print("Wating for your message")
        record_audio = recognizer.listen(source=source)
        print("Done recording")

        try:
            text = recognizer.recognize_google(record_audio,language='en-us')
            print("User Said:{}".format(text))

        except Exception as ex:
            print(ex)
    return text

try:
    text = record_audio()
    if(len(text) != 0):
        sendEmail(text)
        sentWhatsappMsg(text) 
    else:
        print("Please tell again")

except Exception as e:
    print(e)
    



