from collections import defaultdict

from getBestComplete import get_best_k_completions
from initFromFile import init_data, without_punctuation
from variables import STOP_INPUT, MAX_OF_CHAR


def read_input():
    return without_punctuation(input())


def print_best_completions(list_completions):
    if 0 == len(list_completions):
        print("Sorry, no matches were found")
        return False
    print(f'Here are {len(list_completions)} suggestions')

    for index, completion in enumerate(list_completions, 1):
        print(f'{index}. {completion}')

    return True


def max_of_char(current_input):
    print(f"The system return answer for {MAX_OF_CHAR} first character")
    return current_input[:MAX_OF_CHAR]


def run():
    auto_completion = defaultdict(set)
    file_list = {}
    print("Loading the file and preparing the system...")
    init_data(file_list, auto_completion)

    while True:
        print("The system is ready, please enter your text")
        current_input = read_input()
        if len(current_input) > 0:
            if len(current_input) > MAX_OF_CHAR:
                current_input = max_of_char(current_input)

            while current_input[-1] != STOP_INPUT:
                if False == (print_best_completions(get_best_k_completions(current_input, file_list, auto_completion))):
                    break
                print(current_input, end='')
                current_input += read_input()
