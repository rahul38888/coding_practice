import time
from zipfile import ZipFile
from re import split

from src.practices.dictionary.dictionary import Dictionary, Word, Definition


def parse_word(line: str) -> Word:
    if line is None or len(line) == 0:
        return None

    if line[0] == "\"":
        line = line[1:]
    if line[-1] == "\"":
        line = line[:-1]

    val = list(map(lambda s: s.strip(), split(r" \(|\) ", line, 2)))
    if len(val) < 3:
        return None

    word =  Word(val[0])
    defination = Definition(None if len(val[1]) == 0 else val[1], val[2])
    word.add_definition([defination])
    return word

def build_dictionary(filename: str = "Dictionary-in-csv.zip") -> Dictionary:
    dictionary = Dictionary()

    st = time.time()
    print("Starting loading!")
    count = 0
    with ZipFile(filename) as zip:
        for i in range(26):
            char = chr(ord('A') + i)
            file = zip.open(name="Dictionary in csv/" + char + ".csv")
            lines = file.readlines()
            for line in lines:
                word = parse_word(line.decode("ISO-8859-2").strip())
                if word:
                    dictionary.insert(word)
                    count += 1
        zip.close()

    print("Total number of words in dictionary: %i"%count)
    print("Done loading! Seconds taken: %i"%(time.time()-st))
    return dictionary


if __name__ == '__main__':
    build_dictionary()
