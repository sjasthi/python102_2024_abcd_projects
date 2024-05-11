# Import the necessary libraries
import requests
import json

beta = open("stop_words.txt", "r")
alpha = beta.read()
stop_words = alpha.split(", ")

abcd_ids = [711, 733, 523, 542, 731, 763, 669, 739, 690, 742, 724, 112, 668, 714, 671, 32, 722, 434, 713, 751, 760, 102, 654, 695, 762, 470, 33, 432, 429, 265, 673, 111, 588, 734, 692, 477, 518, 720, 445, 437, 752, 206, 670, 544, 491, 737, 685, 492, 53, 676, 575, 469, 183, 717, 665, 715, 410, 425, 430, 586, 769, 235, 462, 741, 524, 718, 758, 465, 745, 520, 431, 721, 171, 484, 759, 672, 433, 749, 502, 756, 747, 757, 26, 765, 667]

def create_frequency_table(id, identify_stop_words):
    response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={id}', headers={"User-Agent": "XY"})
    json_response = json.loads(response.text)
    name = json_response['data']['name']
    description = json_response['data']['description']
    description_list = description.split()
    description_dictionary: dict[str, int] = {}
    if identify_stop_words == True:
        for word in description_list:
            if word in stop_words:
                continue
            if word not in description_dictionary:
                description_dictionary.update({word:1})
            elif word in description_dictionary:
                v = description_dictionary[word]
                v = v + 1
                description_dictionary[word] = v
        print(f"Frequency Table for Description of {name}")
        del name
        print("\n# | Word\n--|----------------")
        for key in description_dictionary:
            print(f'{description_dictionary[key]} | {key}')
    if identify_stop_words == False:
        for word in description_list:
            if word not in description_dictionary:
                description_dictionary.update({word:1})
            elif word in description_dictionary:
                v = description_dictionary[word]
                v = v + 1
                description_dictionary[word] = v
        print(f"Frequency Table for Description of {name}")
        del name
        print("\n# | Word\n--|----------------")
        for key in description_dictionary:
            print(f'{description_dictionary[key]} | {key}')

create_frequency_table(714, True)
