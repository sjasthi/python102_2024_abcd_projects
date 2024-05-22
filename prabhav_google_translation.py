import googletrans
import requests
import json
from googletrans import Translator

languages = dict(googletrans.LANGUAGES)
for x in languages:
    print(f"{x} | {languages[x]}")
translator = Translator()
to_lang = input(
    'Which language would you like the text to be translated to? /nPlease choose from the languages printed above: ')

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
c = 0

with open("translation.txt", "w", encoding="utf-8") as file:
    # Loop through each ID in the list
    for id_number in abcd_ids:
        c += 1
        if to_lang not in languages:
            print('Sorry. The specified language is not supported.')
            break
        response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={id_number}',
                                headers={"User-Agent": "XY"})
        json_response = dict(json.loads(response.text))
        name = translator.translate(text=json_response['data']['name'], dest=to_lang)
        desc = translator.translate(text=json_response['data']['description'], dest=to_lang)
        fact = translator.translate(text=json_response['data']['did_you_know'], dest=to_lang)
        file.write(
            f"Count: {c} ID: {id_number}\nName: {name.text}\nDescription: {desc.text}\nDid You Know: {fact.text}\n")
