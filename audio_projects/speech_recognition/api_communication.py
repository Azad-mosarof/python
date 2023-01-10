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
headers = {'authorization': API_KEY}

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
                            headers=headers,
                            data=read_file(filename))

    audio_url=upload_response.json()['upload_url']
    return audio_url

#transcribe
def transcribe(audio_url,sentiment_analysis):
    transcript_request = { 
        "audio_url": audio_url,
        'sentiment_analysis':sentiment_analysis
        }
    transcript_response = requests.post(transcribe_endpoint,json=transcript_request, headers=headers)
    job_id=transcript_response.json()['id']
    return job_id

#polling
def polling(transcript_id):
    polling_endpoint=transcribe_endpoint + '/' + transcript_id
    polling_response=requests.get(polling_endpoint,headers=headers)
    return polling_response.json()

def get_transcription_result(audio_url,sentiment_analysis):
    transcript_id=transcribe(audio_url,sentiment_analysis)
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

def save_transcript(audio_url,text_file_name,sentiment_analysis=False):
    data,error=get_transcription_result(audio_url,sentiment_analysis)
    if data:
        with open(text_file_name+".txt","w") as f:
            f.write(data['text'])
        print("Transcription is successful")

        if sentiment_analysis:
            filename=text_file_name+"_sentiment.json"
            with open(filename,"w") as f:
                sentiments=data["sentiment_analysis_results"]
                json.dump(sentiments,f,indent=4)
    elif error:
        print("Error in transcription",error)

