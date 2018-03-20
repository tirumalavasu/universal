from pytube import YouTube

YouTube(str(input("Enter the video link: "))).streams.first().download()


