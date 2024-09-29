import moviepy.editor as mp
import os
def extract_audio(videos_file_path):
    my_clip = mp.VideoFileClip(videos_file_path)
    my_clip.audio.write_audiofile(f'{videos_file_path}.mp3')



def traverse_path():
    for root, dirs, files in os.walk('F:\高中'):
        for file in files:
            print(os.path.join(root, file))
            if file.endswith("mp4"):
                extract_audio(os.path.join(root, file))
 

if __name__ == "__main__":
    traverse_path()




