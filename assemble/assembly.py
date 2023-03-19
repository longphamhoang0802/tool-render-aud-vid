import os
import subprocess


import datetime
import subprocess

input_arr_audio = ['C:\\Users\\Administrator\\Desktop\\a\\01-linkinparkkiiara-heavyfeat.kiiara.mp3',
                   'C:\\Users\\Administrator\\Desktop\\a\\02-linkinpark-intheend.mp3',
                   'C:\\Users\\Administrator\\Desktop\\a\\03-linkinpark-numb.mp3',
                   'C:\\Users\\Administrator\\Desktop\\a\\20210310_081650_y2mate.com-westlifemyloveofficialvideov144p.mp4',
                   'C:\\Users\\Administrator\\Desktop\\a\\20210310_081810_y2mate.com-westlifemyloveofficialvideov144p.mp4']

input_video_array = ['C:\\Users\\Administrator\\Desktop\\b\\videoplayback.mp4',
                     'C:\\Users\\Administrator\\Desktop\\b\\videoplayback1.mp4',
                     'C:\\Users\\Administrator\\Desktop\\b\\file_637599553230621736.mp4']

logo_path = "C:\\Users\\Administrator\\Desktop\\LEGO_logo.svg.png"
logo_resize_path = "C:\\Users\\Administrator\\Desktop\\in_processing\\assemble\\logo_resized.png"


class HandleAudio:

    def convert_to_mp3(audio_paths):
        # audio_paths là mảng chứa các đường dẫn
        input_aud_arr = []  # chứa đường dẫn các audio_path sau khi đã xử lí
        for audio_path in audio_paths:
            audio_extend = os.path.splitext(audio_path)[-1]
            audio_name = os.path.splitext(audio_path)[0]
            if audio_extend == ".mp3":
                input_aud_arr.append(audio_path)
            if audio_extend == ".mp4" or audio_extend == ".wav":
                command_convert = f'ffmpeg -i "{audio_path}" -vn -ar 44100 -ac 2 -b:a 192k "{audio_name}".mp3'
                subprocess.call(command_convert, shell=True)
                input_aud_arr.append(audio_name + ".mp3")

        return input_aud_arr

    def concat_audio(input_aud_arr):
        # input_aud_arr = []  # chứa đường dẫn các video
        # file txt lưu đường dẫn các file đầu vào
        file_in = "C:\\Users\\Administrator\\Desktop\\1.txt"
        file_out = "temp_audio"  # audio đã xử lí xong

        with open(file_in, 'w') as f:
            for audio in input_aud_arr:
                f.write("file " + "'" + audio + "'")
                f.write('\n')
            f.close()

        command_concat = f'ffmpeg -f concat -safe 0 -i {file_in} -c copy {file_out}.mp3'
        subprocess.call(command_concat, shell=True)

        return file_out

    def run():
        temp_audio_arr = HandleAudio.convert_to_mp3(input_arr_audio)
        temp_audio = HandleAudio.concat_audio(temp_audio_arr)
        print('done Handle-audio')
        return temp_audio


class HandleVideo:

    def concat_video(input_vid_arr):

        # input_vid_arr = []  # chứa đường dẫn các video
        # file txt lưu đường dẫn các file đầu vào
        file_in = "C:\\Users\\Administrator\\Desktop\\2.txt"
        file_out = "concated_v"  # video đã xử lí xong

        with open(file_in, 'w') as f:
            for video in input_vid_arr:
                f.write("file " + "'" + video + "'")
                f.write('\n')
            f.close()

        command_concat = f'ffmpeg -f concat -safe 0 -i {file_in} -c copy {file_out}.mp4'
        subprocess.call(command_concat, shell=True)
        # Process.write_log(text="Done concat-video")
        return file_out

    def run():
        temp_video = HandleVideo.concat_video(input_video_array)
        temp_video = SettingVideo.add_logo(temp_video)
        # if logo == None:
        #     return
        temp_video = SettingVideo.set_bitrate(temp_video)
        # temp_video = SettingVideo.fix_format(temp_video)
        print('done Handle-video')
        return temp_video


class SettingAudio:
    input = ""
    output = ""

    def __init__(self, input, output):
        self.input = input
        self.output = output

    def cut_audio(self):
        self.update_stt()
        start_time = datetime.time(0, 2, 15)  # thời điểm bắt đầu
        duration_time = datetime.time(0, 2, 36)  # khoảng thời gian
        command_cut_aud = f'ffmpeg -i {self.input} -ss {start_time} -t {duration_time} -acodec copy {self.output}.mp3'
        subprocess.call(command_cut_aud, shell=True)


