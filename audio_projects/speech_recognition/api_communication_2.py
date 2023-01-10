import json
from logging.config import listen
from os import system
from pprint import pprint
import requests
from api import API_KEY
from os import system
from time import sleep

upload_endpoin='https://api.assemblyai.com/v2/upload'
transcribe_endpoint = "https://api.assemblyai.com/v2/transcript"
transcript_headers = {'authorization': API_KEY}

listen_notes_episode_endPoint="url = 'https://listen-api.listennotes.com/api/v2/episodes"
listen_notes_headers = {
  'X-ListenAPI-Key': '<SIGN UP FOR API KEY>',
}
def get_episode_audio_url(episode_id):
    url=listen_notes_episode_endPoint + '/' + episode_id
    response = requests.request('GET', url, headers=listen_notes_headers)
    data=response.json()
    pprint.pprint(data)
    audio_url=data['audio']
    episode_thumbnail=data['thumbnail']
    podcast_title=data['podcast']['title']
    episode_title=data['title']
    return audio_url,episode_thumbnail,podcast_title,episode_title

#upload a file
def upload(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break  

                yield data

    
    upload_response = requests.post(upload_endpoin,
                            headers=transcript_headers,
                            data=read_file(filename))

    audio_url=upload_response.json()['upload_url']
    return audio_url

#transcribe
def transcribe(audio_url,auto_chapters):
    transcript_request = { 
        "audio_url": audio_url,
        'auto_chapters':auto_chapters
        }
    transcript_response = requests.post(transcribe_endpoint,json=transcript_request, headers=transcript_headers)
    job_id=transcript_response.json()['id']
    return job_id

#polling
def polling(transcript_id):
    polling_endpoint=transcribe_endpoint + '/' + transcript_id
    polling_response=requests.get(polling_endpoint,headers=transcript_headers)
    return polling_response.json()

def get_transcription_result(audio_url,auto_chapters):
    transcript_id=transcribe(audio_url,auto_chapters)
    i=0
    while True:
        _=system('clear')
        if i%4==0:
            print("Processing")
            sleep(20/1000)
        if i%4==1:
            print("Processing.")
            sleep(20/1000)
        if i%4==2:
            print("Processing..")
            sleep(20/1000)
        if i%4==3:
            print("Processing...")
            sleep(20/1000)
        i=i+1
        data=polling(transcript_id)
        if data['status'] == 'completed':
            return data,None
        elif data['status'] == 'error':
            return data,data['error']

def save_transcript(episode_id):
    audio_url,episode_thumbnail,podcast_title,episode_title=get_episode_audio_url(episode_id)

    data,error=get_transcription_result(audio_url,auto_chapters=True)
    if data:
        with open(episode_id+".txt","w") as f:
            f.write(data['text'])
        print("Transcription is successful")

        with open(episode_id+"_chapter.txt",'w') as i:
            chapters=data['chapters']

            episode_data={'chapters':chapters}
            episode_data['episode_thumbnail']=episode_thumbnail
            episode_data['episode_title']=episode_title
            episode_data['podcast_title']=podcast_title

            json.dump(episode_data,f)
            print("Transcription is saved")
            return True
    elif error:
        print("Error in transcription",error)
        return False