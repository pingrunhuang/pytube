import sys
from pytube import YouTube
import os
import datetime


if __name__ == "__main__":
    output_dir = sys.argv[1]
    url = sys.argv[2]
    today = datetime.datetime.today()
    yt = YouTube(url)
    output_dir = os.path.join(output_dir, today.strftime("%Y%m%d"))
    streams = yt.streams.filter(file_extension='mp4')
    res = "1080p"
    vitag = 22
    aitag = 139
    for s in streams:
        if s.resolution == res:
            vitag = s.itag
    stream = yt.streams.get_by_itag(vitag)
    title = f"surfing 冲浪 | {yt.title} -- {yt.author}"
    desc = f"Originated from: {url}"
    stream.download(output_path=output_dir)
    print(title)
    print(desc)
    stream = yt.streams.get_by_itag(aitag)
    stream.download(output_path=output_dir, filename=f"{yt.title}.mp3") 