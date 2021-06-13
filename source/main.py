import os
import json
import re
import string
import worksheet
import flashcard
import process_svg
import cairosvg
import concurrent.futures
from pathlib import Path

"""
main.py takes an input file of Chinese characters and produces both one-sided flashcards and handwriting practice worksheets.
"""

CHARACTER_DICTIONARY = {}
used_hanzi = []


# class for character, definition, and pinyin
class Hanzi:
    def __init__(self, entry):
        self.character = entry['character']
        self.definition = entry['definition'] if 'definition' in entry else None
        self.pinyin = entry['pinyin']
        self.code_point = ord(self.character)

    def svg_file_name_original(self):
        return '../makemeahanzi/svgs/' + str(self.code_point) + '.svg'

    def svg_file_name_original_still(self):
        return '../makemeahanzi/svgs-still/' + str(self.code_point) + '-still.svg'

    def svg_file_name(self):
        return str(self.code_point) + '.svg'

    def pdf_file_name(self):
        return str(self.code_point) + '.pdf'

    def svg_file_name_worksheet(self):
        return 'worksheet/' + str(self.code_point) + '.svg'

    def pdf_file_name_worksheet(self):
        return 'worksheet/' + str(self.code_point) + '.pdf'

    def svg_file_name_flashcard(self):
        return 'flashcard/' + str(self.code_point) + '.svg'

    def pdf_file_name_flashcard(self):
        return 'flashcard/' + str(self.code_point) + '.pdf'


# reads dictionary.txt to CHARACTER_DICTIONARY
def read_files():
    with open("../makemeahanzi/dictionary.txt", 'r') as dictionary:
        for line in dictionary:
            entry = json.loads(line)
            character = Hanzi(entry)
            CHARACTER_DICTIONARY[character.character] = character

    with open('input.txt', 'r') as input:
        text = input.read()

        # remove whitespace
        text = re.sub(r'(\s|\u180B|\u200B|\u200C|\u200D|\u2060|\uFEFF|)+', '', text)

        # remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))

        for symbol in text:
            if symbol in CHARACTER_DICTIONARY.keys():
                used_hanzi.append(CHARACTER_DICTIONARY.get(symbol))
            else:
                print('{} is not in the provided dictionary'.format(symbol))

    Path('worksheet').mkdir(parents=True, exist_ok=True)
    Path('flashcard').mkdir(parents=True, exist_ok=True)
    process_used_hanzi()
    worksheet.write_tex(used_hanzi)
    flashcard.write_tex(used_hanzi)


def process_used_hanzi():
    existing_hanzi = set()
    for hanzi in used_hanzi:
        if not os.path.exists(hanzi.svg_file_name_original()):
            print("SVG does not exist: {}".format(hanzi.svg_file_name_original()))
            continue
        existing_hanzi.add(hanzi)
        process_svg.process_worksheet(hanzi)
        process_svg.process_flashcard(hanzi)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for hanzi in existing_hanzi:
            executor.submit(cairosvg.svg2pdf, url=hanzi.svg_file_name_worksheet(), write_to=hanzi.pdf_file_name_worksheet())
            executor.submit(cairosvg.svg2pdf, url=hanzi.svg_file_name_flashcard(), write_to=hanzi.pdf_file_name_flashcard())


if __name__ == "__main__":
    read_files()
