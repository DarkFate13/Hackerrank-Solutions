for _ in range(int(input())):
    size = int(input()); arr = list(map(int, input().split())); inversion = 0
    inversion += sum([1 if (arr[i] > arr[j]) else 0 for i in range(size) for j in range(i+1, size)])
    print("YES") if(inversion % 2 == 0) else print("NO")