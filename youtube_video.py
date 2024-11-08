from yt_dlp import YoutubeDL
import subprocess
import os

def download_video(video_url, output_filename):
    # Configuring yt-dlp for video download
    ydl_opts = {
        'format': 'bestvideo+bestaudio',  # Downloads the best video and audio available
        'merge_output_format': 'mp4',     # Merges the video and audio into an MP4 file
        'outtmpl': f"{output_filename}",  # Defines the output filename
    }

    # Downloading the video
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Taking user inputs (link,name) and calling the function
video_url = input("Enter the video link : ")
name = input("Name your video file : ")
download_video(video_url, "output_file.mp4")

# Making a copy with the audio format AAC instead of default Oups (Oups cant be decoded in regular video players)
subprocess.run([
    'ffmpeg', '-i', 'output_file.mp4', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '128k', f'{name}.mp4'
])

# Removing the file with Oups audio
os.remove("output_file.mp4")