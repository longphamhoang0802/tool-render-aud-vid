import json
import os
import shutil
import datetime
import subprocess


input = "C:\\Users\\Administrator\\Desktop\\lol.mp4"
output = "output"

start_time = datetime.time(0, 2, 15)
end_time = datetime.time(0, 2, 36)


def cut_video():
    if (end_time.hour < start_time.hour):
        print("nhap lai thoi gian")
    elif (end_time.hour > start_time.hour):
        command_cut = f'ffmpeg -ss {start_time} -to {end_time} -i {input} -c copy {output}.mp4'
        subprocess.call(command_cut, shell=True)
        print("ok")
    else:
        if (end_time.minute < start_time.minute):
            print("nhap lai thoi gian")
        elif (end_time.minute > start_time.minute):
            command_cut = f'ffmpeg -ss {start_time} -to {end_time} -i {input} -c copy {output}.mp4'
            subprocess.call(command_cut, shell=True)
            print("ok")
        else:
            if (end_time.second < start_time.second):
                print("nhap lai thoi gian")
            elif (end_time.second > start_time.second):
                command_cut = f'ffmpeg -ss {start_time} -to {end_time} -i {input} -c copy {output}.mp4'
                subprocess.call(command_cut, shell=True)
                print("ok")
            else:
                print("nhap lai thoi gian")


if __name__ == '__main__':
    print(start_time)
    cut_video()
