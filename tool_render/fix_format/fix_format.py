import subprocess
import os
import math


# input = "C:\\Users\\Administrator\\Desktop\\in_processing\\assemble\\temp_video.mp4"
# ffprobe -i {input} -show_entries format=duration -v quiet -of csv="p=0
output = "output"
input = r'C:\Users\Administrator\Desktop\in_processing\assemble\temp_audio.mp3'

# command = f'ffmpeg -y -vsync 0 -hwaccel cuda -hwaccel_output_format cuda -i {input} -c:a copy -c:v h264_nvenc -b:v 5M {output}.mp4'
command = f'ffprobe -i {input} -show_entries format=duration -v quiet -of csv="p=0"'
# duration =
# echo "Duration is $duration seconds."


def fix_format():
    # subprocess.call(command, shell=True)
    pipe = float(subprocess.getoutput(command))
    a = 3
    print(type(a))
    print(type(pipe))
    print(pipe)


if __name__ == '__main__':
    fix_format()
