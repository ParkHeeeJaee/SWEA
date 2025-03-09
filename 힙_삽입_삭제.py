heap = [0] * 11

last = 0

def enq(item):
    global last
    last += 1
    heap[last] = item

    c = last
    p = c // 2

    while p > 0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]

        c = p
        p = c // 2

def deq():
    global last

    root = heap[1]

    heap[1] = heap[last]

    last -= 1

    p = 1
    c = p * 2

    while c <= last:

        if c + 1 < last and heap[c] < heap[c+1]:
            c = c + 1

        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]

            p = c
            c = c * 2
        
        else:
            break
    return root

arr = [ 6, 4, 5, 2, 3, 2, 9, 7, 8, 10]

for i in arr:
    enq(i)

print(heap
)

sorted.arr = []

for i in