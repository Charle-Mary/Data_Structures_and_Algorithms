# from collections import defaultdict
#
# cache = defaultdict(int)
#
# def minimumchessmoves(i,j,p,q):
#     matches = {(i-1,j-2):True, (i+1,j-2):True, (i-2,j-1):True, (i+2,j-1):True,
#                (i-1,j+2):True, (i-2,j+1):True, (i+2,j+1):True, (i+1,j+2):True,
#                (i,j-1):True, (i-1,j-1):True, (i-1,j):True, (i-1,j+1):True,
#                (i,j+1):True, (i+1,j+1):True, (i+1,j):True, (i+1,j-1):True}
#
#     if (p,q) in matches:
#         return 1
#
#     if p in range(0,8) and q == j:
#         return abs(i - p)
#     if p in range(0, 8) and q in range(0,j):
#         return 1 + min(minimumchessmoves(i,j,p-1,q), minimumchessmoves(i,j,p-1,q+1),
#                    minimumchessmoves(i,j,p,q+1), minimumchessmoves(i,j,p+1,q),
#                    minimumchessmoves(i,j,p+1,q+1), minimumchessmoves(i,j,p+1,q+2),
#                    minimumchessmoves(i,j,p+2,q+1))
#     elif p in range(0, 8) and q in range(j+1,8):
#         return 1 + min(minimumchessmoves(i,j,p-1,q), minimumchessmoves(i,j,p+1,q),
#                    minimumchessmoves(i,j,p-1,q-1), minimumchessmoves(i,j,p+1,q-1),
#                    minimumchessmoves(i,j,p,q-1), minimumchessmoves(i,j,p+1,q-2),
#                    minimumchessmoves(i,j,p+2,q-1))
#
#
# print(minimumchessmoves(4,4,1,4))
#
#
def minimumchessmoves(i,j,p,q):
    dp = [[0 for j in range(8)] for i in range(8)]

