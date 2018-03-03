import bisect

def find_LIS(i, l, s):
    max_lj = list()
    for j in range(i):
        if s[j] < s[i]:
            if len(l[j]) > len(max_lj):
                max_lj = list(l[j])
    max_lj.append(s[i])
    l.append(max_lj)



def main():

    with open('data', 'r') as f:
        n = int(f.readline().strip())
        permutations = f.readline().strip()

    s = list(map(lambda x: int(x), permutations.split()))

    # initialization: longest increasing subseq of S ending in first element
    # of S is the first element itself.
    l = [[s[0]]]

    # populate DP table (i.e. l[i] array)

    for i in range(1,len(s)):
        find_LIS(i, l, s)

    longest_inc = max(l, key = lambda x: len(x))

    s.reverse()
    l = [[s[0]]]
    for i in range(1, len(s)):
        find_LIS(i, l, s)

    longest_dec = max(l, key = lambda x: len(x))


    for i in longest_inc:
        print(i, end = " ")
    print()
    for j in reversed(longest_dec):
        print(j, end = " ")
    print()




    # for start in range(0, len(perms)):
    #     inc = [perms[start]]
    #     dec = [perms[start]]
    #     for pos in range(start, len(perms)):
    #         # next element is strictly larger than largest so far
    #         if perms[pos] > inc[-1]:
    #             inc.append(perms[pos])
    #             if len(inc) > len(longest_inc):
    #                 longest_inc = inc
    #         # next element is larger than first in cur but not largest so far
    #         elif perms[pos] > inc[0]:
    #             idx = bisect.bisect(inc, perms[pos])
    #             inc = inc[0:idx]
    #             inc.append(perms[pos])
    #
    #         # next element is stricly less than smallest so far
    #         if perms[pos] < dec[0]:
    #             bisect.insort(dec, perms[pos])
    #             if len(dec) > len(longest_dec):
    #                 longest_dec = dec
    #         # next element is smaller than first of this subseq but not smallest
    #         elif perms[pos] < dec[-1]:
    #             idx = bisect.bisect(dec, perms[pos])
    #             dec = dec[idx:]
    #             bisect.insort(dec, perms[pos])
    #
    #     if len(inc) > len(longest_inc):
    #         longest_inc = inc
    #     if len(dec) > len(longest_dec):
    #         longest_dec = dec



main()
