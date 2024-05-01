from scripts.screenplay_parser import collect_character_names

# Creates nodes for Radix Trie that will store string segments
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Creates Radix Trie to store character names
class Trie:
    # Initializes the root node
    def __init__(self):
        self.root = TrieNode()

    # Inserts a character into the trie
    def insert(self, name):
        # Start at the root node
        node = self.root
        # Iterates over name
        for char in name:
            # Adds character to children if not already a child
            if char not in node.children:
                node.children[char] = TrieNode()
            # Updates to the child node
            node = node.children[char]
        node.is_end_of_word = True

    # Looks for the character name in the trie
    def search(self, name):
        node = self.root
        for char in name:
            # returns an empty list if the character in question not present in data structure
            if char not in node.children:
                return []
            node = node.children[char]
        return self.possible_names(node, name)
    
    # helper function for search to recursively find possible names based on prefix
    def possible_names(self, node, prefix):
        candidate_names = []
        if node.is_end_of_word:
            candidate_names.append(prefix)
        for char, child in node.children.items():
            # calls itself using extend to append possible names to candidate_names
            candidate_names.extend(self.possible_names(child, prefix + char))
        return candidate_names
    
def generate_trie():
    name_trie = Trie()
    # Calls the function to collect character names from screenplays from screenplay_parser.py
    all_names = collect_character_names()
    for name in all_names:
        name_trie.insert(name)
    return name_trie