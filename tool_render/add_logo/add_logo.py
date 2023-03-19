import os
import subprocess


logo_path = "C:\\Users\\Administrator\\Desktop\\LEGO_logo.svg.png"
input = "C:\\Users\\Administrator\\Desktop\\20220704_114854_nature-72.mp4"
output = "output1.mp4"
logo_resize_path = "C:\\Users\\Administrator\\Desktop\\in_processing\\add_logo\\logo_resized.png"

# root_cpu_ffmpeg = "/usr/bin/ffmpeg -hide_banner -loglevel error -y"
command_logo_resize = f'ffmpeg -i {logo_path} -vf scale=320:240 logo_resized.png'


option = '-filter_complex "[0:v][1:v] overlay=x=25:y=25" -pix_fmt yuv420p -c:a copy'

command = f'ffmpeg -hide_banner -loglevel error -i "{input}" -i "{logo_resize_path}" {option} "{output}"'


def resize_logo():
    subprocess.call(command_logo_resize, shell=True)


def add_logo():
    subprocess.call(command, shell=True)


if __name__ == '__main__':
    resize_logo()
    add_logo()
