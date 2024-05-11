import requests
from localspelling import convert_spelling
from localspelling.gb_us import DICTIONARY
from localspelling.util import get_lookup_dictionaries

# Define the API endpoint URL
api_url = 'https://abcd2.projectabcd.com/api/getinfo.php?id='

# Selected IDs from the abcd_id_list
selected_ids = [711, 733, 523 ,542, 731, 763, 669, 739, 690, 742, 724, 112, 668, 714, 671, 32, 722, 434, 713, 751,
                760, 102, 654, 695, 762, 470, 33, 432, 429, 265, 673, 111, 588, 734, 692, 477, 518, 720, 445, 437,
                752, 206, 670, 544, 491, 737, 685, 492, 53, 676, 575, 469, 183, 717, 665, 715, 410, 425, 430, 586,
                769, 235, 462, 741, 524, 718, 758, 465, 745, 520, 431, 721, 171, 484, 759, 672, 433, 749, 502, 756,
                747, 757, 26, 765, 667]

lookups = get_lookup_dictionaries(DICTIONARY)

found_difference = False

for id_number in selected_ids:
    response = requests.get(f'{api_url}{id_number}', headers={"User-Agent": "XY"})
    json_response = response.json()
    name = json_response['data']['name']
    description = json_response['data']['description']

    # Tokenize the description into words
    words = description.split()

    # Convert the spellings to British English
    converted_words = [convert_spelling(word, "gb") for word in words]

    # Filter words with different British/American spellings
    different_spellings = [(original, converted) for original, converted in zip(words, converted_words) if original.lower() != converted.lower() and converted.lower() not in DICTIONARY]

    if different_spellings:
        found_difference = True
        print(f"ID: {id_number}")
        print(f"Name: {name}")
        print("Words with different British/American spellings:")
        for original, converted in different_spellings:
            print(f"{original} -> {converted}")
        print("\n")
    else:
        print(f"ID: {id_number}")
        print(f"Name: {name}")
        print("Nothing to convert.\n")

if not found_difference:
    print("Nothing to convert.")
