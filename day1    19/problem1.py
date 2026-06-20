n = int(input())
a = list(map(int, input().split()))

max_count = 0
count = 0

for num in a:
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print(max_count)