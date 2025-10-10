import yt_dlp

def download_video(url, save_path):
    try:
        ydl_opts = {
            'format': 'mp4',  # force progressive MP4
            'outtmpl': f'{save_path}/%(title)s.%(ext)s'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Video downloaded successfully!")

    except Exception as e:
        print("Error:", e)


url = "https://youtu.be/hbRgHyHNVag"
save_path = "C:/Users/DELL/Downloads"
download_video(url, save_path)
