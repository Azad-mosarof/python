import youtube_dl

ydl=youtube_dl.YoutubeDL()

def get_video_infos(url):
    with ydl:
        result=ydl.extract_info(
            url,
            download=False
        )
    if "entries" in result:
        return result["entries"][0]
    return result


def get_audio_url(video_infos):
    for i in video_infos["formats"]:
        if i["ext"] == "m4a":
            return i["url"]

if __name__== "__main__":
    video_infos=get_video_infos("https://www.youtube.com/watch?v=mYUyaKmvu6Y")
    audio_infos=get_audio_url(video_infos)
    print(audio_infos)
