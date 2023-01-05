from pytube import YouTube, request

import os
from pathlib import Path

request.default_range_size = 500000

def get_video(url, save_location, in_progress, on_complete, handle_error):

    try:
        filename = str(Path(save_location).name)
        output_path = str(os.path.split(Path(save_location))[0])
        print(filename)
        print(output_path)
        download = YouTube(url, on_progress_callback=in_progress, on_complete_callback=on_complete)
        stream = download.streams.filter(progressive=True).get_highest_resolution()
        stream.download(filename=filename, output_path=output_path)
        return  
    except:
        error = True
        handle_error()
        return
        

if __name__ == "__main__":
    filetype = "mp4"
    url = input("Please enter URL: ")
    get_video(url, "./")