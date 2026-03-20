from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

dq = deque()  # хранит индексы

for i in range(n):
    # удаляем с хвоста индексы, у которых значения >= a[i]
    while dq and a[dq[-1]] >= a[i]:
        dq.pop()
    dq.append(i)

    # удаляем индексы, вышедшие из окна
    while dq and dq[0] <= i - k:
        dq.popleft()

    # выводим минимум для текущего окна
    if i >= k - 1:
        print(a[dq[0]])
