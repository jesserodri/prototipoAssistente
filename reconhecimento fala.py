import speech_recognition as sr

#reconhecedor das falas
rec = sr.Recognizer()

'''
for i in sr.Microphone().list_microphone_names():

 print(i)
'''

# se usa o with pois apartir do momento que sair desse bloco ele vai fechar sem precisar usar mic.close()
with sr.Microphone(1) as mic:
    #o computador não entende o que é barulho\ruido simplesmente pelo som mas se ele indentifica o ruido e o separa
    #tudo que for maior que o ruido é um audio
    rec.adjust_for_ambient_noise(mic)
    print("pode falar que eu vou gravar")

    #ouvindo nosso audio
    audio = rec.listen(mic)

    #reconhecer nosso audio e traduzir em um texto
    texto = rec.recognize_google(audio, language="pt-BR")

    #mostre o texto
    print(texto)


'''
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("pode falar que eu vou gravar")
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
'''
