import os
from pathlib import Path
import subprocess

path = "C:\\Users\\Administrator\\Desktop\\um4k.mp4"
num = 5
output = "um_output1"

command_show = f'ffprobe -i {path} -show_entries format=bit_rate -v quiet -of csv="p=0"'
# print(command_show)

command_change = f'ffmpeg -i {path} -b:v {num}M -acodec copy {output}.mp4'


def show():
    subprocess.call(command_show, shell=True)


def change():
    subprocess.call(command_change, shell=True)


if __name__ == '__main__':
    show()
    change()
    # subprocess.call(
    #     'ffprobe -i C:\\Users\\Administrator\\Desktop\\lol.mp4 -show_entries format=bit_rate -v quiet -of csv="p=0"', shell=True)
