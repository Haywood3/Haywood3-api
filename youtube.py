import youtube_dl

def download_youtube_video(url):
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print("Video downloaded:", info.get('title'))
    except Exception as e:
        print("Error:", str(e))

# Get the YouTube video URL from user input
video_url = input("Enter the YouTube video URL: ")

# Download the video
download_youtube_video(video_url)



# #!/usr/bin/env python
# import subprocess
# import os
# from multiprocessing import Pool

# def run(task):
#     print(task)
#     subprocess.call(["rsync", "-varq", task, dest])

# src = "data/prod/"
# dest = "data/prod_backup/"

# dir_tasks = [os.path.join(src, x) for x in os.listdir(src)]
# p = Pool(len(dir_tasks))
# p.map(run, dir_tasks)