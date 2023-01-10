import json

from yt_extractor import get_video_infos,get_audio_url
from api_communication import save_transcript

def save_video_sentiments(url):
    video_infos=get_video_infos(url)
    audio_url=get_audio_url(video_infos)
    print(audio_url)
    title=video_infos["title"]
    title=title.strip().replace(" ","_")
    save_transcript(audio_url,title,sentiment_analysis=True)

    filename=title+"_sentiment.json"
    with open(filename,'r') as f:
        data=json.load(f)

    positives=[]
    negetives=[]
    neutrals=[]

    for result in data:
        text=result['text']
        if result['sentiment']=="POSITIVE":
            positives.append(text)
        if result['sentiment']=="NEGATIVE":
            negetives.append(text)
        if result['sentiment']=="NEUTRAL":
            neutrals.append(text)
    
    n_pos=len(positives)
    n_neg=len(negetives)
    n_neu=len(neutrals)

    print("Number of positive sentiment:",n_pos)
    print("Number of negetive sentiment:",n_neg)
    print("Number of neutral sentiment:",n_neu)

    r=n_pos/(n_pos+n_neg)
    print("Ratings is:",r)

if __name__ == "__main__":
    save_video_sentiments("https://youtu.be/D_FClmOULUo")

    