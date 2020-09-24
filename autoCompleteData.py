import ntpath


class AutoCompleteData:
    def __init__(self, sentence, current_file, line_in_file, score):
        self.completed_sentence = sentence
        self.source_text = current_file
        self.offset = line_in_file
        self.score = score

    def __str__(self):
        self.source_text = f'{ntpath.basename(self.source_text)[:-4]}'

        return f'{self.completed_sentence} ({self.source_text} {str(self.offset)})'

    def get_sentence(self):
        return self.completed_sentence

