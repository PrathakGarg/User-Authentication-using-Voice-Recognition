import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source)
    print('now say')
    audio = r.listen(source)
    print(r.recognize_google(audio))