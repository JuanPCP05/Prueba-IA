import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voices', voice[0].id)
newVoiceRate = 145
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime("%I:%M")
    speak("La hora es: "+time)

def date():
    year = str(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    mes = mesesDelyear(month)
    day = str(datetime.datetime.now().day)
    speak("La fecha es: "+day+" de "+str(mes)+" del "+year)

def tiempo():
    hora = ""
    hour = datetime.datetime.now().hour
    if hour > 5 and hour <= 12:
        hora = "Buenos dias"
        return hora
    elif hour > 12 and hour <= 18:
        hora = "Buenas tardes"
        return hora
    else:
        hora = "Buenas noches"
        return hora

def mesesDelyear(argumento):
    switcher = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }
    return switcher.get(argumento, "El mes no está disponible")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Grabado...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Disculpa, no te entendí, repitelo nuevamente")
        return "None"
    return query

def wishme():
    speak("Bienvenido!")
    hora = tiempo()
    speak(str(hora) + " ¿En que puedo ayudarte?")

def search(query):
    speak("searching...")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences = 2)
    speak(result)

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("email", "password")
    server.sendmail("email", to, content)
    server.close()

def searchGoogle():
    speak("¿Que deseas buscar?")
    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    search = takeCommand().lower()
    wb.get(chromepath).open_new_tab(search + ".com")

def song():
    song_dir = "D:/musica"
    song = os.listdir(song_dir)
    os.startfile(os.path.join(song_dir, song[0]))

def recuerdo(tipo):
    if(tipo == True):
        speak("¿Que te gustría que recordara?")
        data = takeCommand()
        speak("Dijiste que recordara"+data)
        remember = open("data.txt", "w")
        remember.write(data)
        remember.close()
    elif(tipo == False):
        remember = open("data.txt", "r")
        speak("Me pediste que recordara" + remember.read())

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Juan Pablo Claro/Desktop/IA Curso/img/ss.png")
    speak("Captura realizada")

def diagnostico():
    usage = str(psutil.cpu_percent())
    speak("CPU es de: "+usage)

def bromas():
    speak(pyjokes.get_joke())
    print(pyjokes.get_joke())


if __name__ == "__main__":
    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit() 
        elif "wikipedia" in query:
            search(query)
        elif "send email" in query:
            try:
                speak("¿Que quieres enviar?")
                content = takeCommand()
                to = ""
                sendmail(to, content)
                speak("Correo enviado con exito")
            except Exception as e:
                print(e)
                speak("Hubo un error, intentelo despues")
        elif "chrome" in query:
            searchGoogle()
        elif "log out" in query:
            os.system("shutdown - 1")
        elif "shutdown" in query:
            os.system("shutdoun /s /t 1")
        elif "restart" in query:
            os.system("shutdoun /r /t 1")
        elif "play song" in query:
            song()
        elif "remember" in query:
            recuerdo(True)
        elif "do you know anything" in query:
            recuerdo(False)
        elif "screenshot" in query:
            screenshot()
        elif "computer" in query:
            diagnostico()
        elif "joke" in query:
            bromas()
        
            

