from collections import defaultdict
from queue import Queue
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
            else:
                lst = []
                queue = Queue(0)
                seen[email] = True
                queue.put(email)

                while not queue.empty():
                    current_email = queue.get()
                    lst.append(current_email)

                    for adjacent_email in graph[current_email]:
                        if seen.get(adjacent_email):
                            continue
                        else:
                            seen[adjacent_email] = True
                            queue.put(adjacent_email)

                res.append([d[email]] + sorted(lst))
        return res











accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]
soln = Solution()

soln.accountsMerge(accounts)


