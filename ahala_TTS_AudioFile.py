import gtts
import os
import requests
import json

if __name__ == '__main__':

        # Giving the list of all the Sheroes IDs from the Project ABCD website

        abcd_id_list = [26, 27, 28, 29, 30, 31, 32, 33, 39, 50, 52, 53, 101, 102, 110, 111, 112, 114, 115, 116, 117, 119, 151,
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
                        750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772]

        id_list_len = len(abcd_id_list)
        all_list = ''

        # Using a for loop to go throught the abcd_id_list and create API ids
        for id_number in abcd_id_list:
                response = requests.get(f'https://abcd2.projectabcd.com/api/getinfo.php?id={id_number}',
                                        headers={"User-Agent": "XY"})

        # Using json to get only the description and did you know
                json_response = json.loads(response.text)
                desc = json_response['data']['description']
                dyk = json_response['data']['did_you_know']
                total_text = '\n' + desc + ' ' + dyk

                all_list = all_list + total_text
        # print('\n', all_list)

        # Naming the audio file that is to be created
        AUDIO_FILE = '_sheroes.mp3'
        my_text = all_list

        # Python supports many accents and languages - which we can choose from
        # Here we have picked English with a US accent
        language = 'en-US'

        # Passing the text and language to the engine
        # We have marked slow=True which tells the module that the audio should have a low speed
        my_audio = gtts.gTTS(text=my_text, lang=language, slow=True)

        # Saving the converted audio file
        my_audio.save(AUDIO_FILE)

        # Playing the converted audio file
        os.startfile(AUDIO_FILE)
