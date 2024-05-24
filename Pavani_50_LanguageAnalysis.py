#Project 50: Language Analysis - Ease of Reading, Lexile Score, Grade Level
import textstat
import pkg_resources
import requests
import json
import pandas as pd

import sheroes_base_lib

#get the sheroes id list from the sheroes_base_lib
sheroes_id_list = sheroes_base_lib.sheroes_id_list


api_url = 'https://abcd2.projectabcd.com/api/getinfo.php?id='

#Create the dictionary with keys and empty values
language_analysis = {'Sheroes_ID':[],'Flesch reading ease':[],'FOG Index of given text':[],'Text Standard - Grade Level':[],'Readability Score':[],'Ease of Reading':[]}

# Getting the API and using json
with open("Language_Analysis.txt", "w") as file1:
    # Writing data to a file
    file1.write("Project 50: Language Analysis - Ease of Reading, Lexile Score, Grade Level \n\n")
    for id_number in sheroes_id_list:
        text_data = ''
        response = requests.get(f'{api_url}{id_number}', headers={"User-Agent": "XY"}, verify=False)
        json_response = json.loads(response.text)
        language_analysis['Sheroes_ID'].extend([id_number])

        description = json_response['data']['description']
        did_you_know = json_response['data']['did_you_know']
        complete_text = description + ' ' + did_you_know
        id_number = json_response['data']['id']
        name = json_response['data']['name']
        text_data = text_data+complete_text

        #Write to the file
        file1.write("Sheroes ID:"+ str(id_number) + "\n")

        file1.write("Name:" + name + "\n")
        file1.write("Flesch reading ease:" + str(textstat.flesch_reading_ease(text_data)) + "\n")
        file1.write("FOG Index of given text:" + str(textstat.gunning_fog(text_data)) + "\n")
        file1.write("Text Standard - Grade Level:" + textstat.text_standard(text_data) + "\n")
        file1.write("Readability Score:" + str(textstat.automated_readability_index(text_data)) + "\n")
        file1.write("Ease of Reading:" + str(textstat.flesch_reading_ease(text_data)) + "\n\n")

        #Collecting the value list for the dictionary
        language_analysis['Flesch reading ease'].extend([textstat.flesch_reading_ease(text_data)])
        language_analysis['FOG Index of given text'].extend([textstat.gunning_fog(text_data)])
        language_analysis['Text Standard - Grade Level'].extend([textstat.text_standard(text_data)])
        language_analysis['Readability Score'].extend([textstat.automated_readability_index(text_data)])
        language_analysis['Ease of Reading'].extend([textstat.flesch_reading_ease(text_data)])


        # You can create a data frame from a dictionary
        my_df = pd.DataFrame(language_analysis)

        #write data frame to the Excel
        with pd.ExcelWriter('Language_Analysis.xlsx') as excel_writer:
            my_df.to_excel(excel_writer, sheet_name='Sheet1', index=False)

        #print(language_analysis)




