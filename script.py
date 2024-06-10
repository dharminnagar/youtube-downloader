from pytube import YouTube

def download(url, destination="."):
    try:
        yt = YouTube(url)
        
        ys = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")
        
        ys.download(destination)
        print("Download completed!")
    
    except Exception as e:
        print(f"An error occurred: {e}")


url = input("Enter the YouTube video URL: ")
destination = "/Users/dharmin/Downloads"
print("'.' for current directory, empty for default")
destination = input(f"Enter the destination path: ") or destination

download(url, destination)