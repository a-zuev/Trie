class Trie:
    '''Memory-inefficient implementation of Trie with dictionaries.'''
    def __init__(self):
        self.children = dict()
        self.is_end = False

    def check_word(self, word):
        curr_node = self
        for w in word:
            if not w in curr_node.children:
                return False
            curr_node = curr_node.children[w]
        return curr_node.is_end

    def add_word(self, word):
        curr_node = self
        for w in word:
            if not w in curr_node.children:
                curr_node.children[w] = Trie()
            curr_node = curr_node.children[w]
        curr_node.is_end = True
