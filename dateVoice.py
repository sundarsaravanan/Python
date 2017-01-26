#!usr/bin/env python
import pyaudio
import datetime
import wave



#write a function to split year into lowest parts


def year_split(year1):
    play_audio(str(2))
    play_audio('thousand')
    play_audio(str(17))





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


year=datetime.date.today().strftime("%Y")
day=datetime.date.today().strftime("%d")
month=datetime.date.today().strftime("%B")
week_day=datetime.date.today().strftime("%A")
hour=datetime.datetime.now().strftime("%I")
min=datetime.datetime.now().strftime("%M")
min=min.lstrip('0')
hour=hour.lstrip('0')
day=day.lstrip('0')


print "DATE: ", day,"-", month,"-", year,"-", week_day
print "Time:",hour,"-",min



play_audio('Today')
play_audio(month)
play_audio(day)
year_split(year)
play_audio(week_day)
play_audio(hour)
play_audio('Am')
play_audio(min)
play_audio('Minutes')
