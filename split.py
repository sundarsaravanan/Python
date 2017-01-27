#!usr/bin/env python
import pyaudio
import datetime
import wave

#write a function to split year into lowest parts

def play_audio(file_name):
    week_audio="date/"+file_name+".wav"
    chunk=1024
    f = wave.open(week_audio,"rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    data = f.readframes(chunk)
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()  


def thousand_split(num11):
    a=num11
    a1=a/100
    a=a-(a1*100)
    a2=a/10
    a2=a2*10
    a=a-a2
    strh='hundred'

    play_audio(str(a1))
    play_audio(str(strh))
    play_audio(str(a2))
    play_audio(str(a))







number=999843637

#  9 hundred 90  9 million 8 hundred forty three thousand six thirty seven

if(number>=1000000):
    i=1000000
elif(number>1000):
    i=1000
elif(number>1):
    i=1
num=number
num1=num/i
num=num-(num1*i)
i=i/1000
num2=num/i
num=num-(num2*i)



print number
thousand_split(num1)
play_audio('million')
thousand_split(num2)
play_audio('thousand')
thousand_split(num)
