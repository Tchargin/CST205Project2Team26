# Multimedia Programming Project 2 Fighting Scene Soundboard + Filter
from moviepy.editor import *
Fightscene = VideoFileClip("C:/Project2/Killbill.mp4", audio=False).subclip(59, 200)
Fightscene.preview()
