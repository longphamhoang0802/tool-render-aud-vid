import subprocess


def run(audio, video):
    command_dur_aud = f'ffprobe -i {audio} -show_entries format=duration -v quiet -of csv="p=0"'
    print(command_dur_aud)
    command_dur_vid = f'ffprobe -i {video} -show_entries format=duration -v quiet -of csv="p=0"'
    print(command_dur_vid)
    pipe_aud = (subprocess.getoutput(command_dur_aud))
    pipe_vid = (subprocess.getoutput(command_dur_vid))
    if (pipe_aud >= pipe_vid):
        result_video = Render.merge1(HandleAudio.run(), HandleAudio.run())
        return result_video
    else:
        result_video = Render.merge2(HandleAudio.run(), HandleAudio.run())
        return result_video


_audio = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_audio.mp3"
_video = r"C:\Users\Administrator\Desktop\in_processing\assemble\temp_video.mp4"

run(_audio, _video)
