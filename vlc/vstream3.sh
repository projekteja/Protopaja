#!/bin/bash
cvlc v4l2:///dev/video4:width=640:height=480:fps=5 --sout "#transcode{vcodec=mp2v,vb=3000,acodec=none,scodec=none}:http{mux=ts,dst=:8082/}" :no-sout-all :sout-keep
