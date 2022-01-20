class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        current_node = self.root
        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                return None

        return current_node


    def insert(self, word, priority=0):
        current_node = self.root

        for char in word:
            if current_node.children.get(char):
                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node

                current_node = new_node

        current_node.children["*"] = priority



    def collectAllWords(self, node=None, word="", words=[]):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(child_node, word + key, words)

        return words


    def autoComplete(self, prefix):
        current_node = self.search(prefix)

        if not current_node:
            return None

        return self.collectAllWords(current_node)

    def traverse(self, node=None):
        current_node = node or self.root
        for key, child_node in current_node.children.items():
            print(key, end=',')
            if key != "*":
                self.traverse(child_node)


    def autoCorrect(self, word):
        current_node = self.root

        char_so_far = ""
        for char in word:
            if current_node.children.get(char):
                char_so_far += char
                current_node = current_node.children[char]
            else:
                return char_so_far + self.collectAllWords(current_node)[0]
        return word




mytrie = Trie()

mytrie.insert("cat")
mytrie.insert("catnap")
mytrie.insert("catnip")
mytrie.insert("charles")
mytrie.insert("cherry")
mytrie.insert("youghurt")
mytrie.insert("youversion")
mytrie.insert("you")
mytrie.insert("joeman")
mytrie.insert("joemanni")
mytrie.insert("joken")
mytrie.insert("scissors")
mytrie.insert("scientific")


y = mytrie.autoCorrect("youkeps")

print(y)



