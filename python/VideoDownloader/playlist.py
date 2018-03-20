from pytube import Playlist
pl = Playlist(str(input("Enter the video link: ")))
destination = str(input("Enter the destination: "))
pl.download_all(destination)
