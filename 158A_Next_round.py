#Problem: 158A - Next Round
#Plan: Count the number of participants who advance to the next round based on their scores.
#Platform: Codeforces

n, k = map(int, input().split())

a = list(map(int, input().split()))

count = 0

for x in a:
    if x >= a[k - 1] and x > 0:
        count += 1

print(count)
