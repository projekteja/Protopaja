#!/bin/bash
cvlc alsa://plughw:1,0 --sout "#transcode{acodec=mp3,ab=128, scodec=none, vcodec=none, channels=1, samplerate=44100}:http{mux=mp3,dst=:8083/}" :no-sout-all :sout-keep
