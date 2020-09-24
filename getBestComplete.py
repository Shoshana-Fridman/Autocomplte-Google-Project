from typing import List

from autoCompleteData import AutoCompleteData
from checkingChangesInSubstring import substring_without_change, change_characters_minus_one_score, \
    delete_or_add_character_minus_two_score, change_character, delete_or_add_character
from variables import NUM_COMPLETE


def get_best_k_completions(prefix, file_list, auto_completion):
    class_result = []
    class_result += substring_without_change(prefix, file_list, auto_completion)

    if enough_complete(class_result):
        return class_result

    class_result += change_characters_minus_one_score(prefix, NUM_COMPLETE - len(class_result), file_list, auto_completion)

    if enough_complete(class_result):
        return class_result

    class_result += (delete_or_add_character_minus_two_score(prefix, NUM_COMPLETE - len(class_result), file_list, auto_completion))
    same_minus_score(prefix, class_result, file_list, auto_completion, 3)

    if enough_complete(class_result):
        return class_result

    class_result += (change_character(prefix, NUM_COMPLETE - len(class_result), 2, file_list, auto_completion))

    if enough_complete(class_result):
        return class_result

    class_result += (delete_or_add_character(prefix, NUM_COMPLETE - len(class_result), 3, file_list, auto_completion))
    same_minus_score(prefix, class_result, file_list, auto_completion, 1)

    if enough_complete(class_result):
        return class_result

    class_result += change_character(prefix, NUM_COMPLETE - len(class_result), 0, file_list, auto_completion)

    if enough_complete(class_result):
        return class_result

    for i in range(2, -1, -1):
        class_result += (
            delete_or_add_character(prefix, NUM_COMPLETE - len(class_result), i, file_list, auto_completion))

        if enough_complete(class_result):
            return class_result

    return class_result


def enough_complete(class_result):
    return len(class_result) == NUM_COMPLETE


def same_minus_score(prefix, class_result, file_list, auto_completion, index):

    for i in change_character(prefix, NUM_COMPLETE - len(class_result), index, file_list, auto_completion):
        class_result.append(i)
        if len(class_result) > NUM_COMPLETE:
            remove_lowest_class(class_result)


def remove_lowest_class(list_: List[AutoCompleteData]):
    tmp_list = []
    tmp_dict = {}

    for val in list_:
        tmp_list.append(val.completed_sentence)
        tmp_dict[val.completed_sentence] = val
    tmp_list.sort()
    list_.remove(tmp_dict[tmp_list[-1]])
