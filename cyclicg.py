class Solution:
    def findWords(self, board, words):
        self.rows, self.cols = len(board), len(board[0])
        self.board = board
        res = []
        trie = self.buildTrie(words)
        print(trie)
        for i in range(self.rows):
            for j in range(self.cols):
                if board[i][j] in trie:
                    self.dfs(i, j, trie, res)
        return res

    def buildTrie(self, words):
        trie = {}
        for word in words:
            p = trie
            for char in word:
                if char not in p:
                    p[char] = {}
                p = p[char]

            p['*'] = word
        return trie

    def dfs(self, r, c, trie, res):
        char = self.board[r][c]
        last = trie[char].pop('*', False)
        if last:
            res.append(last)
        self.board[r][c] = None
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for row, col in directions:
            if 0 <= row < self.rows and 0 <= col < self.cols and self.board[row][col] in trie[char]:
                self.dfs(row, col, trie[char], res)
        self.board[r][c] = char

        if not trie[char]:
            trie.pop(char)



board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

soln = Solution()
print(soln.findWords(board,words))


def minMeetingRooms(self, intervals):
    start = sorted([i.start for i in intervals])
    end = sorted([i.end for i in intervals])

    res, count = 0, 0
    s,e = 0,0
    while s < len(intervals):
        if start[s] < end[e]:
            s += 1
            count += 1
        else:
            e += 1
            count -= 1
        res = max(res, count)

    return res

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

class Solution(object):
    def countShips(self, sea, topRight, bottomLeft):
        def findShips(topRight,bottomLeft):
            if topRight.y < bottomLeft.y or topRight.x < bottomLeft.x:
                return 0
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))


            if not sea.hasShips(topRight, bottomLeft):
                return 0
            midX = (bottomLeft.x + topRight.x) // 2
            midY = (bottomLeft.y + topRight.y) // 2

            mid = Point(midX, midY)

            topleftQ = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
            toprightQ = findShips(topRight, Point(mid.x + 1, mid.y  + 1))
            bottomleftQ = findShips(Point(mid.x, mid.y), bottomLeft)
            bottomrightQ = findShips(Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))

            return topleftQ + toprightQ + bottomrightQ + bottomleftQ

        return findShips(topRight, bottomLeft)





