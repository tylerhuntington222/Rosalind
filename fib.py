
def main():

    n = 33
    k = 4

    pairs = [1, 1]
    for i in range(2, n):
        pairs.append(pairs[i-2] * k + pairs[i-1])

    res = pairs[n-1]


    # res = recur(n, k)

    print("%d %d" % (n,k))
    print(res)
    assert(res == 7334743797805)

def recur(n, k):

    if n == 1:
        return 1

    if n == 2:
        return 1


    return (k*recur(n-2, k) + recur(n-1, k))


main()
