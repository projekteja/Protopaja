#!/bin/bash
cvlc v4l2:// :input-slave=alsa://hw:1,0 --sout "#transcode{vcodec=none,acodec=mp3,ab=312,channels=1,samplerate=44100,scodec=none}:http{mux=mp3,dst=:8083/}" :no-sout-all :sout-keep
