from pytube import YouTube

def get_video(url, filetype):
    try:
        
        download = YouTube(url)
        stream = download.streams.filter(progressive=True, file_extension=filetype).get_highest_resolution()
        stream.download()
        return  
    except:
        error = True
        return "Something went wrong"
        

if __name__ == "__main__":
    filetype = "mp4"
    url = input("Please enter URL: ")
    get_video(url, filetype)