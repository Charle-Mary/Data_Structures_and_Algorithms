# class TrieNode:
#     def __init__(self):
#         self.children = {}
#
#
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#
#
#     def search(self, word):
#         current_node = self.root
#
#         for char in word:
#             if current_node.children.get(char):
#                 current_node = current_node.children[char]
#             else:
#                 return None
#
#         return current_node
#
#
#     def insert(self, word):
#         current_node = self.root
#
#         for char in word:
#             if current_node.children.get(char):
#                 current_node = current_node.children[char]
#             else:
#                 newNode = TrieNode()
#                 current_node.children[char] = newNode
#
#                 current_node = newNode
#
#         current_node.children["*"] = None
#
#
#
#     def collectAllWords(self, node=None, word="", words=[]):
#         current_node = node or self.root
#
#         for key, child_node in current_node.children.items():
#             if key == "*":
#                 words.append(word)
#
#             else:
#                 self.collectAllWords(child_node, word + key, words)
#
#         return words
#
#
#
#     def autoComplete(self, prefix):
#         currentNode = self.search(prefix)
#
#         if not currentNode:
#             return
#         return self.collectAllWords(currentNode)


class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        # self.root = TrieNode()
        self.root = {}

    def insert(self, word):
        current_node = self.root

        for char in word:
            if current_node.get(char):
                current_node = current_node[char]
            else:
                new_node = {}
                current_node[char] = new_node

                current_node = new_node

        current_node["*"] = True

    def search(self, word):
        current_node = self.root

        for char in word:
            if current_node.get(char):
                current_node = current_node[char]
            else:
                return False

        return "*" in current_node

    def startsWith(self, prefix):
        current_node = self.root

        for char in prefix:
            if current_node.get(char):
                current_node = current_node[char]
            else:
                return False
        return True

    def collectallwords(self, node=None, word="", words=[]):
        current_node = node or self.root
        for key, child_node in current_node.items():
            if key == "*":
                words.append(word)
            else:
                self.collectallwords(child_node, word + key, words)

        return words


class Solution:
    def findWords(self, board, words):
        t = Trie()
        for word in words:
            t.insert(word)

        print(t.root)
        print(t.root['o'])
        print('a' in t.root['o'] )

        N = len(board)
        M = len(board[0])
        output = []

        def dfs(row, col, path):
            if row < 0 or row >= N or col < 0 or col >= M or board[row][col] == 0:
                return

            temp = path + [board[row][col]]
            string = "".join(temp)

            if not t.startsWith(string):
                return
            elif t.search(string) and string not in output:
                output.append(string)
            placeholder = board[row][col]
            board[row][col] = 0
            dfs(row - 1, col, temp)
            dfs(row + 1, col, temp)
            dfs(row, col - 1, temp)
            dfs(row, col + 1, temp)

            board[row][col] = placeholder

        for r in range(N):
            for c in range(M):
                dfs(r, c, [])

        return output


board = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
# words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
words = ["oath","pea","eat","rain"]
s = Solution()
print(s.findWords(board, words))


# def build_trie(words):
#     trie = {}
#     for word in words:
#         p = trie
#         for c in word:
#             if c not in p:
#                 p[c] = {}
#             p = p[c]
#         p['$'] = word
#     return trie
#
# words = ["oath","pea","eat","rain"]
# trie = build_trie(words)
# print(trie)
#










