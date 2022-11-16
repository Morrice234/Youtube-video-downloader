# Youtube-video-downloader
This is a simple python code that you can use to download a youtube video
This script allows you to enter the URL of the video you want to download, then it will list all the video streams and
allow you to enter the video stream you want.
## NOTE:
I used the 'get_by_itag()' attribute to select the stream so you have to enter the itag value

If you entered the valid itag value the script will proceed to download the video file and move it to the specified directory in the 'download()' method

# Packages used
pytube
# Installing pytube
pip install pytube

# running the script
Open command prompt and navigate to the folder where your file is stored and type the following:
python youtube.py


