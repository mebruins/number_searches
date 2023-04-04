def linear_search_dictionary(dictionary, target):
    for key,value in dictionary.items():
        if value == target:
            print('Found at key', key)
            return key
    print('Target is not in the dictionary')
    return None



my_dictionary = {'red': 5, 'blue': 3, 'yellow': 12, 'green': 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)

# asnwer from prof

def linear_search_dictionary2(dictionary, target):
    for k in dictionary.keys():
        if dictionary[k] == target:
            print('Found at key', k)
            return k
    print('Target is not in the dictionary')
    return None

linear_search_dictionary2(my_dictionary, 3)
