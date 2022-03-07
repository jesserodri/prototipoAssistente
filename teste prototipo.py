import sys
import os,signal
import webbrowser as wb
import pyttsx3
import time
import sys
from random import randint
cont =0
import speech_recognition as sr
robo = pyttsx3.init()

falas_prox_tarefa = ['Se precisar de algo a mais me avise', 'caso queira mais algo, é só pedir ', 'precisando é só pedir',
                     'se quiser mais algo, não ezite em me pedir ']

rec = sr.Recognizer()





#wb.open_new("https://www.youtube.com/")

#print(sys.platform)
tempo = time.strftime("dia %d do %b, Agora são:  %H:%M")
hora = int(time.strftime('%H'))
dahora=time.strftime('%Hhoras e %Mminutos ')
if tempo:
    if hora < 12:
        robo.say("Bom dia Senhor, o que posso ajudar? ")
    if hora >= 12:
        robo.say("Boa Tarde Senhor, o que posso ajudar? ")

#robo.say("Olá JESSÉ, Sou sua assistente artificial teste, o que posso ajudar: ")

robo.runAndWait()
while True:
    num_falas = randint(0, len(falas_prox_tarefa)-1)

    if cont :
        robo.say(falas_prox_tarefa[num_falas])
        robo.runAndWait()

    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Fale o que deseja:", end=" ")
        audio = rec.listen(mic)
        op = rec.recognize_google(audio, language="pt-BR")
        print(op)


    #op = input("digite o que deseja abrir: ").lower().strip()
    if 'lol' in op:
        lol = os.startfile("C:/Riot Games/Riot Client/RiotClientServices")
        robo.say(f"o League of Legends vai abrir em instantes")
    elif 'valorant' in op:
        os.startfile("C:/Riot Games/Riot Client/RiotClientServices")
        robo.say(f"o Valoranti está para ser executado em instantes ")
    elif 'discord' in op :
        os.startfile("C:/Users/Daycão/Desktop/Discord.lnk")
        robo.say(f"Você acabou de abrir o Discorde ")
    elif op == 'epic':
        os.startfile("C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")
        robo.say(f"Você acabou de abrir a Epic Games")
    elif op == 'pycharm':
        os.startfile("C:/Program Files/JetBrains/PyCharm Community Edition 2021.3.2/bin/pycharm64.exe")
        robo.say(f"pycharm está sendo executado")
    elif 'data' in op:
        robo.say(tempo)
    elif 'hora' in op:
        robo.say(f"agora é :{dahora}")
        if hora > 12:
            robo.say(f"Uma bela tarde insolarada")
    elif 'Twitch' in op:
        wb.open_new("https://dashboard.twitch.tv/u/daycao/stream-manager")
    elif 'Netflix' in op:
        wb.open_new("https://netflix.com")
    elif 'disney' in op :
        wb.open_new('https://disneyplus.com/pt-br/home')
    elif 'o que é voce' in op:
        robo.say('Sou um prototipo do senhor Jessé')



    '''msg_robo = op
    robo.say(f"Você acabou de abrir o {op} ")
    '''
    robo.runAndWait()
    cont+=1
