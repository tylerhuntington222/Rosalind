
def main():

    n = 94
    m = 17

    # indices of this list correspond to generations
    # value at each index is the number of breeding pairs of rabbits in
    # that generation
    pairs = [1, 1]

    def fib(i, j):
        count = 2 # number of months gone by
        while count < i:
            if count < j: # no rabbits have died
                pairs.append(pairs[-2] + pairs[-1])
            # base cases for subtracting rabbit deaths of seed pair
            elif count == j or count == j+1:
                pairs.append((pairs[-2] + pairs[-1])-1)

            # recurrence relation accounting for deaths in subsequent gens
            else:
                pairs.append(pairs[-2] + pairs[-1] - pairs[-(j+1)])

            count += 1

        return pairs[-1]






    # res = recur(n, k)

    print("%d" % fib(n,m))
#
# def recur(n, k):
#
#     if n == 1:
#         return 1
#
#     if n == 2:
#         return 1
#
#
#     return (k*recur(n-2, k) + recur(n-1, k))


main()