class SettingVideo:
    def cut_video(self):

        start_time = datetime.time(0, 2, 15)
        end_time = datetime.time(0, 2, 36)

        if (end_time.hour < start_time.hour):
            print("nhap lai thoi gian")
        elif (end_time.hour > start_time.hour):
            command_cut = f'ffmpeg -ss {start_time} -to {end_time} -i {self.input} -c copy {self.output}.mp4'
            subprocess.call(command_cut, shell=True)
            print("ok")
        else:
            if (end_time.minute < start_time.minute):
                print("nhap lai thoi gian")
            elif (end_time.minute > start_time.minute):
                command_cut = f'ffmpeg -ss {start_time} -to {end_time} -i {self.input} -c copy {self.output}.mp4'
                subprocess.call(command_cut, shell=True)
                print("ok")
            else:
                if (end_time.second < start_time.second):
                    print("nhap lai thoi gian")
                elif (end_time.second > start_time.second):
                    command_cut = f'ffmpeg -ss {start_time} -to {end_time} -i {self.input} -c copy {self.output}.mp4'
                    subprocess.call(command_cut, shell=True)
                    print("ok")
                else:
                    print("nhap lai thoi gian")
        # Process.write_log(text="Done cut-video")

    def add_logo(file_out):
        # đường dẫn của file_out concat_video
        input = "C:\\Users\\Administrator\\Desktop\\in_processing\\assemble\\concated_v.mp4"
        output = "added_logo.mp4"
        # root_cpu_ffmpeg = "/usr/bin/ffmpeg -hide_banner -loglevel error -y"
        command_logo_resize = f'ffmpeg -i {logo_path} -vf scale=320:240 logo_resized.png'
        option = '-filter_complex "[0:v][1:v] overlay=x=25:y=25" -pix_fmt yuv420p -c:a copy'
        command_add = f'ffmpeg -hide_banner -loglevel error -i "{input}" -i "{logo_resize_path}" {option} "{output}"'
        subprocess.call(command_logo_resize, shell=True)
        subprocess.call(command_add, shell=True)
        # Process.write_log(text="Done add-logo-video")
        return output

    def set_bitrate(added_logo):
        input = "C:\\Users\\Administrator\\Desktop\\in_processing\\assemble\\added_logo.mp4"
        output = "temp_video.mp4"
        num = 5
        # command_show = f'ffprobe -i {self.input} -show_entries format=bit_rate -v quiet -of csv="p=0"'
        # print(command_show)
        command_change = f'ffmpeg -i {input} -b:v {num}M -acodec copy {output}'

        # subprocess.call(command_show, shell=True)
        subprocess.call(command_change, shell=True)
        # Process.write_log(text="Done set-bitrate-video")
        return output

    # def fix_format(setted_bitrate):
    #     input = 'C:\\Users\\Administrator\\Desktop\\in_processing\\assemble\\setted_bitrate.mp4'
    #     output = 'temp_video'
    #     command_fix = f'ffmpeg -y -vsync 0 -hwaccel cuda -hwaccel_output_format cuda -i {input} -c:a copy -c:v h264_nvenc -b:v 5M {output}.mp4'
    #     subprocess.call(command_fix, shell=True)
    #     # Process.write_log(text="Done fix-format-video")
    #     return output


class Render:
    # tham số phải sửa thành đường dẫn: audio, video
    def merge1():
        audio = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_audio.mp3"
        video = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_video.mp4"
        option = '-c copy -map 0:0 -map 0:v -map 1:a -shortest'
        output = 'result.mp4'
        command_merge1 = f'ffmpeg -stream_loop -1 -i {video} -i {audio} {option} {output}'
        subprocess.call(command_merge1, shell=True)
        return output

    def merge2():
        audio = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_audio.mp3"
        video = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_video.mp4"
        option = '-c copy -map 0:0 -map 0:v -map 1:a -shortest'
        output = 'result.mp4'
        command_merge2 = f'ffmpeg -i {video} -i {audio} {option} {output}'
        subprocess.call(command_merge2, shell=True)
        return output

    def run():
        audio1 = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_audio.mp3"
        video1 = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_video.mp4"
        command_dur_aud = f'ffprobe -i {audio1} -show_entries format=duration -v quiet -of csv="p=0"'
        command_dur_vid = f'ffprobe -i {video1} -show_entries format=duration -v quiet -of csv="p=0"'
        pipe_aud = float(subprocess.getoutput(command_dur_aud))
        pipe_vid = float(subprocess.getoutput(command_dur_vid))

        if (pipe_aud >= pipe_vid):
            result_video = Render.merge1()
            return result_video
        else:
            result_video = Render.merge2()
            return result_video


if __name__ == '__main__':
    HandleAudio.run()
    HandleVideo.run()
    Render.run()
