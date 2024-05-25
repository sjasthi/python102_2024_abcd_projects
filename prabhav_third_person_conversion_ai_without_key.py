# !pip install openai
import openai
from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

# defining the API key in two places
# openai.api_key = "-------------------------------------------------------"
# client = OpenAI(api_key="-----------------------------------------------")

# every abcd id that has the tag "shero"
abcd_ids = [26, 27, 28, 29, 30, 31, 32, 33, 39, 50, 52, 53, 101, 102, 110, 111, 112, 114, 115, 116, 117, 119, 151,
            171, 183, 188, 196, 201, 206, 235, 265, 275, 276, 306, 313, 314, 316, 317, 318, 319, 320, 321, 322, 323,
            324, 325, 326, 327, 328, 329, 330, 356, 401, 405, 406, 407, 409, 410, 411, 412, 413, 414, 415, 418, 419,
            420, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441,
            442, 443, 444, 445, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478,
            483, 484, 491, 492, 493, 502, 506, 518, 520, 523, 524, 525, 534, 538, 542, 544, 547, 548, 549, 560, 568,
            574, 575, 577, 578, 581, 582, 583, 586, 588, 601, 605, 611, 618, 620, 626, 631, 632, 654, 655, 658, 659,
            660, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 676, 677, 678, 679, 680, 681, 682,
            683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703,
            704, 706, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 728,
            729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749,
            750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770,
            771, 772]
# test ids for the presentation
test_abcd_ids = [26, 27, 28, 29, 30, 31, 32, 33, 39, 50]

def conversion(sheroes: list):
    # create a new file to store all of these conversions
    with open("sheroes_conversion.txt", "w") as a:
        a.write("Full Conversions")
        # start iterating through each id
        for x in sheroes:
            # load the entire info for one specific shero
            response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={x}', headers={"User-Agent": "XY"})
            json_response = dict(json.loads(response.text))
            # check that the id has information stored, if not, go to the next id
            if json_response['response_code'] == 400:
                continue
            # write their name and ID at the top
            a.write(f"ID: {x} | Name: {json_response['data']['name']}\n")
            # load the description
            description = json_response['data']['description']
            # loop through to remove any newline characters or carraige returns
            while True:
                if "\r\n" in description:
                    description = description.replace("\r\n", " ")
                if "\n" in description:
                    description = description.replace("\n", "")
                else:
                    break
            # add this proofed description to the file
            a.write(f"Third Person: {description}")
            # ask GPT-3.5 to turn this document into a first person description, then writes it to the file
            # completion = client.chat.completions.create(
            #     model="gpt-3.5-turbo",
            #     messages=[
            #         # defines the system's role
            #         {"role": "system", "content": "You are translating third person descriptions of famous Indian women into first person scripts with the same reading complexity level."},
            #         # gives the system the relevant content
            #         {"role": "user", "content": description}
            #     ]
            # )
            # a.write(f"\nFirst Person: {completion.choices[0].message.content}\n")

# the real version would be able to do this, but it would take way too long
# conversion(abcd_ids)

# you could also go by each id, but the function would break unless the individual id is surrounded by brackets
# conversion([430])

# we do this one instead in the interest of time
conversion(test_abcd_ids)
