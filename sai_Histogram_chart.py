import requests
import json
#import matplotlib
#from collections import Counter
#import re
#import numpy


abcdlist = [711, 733, 523, 542, 731, 763, 669, 739, 690, 742, 724, 112, 668, 714, 671, 32, 722, 434, 713, 751,
                760, 102, 654, 695, 762, 470, 33, 432, 429, 265, 673, 111, 588, 734, 692, 477, 518, 720, 445, 437,
                752, 206, 670, 544, 491, 737, 685, 492, 53, 676, 575, 469, 183, 717, 665, 715, 410, 425, 430, 586,
                769, 235, 462, 741, 524, 718, 758, 465, 745, 520, 431, 721, 171, 484, 759, 672, 433, 749, 502, 756,
                747, 757, 26, 765, 667]

# dictionary 
year_counts = {year: 0 for year in range(1900, 2000)}

for id_number in abcdlist:
    response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={id_number}', headers={"User-Agent": "XY"})
    json_response = json.loads(response.text)

    name = json_response['data']['name']
    desc = json_response['data']['description']

    for year in range(1900, 2000):
        if 'born' in desc and str(year) in desc:
            #print(name, year)
            year_counts[year] += 1

# the histogram
print("\nHistogram of Birth Years for Sheroes:")
for year in range(1900, 2000):
    print(f"{year} {'+' * year_counts[year]}")


