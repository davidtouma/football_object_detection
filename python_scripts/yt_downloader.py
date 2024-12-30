from pytube import YouTube
import os

def download(link):
    save_path = "Videos"

    if not os.path.exists(save_path):
        os.makedirs(save_path)


    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(output_path=save_path)
    except:
        print("Can't Download")
    print("Download Successfull")

link = input("Enter Youtube URL: ")
download(link)