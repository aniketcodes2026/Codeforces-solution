#Problem: Domino piling 
#Concept: Given a rectangular board of size m×n, determine the maximum number of dominoes that can be placed on the board. Each domino covers exactly two squares.
#Platform: Codeforces

m, n = map(int, input().split())
print((m * n) // 2)