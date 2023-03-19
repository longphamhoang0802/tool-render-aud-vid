import subprocess
import os


input = "C:\\Users\\Administrator\\Desktop\\20220704_114854_nature-72.mp4"
output = "output.txt"

command = f'ffmpeg -y -hwaccel cuda -threads 16 -hide_banner -loglevel error -i "{input}" -f ffmetadata "{output}"'


def fix_metadata():
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    fix_metadata()
