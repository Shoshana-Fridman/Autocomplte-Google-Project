from variables import MAX_OF_CHAR

import linecache
import os
import string


def get_files(file_index_path_dict):
    path = 'try'
    file_index = 0

    for root, dirs, files in os.walk(path):

        for file in files:
            file_index_path_dict[file_index] = (os.path.abspath(os.path.join(root, file)))
            file_index += 1
    return file_index_path_dict


def read_data_from_file(file):
    with open(file, encoding="utf8") as my_file:
        return my_file.read().split("\n")


def init_data(file_list, autocompletion):
    path_files = get_files(file_list)

    for file_index in path_files.keys():
        data = read_data_from_file(path_files[file_index])
        num_line = 1

        for sentence in data:
            sentence = without_punctuation(sentence)
            init_substring(sentence, file_index, num_line, file_list, autocompletion)
            num_line += 1


def init_substring(sentence, file_index, num_line, file_list, autocompletion):
    """We assume that the user does not enter input greater than MAX_OF_CHAR = 20"""
    stop = min(MAX_OF_CHAR, len(sentence))
    num_complete = 5

    for start in range(stop):

        for last in range(start + 1, stop):
            if sentence[start] != ' ' and sentence[last] != ' ':
                autocompletion[without_punctuation(sentence[start:last + 1])].add(tuple([file_index, num_line]))
                if len(autocompletion[sentence[start:last + 1]]) > num_complete:
                    remove_lexographic_order(autocompletion[without_punctuation(sentence[start:last + 1])], file_list)


def without_punctuation(string_):
    string_ = string_.strip()
    string_ = " ".join(string_.split())
    exclude = set(string.punctuation)
    exclude.remove('#')
    return ''.join(ch for ch in string_ if ch not in exclude).lower()


def remove_lexographic_order(list_, file_list):
    tmp_list = []
    tmp_dict = {}
    for val in list_:
        tmp_list.append(linecache.getline(file_list[val[0]], val[1]))
        tmp_dict[linecache.getline(file_list[val[0]], val[1])] = val
    tmp_list.sort()
    list_.remove(tmp_dict[tmp_list[-1]])
