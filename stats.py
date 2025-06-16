def get_num_words(file_contents):
    words = file_contents.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def sort_on(dict):
    return dict

def get_letters(file_contents):
    my_dict = {}
    for letter in file_contents:
        if letter.lower() in my_dict:
            my_dict[letter.lower()] += 1
        else:
            my_dict[letter.lower()] = 1
    return dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
