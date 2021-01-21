import speech_recognition as sr
import smtplib
from email.message import EmailMessage
def listen():
    with sr.Microphone() as source:
            r=sr.Recognizer()
            print("listening.....")
            audio=r.record(source,duration=5)
            try:
                bola=r.recognize_google(audio)
                print(bola)
                return bola.lower()
            except:
                print("say again")
def send_mail(final, subj, body):
    server = smtplib.SMTP("smtp.gmail.com", 555)
    server.starttls()
    server.login("prateektiwari378@gmail.com", "pratik@123")
    email = EmailMessage()
    email['From'] = "prateektiwari378@gmail.com"
    email['To'] = final
    email['Subject'] = subj
    email.set_content(body)
    server.send_message(email)
def email_info():
    print("to whom?")
    name = listen()
    final = name + "@gmail.com"
    print("subject")
    subj = listen()
    print("content")
    body = listen()
    send_mail(final, subj, body)
email_info()