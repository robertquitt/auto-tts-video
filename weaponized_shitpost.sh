#!/bin/bash

cat shitpost ./emoji_translator.py > shitpost_out
espeak -f shitpost_out -w audio.wav
ffmpeg -loop 1 -i image.jpg -i audio.mp3 -shortest -c:v libx264 -c:a aac result.mp4
