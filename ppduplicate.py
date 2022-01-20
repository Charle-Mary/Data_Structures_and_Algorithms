from collections import defaultdict, Counter, deque
def removeDuplicates(self, s: str, k: int) -> str:
    newstring = ""
    hashTable = defaultdict(list)

    for index, char in enumerate(s):
        hashTable[char].append(index)
        newstring += char
        if len(hashTable[char]) == k:
            newstring.replace(char, "")

    return newstring


class Leaderboard:
    def __init__(self):
        self.counter = Counter()


    def addscore(self, playerid, score):
        self.counter[playerid] += score

    def top(self, k):
        return sum(map(lambda x: x[1], self.counter.most_common(k)))

    def reset(self, playerid):
        self.counter[playerid] = 0


class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward = []
        self.backward = []
        self.backward.append(homepage)

    def visit(self, url: str) -> None:
        self.backward.append(url)

    def back(self, steps: int) -> str:
        if self.backward and steps > len(self.backward):
            return self.backward[0]
        for i in range(steps):
            x = self.backward.pop()
            self.forward.append(x)
        return self.backward[-1]

    def forward(self, steps: int) -> str:
        if self.forward and steps > len(self.forward):
            return self.forward[0]
        for i in range(steps):
            x = self.forward.pop()
            self.backward.append(x)
        return self.forward[-1]


b = BrowserHistory("google.com")
b.visit("youtibe")
b.visit("whatdapp")
b.visit("twittet")
b.visit("facebool")
b.visit("linkedin")

print(b.back(3))


class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        count = 0
        d = defaultdict()

        for i,j in pairs:
            d[i] = set(preferences[i][:preferences[i].index(j)])
            d[j] = set(preferences[j][:preferences[j].index(i)])

        for friend in d:
            for pref in d[friend]:
                if friend in d[pref]:
                    count += 1
                    break
        return count




#
# n = 4
# preferences = [[1,3,2],[2,3,0],[1,0,3],[1,0,2]]
# pairs = [[2,1],[3,0]]
# soln = Solution()
#
# print(soln.unhappyFriends(n, preferences, pairs))


class Solut:
    def killprocess(self,pid,ppid,kill):
        d = defaultdict(list)

        for i,pp in enumerate(ppid):
            d[pp].append(pid[i])

        queue = deque([kill])
        res = []
        while queue:
            parent_node = queue.popleft()
            res.append(parent_node)

            queue.extend(d[parent_node])

        return res

    def recurkillprocess(self,pid,ppid,kill):
        d = defaultdict(list)

        for i,pp in enumerate(ppid):
            d[pp].append(pid[i])
        res = []
        def dfs(node,visited = {}):
            visited[node] = True

            res.append(node)
            for nx in d[node]:
                if nx in visited:
                    continue
                dfs(nx,visited)

        dfs(kill)
        return res


#
#
# pid = [1,3,10,5]
# ppid = [3,0,5,3]
# k = 5
# kill = Solut()
# print(kill.recurkillprocess(pid,ppid,k))


class Sotion:
    def decode(self, s, index):
        res = ""
        k = 0
        while index < len(s):
            while s[index].isdigit():
                k = k * 10 + int(s[index])
                index += 1

            if s[index] == "[":
                r, i = self.decode(s, index + 1)
                res += r * k
                k = 0
                index = i + 1
            elif s[index] == "]":
                return res, index
            else:
                res += s[index]
                index += 1
        return res, index

    def decodeString(self, s: str) -> str:
        ans, pos = self.decode(s, 0)
        return ans



soln = Sotion()
print(soln.decodeString("2[abc]3[cd]ef"))























