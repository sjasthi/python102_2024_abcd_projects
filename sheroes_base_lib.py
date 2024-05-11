#============================================================
#  This base libary contains all the helper functions needed for Python102 projects
#  We will import these into other python scripts as needed

# import sheroes_base_lib as sheroes
#=============================================================

import requests

# Declare the global variables
API_BASE_URL = "https://www.projectabcd.com/api/getinfo.php?id="

sheroes_id_list = [26, 27, 28, 29, 30, 31, 32, 33, 39, 50, 52, 53, 101,
                   102, 110, 111, 112, 114, 115, 116, 117, 119, 151, 171,
                   183, 188, 196, 201, 206, 235, 265, 275, 276, 306, 313,
                   314, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325,
                   326, 327, 328, 329, 330, 356, 401, 405, 406, 407, 409,
                   410, 411, 412, 413, 414, 415, 418, 419, 420, 422, 423,
                   424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434,
                   435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445,
                   462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472,
                   473, 474, 475, 476, 477, 478, 483, 484, 491, 492, 493,
                   502, 506, 518, 520, 523, 524, 525, 534, 538, 542, 544,
                   547, 548, 549, 560, 568, 574, 575, 577, 578, 581, 582,
                   583, 586, 588, 601, 605, 611, 618, 620, 626, 631, 632,
                   654, 655, 658, 659, 660, 662, 663, 664, 665, 666, 667,
                   668, 669, 670, 671, 672, 673, 674, 676, 677, 678, 679,
                   680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690,
                   691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701,
                   702, 703, 704, 706, 709, 710, 711, 712, 713, 714, 715,
                   716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726,
                   728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738,
                   739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749,
                   750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760,
                   761, 762, 763, 764, 765, 766, 767, 768, 769, 770, 771, 772]


sheroes_id_list = [761, 762, 763, 764, 765, 766, 767, 768]

'''
Fetch the json data from API
The data_list is a list of dictionaries where each dictionary encapsulates the details of an ID.
'''
def fetch_data_from_api(ids = sheroes_id_list):
    data_list = []
    for id in ids:
        url = API_BASE_URL + str(id)
        headers = {
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data_list.append(response.json()['data'])
        else:
            print(f"Failed to get data from the API for ID {id}. Status code:", response.status_code)

    return data_list


#==== other helper functions to be done =========
# get the name for a given id
# get the description for a given id
# get the did you know for a given id
# get the complete dictionary for a given id

'''
Main method for fetching the data through APIs
'''
if __name__ == "__main__":

    # to minimize the load on the server as well as to run this snippet quicker,
    # we will do only for the first 10 sheroes
    ids = sheroes_id_list[:10]
    fetched_data_list = fetch_data_from_api(ids)
    if fetched_data_list:
        print(f"Fetched the data for {len(fetched_data_list)} sheroes.")
        for data in fetched_data_list:
            print(data)
    else:
        print("Failed to fetch data from the API.")
