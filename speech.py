import speech_recognition as sr
import os
import re
import shutil

r = sr.Recognizer()

list = ['india','google','facebook']
list1 =['microsoft','youtube','china']
# end = True

while(True):
    PATH = str(input("Enter path : "))
    try:
        with sr.AudioFile(PATH) as source:
            audio = r.record(source)
            # print(r.recognize_sphinx(audio))

            # audio = r.record(source)
            # r.adjust_for_ambient_noise(source, duration=0.2)
            # audio = r.listen(source)
            # print("Recognizing...")
            text = r.recognize_sphinx(audio)
            text = text.lower()
            print("you said :"+(text))
            word =  re.split('\s+', text)
            # chars = [c for c in text]
            print(word)
            for i in word:
                if i.lower() in list:
                    filename = 'C:\\Users\\Administrator\\Downloads\\google\\files.txt'
                    with open(filename, "a") as f:
                        f.write(i)
                        f.write(', ')
                        shutil.move(PATH, 'C:\\Users\\Administrator\\Downloads\\google')
                        

                     
                    # with open(filename, "w") as f:
                    #     f.write(text)
                    print("saved")
                elif i.lower() in list1:
                    filename = 'C:\\Users\\Administrator\\Downloads\\china\\files.txt'
                    with open(filename, "a") as f:
                        f.write(i)
                        f.write(', ')
                        shutil.move(PATH, 'C:\\Users\\Administrator\\Downloads\\china')
                    print("saved")
                # elif i.lower() in list and list1:
                #     filename = 'C:\\Users\\Administrator\\Downloads\\google\\files.txt'
                #     with open(filename, "a") as f:
                #         f.write(i)
                #         f.write(', ')
                #         shutil.move(PATH, 'C:\\Users\\Administrator\\Downloads\\google')
                #     print("saved")

    except:
        # print(list)
        print("could not understand")
        end = str(input("Write '"'exit'"' to stop or '"'pass'"' to continue : "))
      
        if end=="exit":
            break
        elif end=="pass":
            pass
    
