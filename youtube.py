from pytube import YouTube


link = input("Enter the Url: ")
video = YouTube(link)

title = video.title

allStreams = video.streams.all()

for i in range(len(allStreams)):
    print(allStreams[i])

quality = input("Enter video Quality: ")

print("Downloading...")

selected_video_quality = video.streams.get_by_itag(quality)

selected_video_quality.download('./Youtube')

print("Video downloaded successfully")
