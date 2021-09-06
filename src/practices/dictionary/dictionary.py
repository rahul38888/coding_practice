
class Definition:
    def __init__(self, type: str, definition: str = None):
        self.type = type
        self.definition = definition

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__str__()

class Word:
    def __init__(self, word: str):
        self.word = word
        self.definitions = []

    def add_definition(self, definitions: list):
        if not definitions:
            return

        self.definitions += definitions

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__str__()


class Node:
    def __init__(self):
        self.child_nodes = {}
        self.word = None

    def insert(self, word: Word, cur_index: int = 0):
        if word.word is None or len(word.word) == 0:
            # Such words are not stored
            return

        w = word.word.lower()
        if cur_index == len(w):
            if self.word is not None:
                self.word.add_definition(word.definitions)
            else:
                self.word = word
        else:
            key = w[cur_index]
            if not self.child_nodes.__contains__(key):
                self.child_nodes[key] = Node()
            self.child_nodes[key].insert(word, cur_index+1)

    def search(self, word: str, cur_index: int = 0) -> Word:
        if word is None or len(word) == 0:
            # Such words are not stored
            return None

        word = word.lower()
        if cur_index == len(word):
            return self.word
        else:
            key = word[cur_index];
            if not self.child_nodes.__contains__(key):
                # Word do not exists
                return None
            return self.child_nodes[key].search(word, cur_index+1)


class Dictionary(Node):
    def __init__(self):
        super(Dictionary, self).__init__()


