import string
import numpy as np


def count_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        num_of_words = len(file_content.split())
        long_string = "".join([s.lower() for s in file_content.split()])
        short_string = string.ascii_lowercase
        character_dict = {}
        for char in long_string:
            if char in short_string:
                if char in character_dict:
                    character_dict[char] += 1
                else:
                    character_dict[char] = 1

        keys = list(character_dict.keys())
        values = list(character_dict.values())
        sorted_value_index = np.argsort(values)
        sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    return sorted_dict, num_of_words


def write_report(sorted_dict, filepath, num_of_words):
    with open(filepath, 'w') as f:
        f.write(
            '=========== REPORT ==================\n'
            f"There is a total of {num_of_words} words in the text.\n"
            '------------------------------------\n'
        )
        for ch in sorted_dict:
            f.write(
                f"The character '{ch}' appears {sorted_dict[ch]} times\n"
            )
        f.write('\n========== END OF REPORT ==============')


new_sort, total_words = count_text('books/frankenstein.txt')
write_report(new_sort, 'books/report.txt', total_words)
