Problem: Team
Platform: Codeforces

n = int(input())
count = 0

for _ in range(n):
# Sum the 3 inputs; increment if at least 2 are confident (1)
    
    if sum(map(int, input().split())) >= 2:
        count += 1

print(count)