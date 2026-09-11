#Problem: 282A - Bit++
#Plan: Count the number of increments and decrements based on the input operations.
#Platform: Codeforces

x = 0
for _ in range(int(input())):
    x += 1 if '+' in input() else -1
print(x)
