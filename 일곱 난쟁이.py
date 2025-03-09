

h = [int(input()) for _ in range(9)]

total_sum = sum(h)
found = False

for i in range(9):
    for j in range(i + 1, 9):
        if total_sum - (h[i] + h[j]) == 100:

            result = []
            for x in range(9):
                if x != i and x != j:
                    result.append(h[x])

            result.sort()
            for h in result:
                print(h)
            found = True
            break
    if found:
        break