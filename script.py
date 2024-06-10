from pytube import YouTube

def listResolutions(yt):
    streams = yt.streams.filter(progressive=True).order_by('resolution')
    stream_list = list(streams)
    
    print("\nAvailable video streams:")
    for i, stream in enumerate(stream_list):
        print(f"{i + 1}. Resolution: {stream.resolution}, Format: {stream.mime_type.split('/')[1]}")
    
    return stream_list

def download(url, destination):
    try:
        yt = YouTube(url)

        streams = listResolutions(yt)
        choice = int(input("\nEnter the number of the stream you want to download: "))
        choice = streams[choice - 1]
        print(f"\nDownloading: {yt.title} in {choice.resolution} resolution")
        
        choice.download(destination)
        
        print("Download completed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")


url = input("Enter the YouTube video URL: ")
destination = "/Users/dharmin/Downloads"
print("'.' for current directory, empty for default")
destination = input(f"Enter the destination path: ") or destination

download(url, destination)