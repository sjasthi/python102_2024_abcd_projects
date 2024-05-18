# import the base library
import sheroes_base_lib as sheroes

if __name__ == "__main__":
    #symbol_list = dir(sheroes)

    # print sheroes id list
    print(sheroes.sheroes_id_list)
    print("Count of IDs: ", len(sheroes.sheroes_id_list))
    print("BaseURL is: ", sheroes.API_BASE_URL)
    print("ID List is: ",  sheroes.sheroes_id_list)


    # data_list = list of dictionaries
    # if you don't pass in the id list, this function fetches the data of all 256 IDs
   # data_list = sheroes.fetch_data_from_api()


    # if you want to test with limited IDs, pass in the ID list
    custom_id_list = [26, 27, 28, 29, 30, 31]
    data_list = sheroes.fetch_data_from_api(custom_id_list)

    # loop through the data list and fetch the data you want for further processing.
    for data in data_list:
        #print(type(data), data)
        print(data['id'], data['name'])

