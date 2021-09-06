
char_count = 26

class Word:
    def __init__(self, word: str, definition: str = None):
        self.word = word
        self.definition = definition

    def __str__(self):
        return self.__dict__.__str__()


class Node:
    def __init__(self):
        self.child_nodes = [None for i in range(char_count)]
        self.word = None

    def insert(self, word: Word, cur_index: int = 0):
        if word.word is None or len(word.word) == 0:
            # Such words are not stored
            return

        if cur_index == len(word.word) - 1:
            self.word = word
        else:
            i = ord(word.word[cur_index]) - ord('a')
            if self.child_nodes[i] is None:
                self.child_nodes[i] = Node()
            self.child_nodes[i].insert(word, cur_index+1)

    def search(self, word: str, cur_index: int = 0) -> Word:
        if word.word is None or len(word.word) == 0:
            # Such words are not stored
            return None

        if cur_index == len(word.word) - 1:
            return self.word
        else:
            i = ord(word.word[cur_index]) - ord('a')
            if self.child_nodes[i] is None:
                # Word do not exists
                return None
            return self.child_nodes[i].search(word, cur_index+1)


class Dictionary(Node):
    def __init__(self):
        super(Dictionary, self).__init__()


if __name__ == '__main__':
    words = ["hot", "a", "cold", "soft", "hard", "top", "bottom"]

    dictionary = Dictionary()
    for w in words:
        word = Word(w)
        dictionary.insert(word=word)

    try:
        while True:
            c = input()
            com = c.split(sep=" ")
            if com[0] == "I":
                dictionary.insert(Word(com[1]))
            elif com[0] == "S":
                word = dictionary.search(Word(com[1]))
                print(str(word))
    except KeyboardInterrupt:
        print("Exiting gracefully!")

