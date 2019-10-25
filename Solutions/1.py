def sum(a, b):
    c = a // b
    return b * (c * (c+1)) // 2
  
def euler1(a):
    return sum(a, 3) + sum(a, 5) - sum(a, 15)

t = int(input().strip())
for i in range(t):
    N = int(input().strip())
    print(euler1(N - 1)) # below N
