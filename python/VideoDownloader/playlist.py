import os
import time
from pytube import Playlist
from pytube import YouTube

def download_youtube_playlist(playlist_url, destination):
    if not os.path.exists(destination):
        os.makedirs(destination)
    
    playlist = Playlist(playlist_url)
    
    for i, url in enumerate(playlist.video_urls):
        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            video.download(destination)
            print(f"Downloaded {i + 1}/{len(playlist.video_urls)}: {yt.title}")

            # Add a delay between downloads
            time.sleep(10)
        except Exception as e:
            print(f"Error downloading video: {url}")
            print(e)

if __name__ == "__main__":
    playlist_url = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
    destination = "path/to/your/destination/folder"
    download_youtube_playlist(playlist_url, destination)

