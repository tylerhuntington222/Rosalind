
def main():

    seqs = {}
    s = ""
    with open('data', 'r') as f:
        eof = False
        while(not eof):
            line = f.readline().strip()
            if line == "":
                eof = True
                break
            elif line.startswith('>'):
                label = line[1:]
                seqs[label] = ""
            else:
                seqs[label] += line

    for k in seqs.keys():
        seqs[k] = calc_gc(seqs[k])

    # sort sequences based on GC constant
    seqs = list(sorted(seqs.items(), key = lambda x: x[1], reverse = True))
    print(seqs[0][0])
    print("%7.6f" % seqs[0][1])


def calc_gc(s):
    count = 0
    for c in s:
        if c == 'G' or c == 'C':
            count += 1

    print(s)
    return (100*count/len(s))


main()
