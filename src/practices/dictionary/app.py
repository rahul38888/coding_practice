from src.practices.dictionary.dictionaryfile_parser import build_dictionary

# dictionary data source: https://www.mso.anu.edu.au/~ralph/OPTED

if __name__ == '__main__':
    dictionary = build_dictionary()

    try:
        while True:
            c = input()
            word = dictionary.search(c)
            print(str(word))
    except KeyboardInterrupt:
        print("Exiting gracefully!")