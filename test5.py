import os
from moviepy.editor import VideoFileClip

def video_to_audio(video_path, audio_path):
    print("test")
    video_clip = VideoFileClip(video_path)
    audio = video_clip.audio
    audio.write_audiofile(audio_path)


def traverse_path():
    for root, dirs, files in os.walk('E:\BaiduNetdiskDownload\韦昭尤寻龙点穴高清现场教学全套视频'):
        for file in files:
            print(os.path.join(root, file))
            video_to_audio(file, "E:\BaiduNetdiskDownload")
 

if __name__ == "__main__":
    traverse_path()






