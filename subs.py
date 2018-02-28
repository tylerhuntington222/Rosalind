def main():

    with open('data', 'r') as f:
        s = f.readline().strip()
        t = f.readline().strip()

    motifs = True
    i = 0
    starts = []
    seen = 0
    while motifs:
        try:
            i = (s[seen:]).index(t)
            starts.append(i+seen+1)
            i += 1
            seen += i
        except ValueError:
            motifs = False

    for val in starts:
        print("%d " % val, end = ""),

main()
