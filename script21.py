# Function to download any video from YouTube.
from pytube import YouTube
from sys import argv

link = argv[1]
YouTube = YouTube(link)

print("Title: ", YouTube.title)
print("Views: ", YouTube.views)

YouTube_Destination = YouTube.streams.get_highest_resolution().download()