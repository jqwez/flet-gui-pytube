from pytube import YouTube

import os
from pathlib import Path

def get_video(url, save_location):
    try:
        print("try")
        filename = str(Path(save_location).name)
        output_path = str(os.path.split(Path(save_location))[0])
        print(filename)
        print(output_path)
        download = YouTube(url)
        stream = download.streams.filter(progressive=True).get_highest_resolution()
        stream.download(filename=filename, output_path=output_path)
        return  
    except:
        error = True
        print("something wrong")
        return "Something went wrong"
        

if __name__ == "__main__":
    filetype = "mp4"
    url = input("Please enter URL: ")
    get_video(url, filetype)