# Importing the necessary libraries
import requests
import json

abcd_id_list = [711, 733, 523, 542, 731, 763, 669, 739, 690, 742, 724, 112, 668, 714, 671, 32, 722, 434, 713, 751,
                760, 102, 654, 695, 762, 470, 33, 432, 429, 265, 673, 111, 588, 734, 692, 477, 518, 720, 445, 437,
                752, 206, 670, 544, 491, 737, 685, 492, 53, 676, 575, 469, 183, 717, 665, 715, 410, 425, 430, 586,
                769, 235, 462, 741, 524, 718, 758, 465, 745, 520, 431, 721, 171, 484, 759, 672, 433, 749, 502, 756,
                747, 757, 26, 765, 667]
all_list = ''
stopwords = ['the', 'a', 'an', 'in', 'he', 'she', 'her', 'to', 'it', 'so', 'and', 'has', 'of',
            'is', 'was', 'for', 'at', 'from', 'where', 'Her', 'She', 'as', 'when', 'on', 'with',
             'by', 'also', 'In', 'that', 'have', 'been', 'how', 'their', 'one' ]

# Getting the API and using json
for id_number in abcd_id_list:
  response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={id_number}', headers={"User-Agent": "XY"})
  json_response = json.loads(response.text)

  # print(type(json_response))
  # print(json_response)
  desc = json_response['data']['description']
  dyk = json_response['data']['did_you_know']
  total_text = desc + ' ' + dyk
  # print('\n', total_text)
  # print(type(total_text))

  all_list = all_list+total_text
  #print('\n', all_list)

# Incrementing the values in count_dict based on their occurences
count_dict = dict()
tot_text = all_list.split()
# print(tot_text)

for word in tot_text:
  if word not in stopwords:

    if word in count_dict:
      count_dict[word] += 1

    else:
      count_dict[word] = 1

sorted_dict = dict(sorted(count_dict.items(), key=lambda item: -item[1]))
# print(sorted_dict)

# Getting the number of words to be printed from the user

num_of_words = int(input('Please give the number of words you would like to see: '))
output_dict = dict(list(sorted_dict.items())[0:num_of_words])
print(str(output_dict))
