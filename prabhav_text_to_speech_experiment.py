import gtts
import pyttsx3
import os
import requests
import json

id_list = [669, 739, 690, 742, 724, 112, 668, 714, 671, 32]

for abcd in id_list:
    response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={abcd}', headers={"User-Agent": "XY"})
    json_response = json.loads(response.text)
    description = json_response['data']['description']
    # pyttsx3 (doesn't work as well as I thought)
    engine = pyttsx3.init()
    engine.setProperty('rate', 20)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
    engine.say(description)
    audio_file = engine.save_to_file(description, f'pyttsx3_Audio_File_ID_{abcd}.mp3')
    # gtts
    language = 'en-US'
    second_audio_file = gtts.gTTS(text=description, lang=language, slow=True)
    second_audio_file.save(f'gtts_Audio_File_ID_{abcd}')
    # until we can figure out better methods, we can't actually play these files
    os.startfile(f'pyttsx3_Audio_File_ID_{abcd}.mp3')
    os.startfile(f'gtts_Audio_File_ID_{abcd}.mp3')