
def main():

    n = 7

    global perms
    perms = []
    nums = set(range(1,n+1))

    print(permutations(nums))

    # find all permutations that start with 1
    rec_helper(nums, [])

    print(str(fact(n)))
    for i in perms:
        for j in i:
            print(j, end = " ")
        print()


def rec_helper(nums, p):
    print(p)
    if len(p) == len(nums):
        return(perms.append(p))
    else:
        poss = list(nums - set(p))
        print("POSS: ", poss)
        for i in poss:
            # create new prefix
            new = list(p)
            new.append(i)
            rec_helper(nums, new)

def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


main()
