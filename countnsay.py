class Solution:
    def trap(self, height) -> int:
        max_left = [0] * len(height)

        for i in range(1, len(height)):
            max_left[i] = max(height[i - 1], max_left[i - 1])

        max_right = [0] * len(height)

        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(height[i + 1], max_right[i + 1])

        res = 0

        for i in range(len(height)):
            water_level = min(max_left[i], max_right[i])

            if water_level >= height[i]:
                res += water_level - height[i]

        return res



def countnsay(num):
    if num == 1:
        return "1"

    prev = countnsay(num - 1)
    ct = 1
    res = ""
    for i in range(len(prev)):
        if i == len(prev) - 1 or prev[i] != prev[i + 1]:
            res += str(ct) + prev[i]
            ct = 1
        else:
            ct += 1
    return res


def validParenthesis(st):
    if not st:
        return
    stack = []

    matches = {"{":"}", "[":"]", "(":")"}

    for i in st:
        if i in matches:
            stack.append(i)
        elif len(stack) > 0 and i == str(matches[stack.pop()]):
            continue
        else:
            return False

    if len(stack) == 0:
        return True

def swap(num, ind1, ind2):
    num[ind1], num[ind2] = num[ind2], num[ind1]
def reverse(num, beg, end):
    while beg < end:
        swap(num, beg, end)
        beg += 1
        end -= 1
def next_greater_permutation(num):
    if len(num) == 1:
        return

    if len(num) == 2:
        return swap(num, 0, 1)
    dec = len(num) - 2
    while dec >= 0 and num[dec] >= num[dec + 1]:
        dec -= 1

    reverse(num, dec + 1, len(num) -1)
    if dec == -1:
        return num
    next_num = dec + 1

    while next_num < len(num) and num[next_num] <= num[dec]:
        next_num += 1

    swap(num, dec, next_num)

    return next_num

from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            d[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return d.values()