class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, contact):
        current_node = self.root

        for char in contact:
            if current_node.children.get(char):
                current_node = current_node.children[char]

            else:
                new_node = TrieNode()

                current_node.children[char] = new_node

                current_node = new_node

        current_node.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(child_node, word + key, words)

        return words


    def find(self, prefix):
        current_node = self.root
        all_find = []
        char_so_far = ""
        for char in prefix:
            if current_node.children.get(char):
                char_so_far += char
                current_node = current_node.children[char]

            else:
                return 0



        for word in self.collectAllWords(current_node):
            if word != "":
                all_find.append(char_so_far + word)
            else:
                all_find.append(char_so_far)

        return len(all_find)

    def traverse(self, node=None):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            print(key, end=',')
            if key != "*":
                self.traverse(child_node)



mytrie = Trie()



def contacts(queries):
    all_finds = []
    count = 0
    for query in queries:
        query = query.split(' ')
        if query[0] == "add":
            mytrie.add(query[1])
        elif query[0] == "find":
            if not all_finds:
                all_finds.append(mytrie.find(query[1]))
            else:
                all_finds.append(mytrie.find(query[1]) - all_finds[count])
                count += 1

    return all_finds


queries = ['add ed', 'add eddie', 'add edward', 'find ed', 'add edwina', 'find edw', 'find a', 'find e']

print(contacts(queries))

mytrie.traverse()



# mytrie.add("ed")
# mytrie.add("eddie")
# mytrie.add("edwards")
# mytrie.add("edwina")
# print(mytrie.find("edwik"))
# # print(mytrie.find("edw"))
# # print(mytrie.find("a"))

