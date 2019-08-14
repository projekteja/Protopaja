import subprocess

subprocess.call('vlc dshow://  --sout "#transcode{vcodec=none,acodec=mp3,ab=128,channels=2,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8080/}" :no-sout-all :sout-keep')

