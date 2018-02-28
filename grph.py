
def main():
    k = 3

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

    # coerce dict into list of tuples where first element in each
    # tuple is the label and the second is the strand
    seq_pairs = list(seqs.items())

    # init list of tuples to store edges
    edges = []
    for s in seq_pairs:
        sfx = s[1][-k:]
        for t in seq_pairs:
            if s[1] == t[1]:
                continue
            else:
                pfx = t[1][0:3]
                if sfx == pfx:
                    edges.append((s[0], t[0]))

    for e in edges:
        print("%s %s" %(e[0], e[1]))


main()
