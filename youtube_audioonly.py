from yt_dlp import YoutubeDL

def download_youtube_audio(video_url, output_filename="output.mp3"):
    # Configuring yt-dlp to download audio 
    ydl_opts = {
        'format': 'bestaudio/best',               # Downloads only audio and in best form
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',          # Converts to mp3 using FFmpeg
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f"{output_filename}.%(ext)s",  # Defining output template
    }

    # Downloading the file
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# Taking user inputs (link,name) and calling the function
video_url = input("Enter the video link : ")
y = input("Name your audio file : ")
download_youtube_audio(video_url, y)
