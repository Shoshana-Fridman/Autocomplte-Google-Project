import linecache

from autoCompleteData import AutoCompleteData
from initFromFile import remove_lexographic_order, without_punctuation
from variables import CHARACTER_LIST


def substring_without_change(_input, file_list, auto_completion):
    if auto_completion.get(without_punctuation(_input)) is not None:
        return list_to_auto_class(auto_completion.get(without_punctuation(_input)), len(_input) * 2, file_list)
    return []


def change_characters_minus_one_score(_input, remain, file_list, auto_completion):
    result = set()

    for i in range(4, len(_input)):
        change(_input, i, result, remain, file_list, auto_completion)

    return list_to_auto_class(result, len(_input) * 2 - 1, file_list)


def change_character(_input, remain, index, file_list, auto_completion):
    result = set()
    change(_input, index, result, remain, file_list, auto_completion)

    return list_to_auto_class(result, len(_input) * 2 - (5 - index), file_list)


def delete_or_add_character_minus_two_score(_input, remain, file_list, auto_completion):
    result = set()

    for i in range(4, len(_input)):
        delete(_input, i, result, remain, file_list, auto_completion)
        add(i, _input, result, remain, file_list, auto_completion)

    return list_to_auto_class(result, len(_input) * 2 - 2, file_list)


def delete_or_add_character(_input, remain, index, file_list, auto_completion):
    result = set()
    delete(_input, index, result, remain, file_list, auto_completion)
    add(index, _input, result, remain, file_list, auto_completion)

    return list_to_auto_class(result, len(_input) * 2 - (10 - (index * 2)), file_list)


def add(i, _input, result, remain, file_list, auto_completion):

    for char in CHARACTER_LIST:
        if auto_completion.get(f'{_input[:i]}{char}{_input[i:]}') is not None:

            for j in auto_completion.get(f'{_input[:i]}{char}{_input[i:]}'):
                result.add(j)
                if len(result) > remain:

                    remove_lexographic_order(result, file_list)


def delete(_input, i, result, remain, file_list, auto_completion):
    if auto_completion.get(f'{_input[:i]}{_input[i + 1:]}') is not None:

        for j in auto_completion.get(f'{_input[:i]}{_input[i + 1:]}'):
            result.add(j)
            if len(result) > remain:
                remove_lexographic_order(result, file_list)


def change(_input, i, result, remain, file_list, auto_completion):

    for character in CHARACTER_LIST:
        if auto_completion.get(f'{_input[:i]}{character}{_input[i + 1:]}') is not None:

            for j in auto_completion.get(f'{_input[:i]}{character}{_input[i + 1:]}'):
                result.add(j)
                if len(result) > remain:
                    remove_lexographic_order(result, file_list)


def list_to_auto_class(_list, score, file_list):
    result = []

    for item in _list:
        result.append(
            AutoCompleteData(linecache.getline(file_list[item[0]], item[1])[:-1], file_list[item[0]], item[1], score))
    return result



