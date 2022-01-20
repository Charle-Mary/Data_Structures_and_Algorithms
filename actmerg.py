from queue import Queue
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts):
        d = {}
        graph = defaultdict(set)

        for account in accounts:
            name = account[0]
            if account[1:]:
                for email in account[1:]:
                    graph[account[1]].add(email)
                    graph[email].add(account[1])
                    d[email] = name

        seen = {}
        res = []
        for email in graph:
            if seen.get(email):
                continue
            lst = []
            queue = Queue(0)
            queue.put(email)
            seen[email] = True

            while not queue.empty():
                current_email = queue.get()
                lst.append(current_email)

                for adjacent_email in graph.get(current_email):
                    if seen.get(adjacent_email):
                        continue
                    else:
                        queue.put(adjacent_email)
                        seen[adjacent_email] = True

            res.append([d[email]] + sorted(lst))

        print(res)






accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
soln = Solution()

soln.accountsMerge(accounts)