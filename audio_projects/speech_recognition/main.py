from fileinput import filename
from turtle import onclick
from api_communication_2 import *
import streamlit as st
import json

st.title("Welcome to my web page")
episode_id=st.sidebar.text_input("Please enter a valid Episode id")
button=st.sidebar.button("Get podcast summary",on_click=save_transcript,args=episode_id)

if button:
    filename=episode_id + '_chapter.txt'
    with open(filename,'r') as f:
        data=json.load(f)

        chapters=data['chapters']
        episode_thumbnail=data['episode_thumbnail']
        episode_title=data['episode_title']
        podcast_title=data['podcast_title']

    st.header(f'{podcast_title}-{episode_title}')
    st.image(episode_thumbnail)
    for chap in chapters:
        with st.expander(chap['gist']):
            chap['summary']

# filename = "audio.mp3"
# audio_url=upload(filename)
# save_transcript(audio_url,"text_file")