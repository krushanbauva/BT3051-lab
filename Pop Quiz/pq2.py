# BT5071 pop quiz 2
# Roll Number: BE17B037
# Name: Krushan Bauva

def bubble(A):
    n = len(A)
    if n%2 == 1:
        A1 = A[0:n//2+1]
        A2 = A[n//2+1:n]
    else:
        A1 = A[0:n//2]
        A2 = A[n//2:n]
    n1 = len(A1)
    for i in range(n1-1, 0, -1):
        for j in range(i):
            if A1[j]>A1[j+1]:
                A1[j], A1[j+1] = A1[j+1], A1[j]
    n2 = len(A2)
    for i in range(n2-1):
        for j in range(n2-1, i, -1):
            if A2[j]>A2[j-1]:
                A2[j], A2[j-1] = A2[j-1], A2[j]
    return (A1, A2)

# Bubble sort is a stable sort since it does not reorder for equal things. Only when one
# element is greater than the other, it does a mutual swap between them.

# Bubble sort's time complexity is O(n^2). Since the outer loop runs for n-1 times and the inner
# loop runs till the index of the outer loop. So if we add all these we get approx =
# (n-1)^2 + (n-2)^2 + (n-3)^2 + ..... (3)^2 + (2)^2 + (1)^2 = n(n-1)/2 = O(n^2)
# Hence the time complexity of bubble sort is O(n^2).
