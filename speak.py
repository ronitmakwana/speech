import vosk
import json
import pyaudio


def listen():


    model1 = vosk.Model(lang="en-us")
    reco = vosk.KaldiRecognizer(model1, 16000)

    cap = pyaudio.PyAudio()
    stream = cap.open(format=pyaudio.paInt16, channels=1,
                    rate=16000, input=True, frames_per_buffer=8192)
    
    stream.start_stream()
    while True:
        data = stream.read(4096)
        
        
        if len(data) == 0:
            break
        
        if reco.AcceptWaveform(data):
           
            s = reco.Result()

            dic = json.loads(s)
            x = dic.values()
            lt = list(x)
            for j in lt:
                print(j)
                return j
                # if j == 'stop':
                # return j
                    # stream.stop_stream()
        # else:
        
        #     print(reco.PartialResult())
        #     print('mid')
       


# def text2int(textnum, numwords={}):
#     if not numwords:
#       units = [
#         "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
#         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
#         "sixteen", "seventeen", "eighteen", "nineteen",
#       ]

#       tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

#       scales = ["hundred", "thousand", "million", "billion", "trillion"]

#       numwords["and"] = (1, 0)
#       for idx, word in enumerate(units):    numwords[word] = (1, idx)
#       for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
#       for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

#     current = result = 0
#     for word in textnum.split():
#         if word not in numwords:
#           raise Exception("Illegal word: " + word)

#         scale, increment = numwords[word]
#         current = current * scale + increment
#         if scale > 100:
#             result += current
#             current = 0

#     return result + current

# print (text2int("one hundred seven five"))

def lati():
    l= []
    lo =[]
    t = 'lat'
    txt = 'two three zero six one four seven two five six five six'
    sp = txt.split()
    for  i in sp:
        if t == 'lat':

            if i == 'one':
                l.append('1')
            
            elif i == 'two':
                l.append('2')

            elif i == 'three':
                l.append('3')
            
            elif i == 'four':
                l.append('4')
            
            elif i == 'five':
                l.append('5')
            
            elif i == 'six':
                l.append('6')
            
            elif i == 'seven':
                l.append('7')
            
            elif i == 'eight':
                l.append('8')
            
            elif i == 'nine':
                l.append('9')
            
            elif i == 'zero':
                l.append('0')        
    
        elif t == "long":

            if i == 'one':
                lo.append('1')
            
            elif i == 'two':
                lo.append('2')

            elif i == 'three':
                lo.append('3')
            
            elif i == 'four':
                lo.append('4')
            
            elif i == 'five':
                lo.append('5')
            
            elif i == 'six':
                lo.append('6')
            
            elif i == 'seven':
                lo.append('7')
            
            elif i == 'eight':
                lo.append('8')
            
            elif i == 'nine':
                lo.append('9')
            
            elif i == 'zero':
                lo.append('0')        

    if t == 'lat':
        s=''
        j = s.join(l)
        lat = j[:2]+'.'+j[2:6]+','+j[6:8]+'.'+j[8:]
        sl=lat.split(',')
        print(sl)
        return sl
    # elif t == 'long':
    #     s=''
    #     j = s.join(lo)
    #     long = j[:2]+'.'+j[2:]
    #     print(long,'----')
    #     return long
# lati()
