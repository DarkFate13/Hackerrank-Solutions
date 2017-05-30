N, T = list(map(int, input().split())); width = list(map(int, input().split()))

for _ in range(T):
    i, j = list(map(int, input().split()))
    print(min(width[i:j + 1]))