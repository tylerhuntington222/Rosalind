import numpy as np
def main():
    strand = ""
    count = 0
    with open('data', 'r') as f:
        for line in f:
            if not line.startswith('>'):
                strand += line.strip()
            else:
                count += 1
    l = len(strand)//count

    # init numpy array
    d = np.array(list(strand)).reshape(len(strand)//l, l)

    profile = np.zeros((4, l))

    bases = "ACGT"
    for i in range(len(bases)):
        for j in range(l):
            profile[i, j] = list(d[:, j:j+1]).count(bases[i])

    cons = ""
    for i in range(l):
        lst = list(profile[:, i:i+1])
        m = max(lst)
        idx = lst.index(m)
        cons += bases[idx]

    print(cons)
    for i in range(len(bases)):
        print("%s:" %bases[i], end = " ")
        for j in range(l):
            print("%d" % profile[i, j], end = " ")
        print()





main()
