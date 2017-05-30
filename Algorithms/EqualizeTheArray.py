from collections import Counter

N = int(input()); arr = list(map(int, input().split()))
print(N - Counter(arr).most_common(N)[0][1])