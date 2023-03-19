import os
import subprocess


import datetime
import subprocess

input_arr_audio = ['C:\\Users\\Administrator\\Desktop\\a\\01-linkinparkkiiara-heavyfeat.kiiara.mp3',
                   'C:\\Users\\Administrator\\Desktop\\a\\02-linkinpark-intheend.mp3',
                   'C:\\Users\\Administrator\\Desktop\\a\\03-linkinpark-numb.mp3',
                   'C:\\Users\\Administrator\\Desktop\\a\\20210310_081650_y2mate.com-westlifemyloveofficialvideov144p.mp4',
                   'C:\\Users\\Administrator\\Desktop\\a\\20210310_081810_y2mate.com-westlifemyloveofficialvideov144p.mp4']


class HandleAudio:

    def convert_to_mp3(audio_paths):
        # audio_paths là mảng chứa các đường dẫn
        input_aud_arr = []  # chứa đường dẫn các audio_path sau khi đã xử lí
        for audio_path in audio_paths:
            audio_extend = os.path.splitext(audio_path)[-1]
            audio_name = os.path.splitext(audio_path)[0]
            if audio_extend == ".mp3":
                input_aud_arr.append(audio_path)
            if audio_extend == ".mp4":
                command_convert = f'ffmpeg -i "{audio_path}" -vn -ar 44100 -ac 2 -b:a 192k "{audio_name}".mp3'
                subprocess.call(command_convert, shell=True)
                input_aud_arr.append(audio_name + ".mp3")

        return input_aud_arr

    def concat_audio(input_aud_arr):
        # input_aud_arr = []  # chứa đường dẫn các video
        # file txt lưu đường dẫn các file đầu vào
        file_in = "C:\\Users\\Administrator\\Desktop\\1.txt"
        file_out = "concated"  # audio đã xử lí xong

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


if __name__ == '__main__':

    # print(HandleAudio.convert_to_mp3(input_arr_audio))
    HandleAudio.run()
