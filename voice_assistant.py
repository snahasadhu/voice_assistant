import speech_recognition as sr
import os

print('Virtual Assistant is ready to help you:\n')
while True:
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        audio_input = recognizer.recognize_google(audio)
        print('You just said: ')
        print(audio_input)

        reply_dict = {
            'how are you': 'I am good',
            'What is your name': 'My name is Snaha',
            'What is my teacher name': 'M Firoz Mridha',
            'open browser': ' i opened browser for u',
            'close browser': ' i closed browser for u',
            'calculator chalu karo': 'calculator chalu kara hoyeche',
            'calculator Ti bondho karo': 'calculator bondho kara hoyeche',
            'open notepad': 'notepad opened',
            'close notepad': 'notepad closed',
            'open wordpad': 'wordpad opened',
            'close wordpad': 'wordpad closed'
        }

        from difflib import SequenceMatcher

        for key, value in reply_dict.items():
            ratio = SequenceMatcher(None, audio_input, key).ratio()

            if ratio > .85:
                print(value)
                if key == 'calculator chalu karo':
                    # starting calculator process of the system
                    os.system("start calc.exe")
                elif key == 'calculator Ti bondho karo':
                    os.system("taskkill /im Calculator.exe /f")
                elif key == 'open notepad':
                    os.system("start notepad.exe")
                elif key == 'close notepad':
                    os.system("taskkill /im notepad.exe /f")
                elif key == 'open wordpad':
                    os.system("start wordpad.exe")
                elif key == 'close wordpad':
                    os.system("taskkill /im wordpad.exe /f")
                elif key == 'open browser':
                    os.system("start msedge.exe")
                elif key == 'close browser':
                    os.system("taskkill /im msedge.exe /f")

                ratio = 0

    except Exception as e:
        continue


