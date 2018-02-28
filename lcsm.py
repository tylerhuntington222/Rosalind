def main():

    seqs = []
    s = ""
    new_seq = False
    i = -1
    with open('data', 'r') as f:
        eof = False
        while(not eof):
            line = f.readline().strip()
            if line == "":
                eof = True
                break
            elif line.startswith('>'):
                new_seq = True
                continue
            elif new_seq:
                seqs.append(line)
                new_seq = False
                i += 1
            else:
                seqs[i] += line

    print(seqs)
    print(str(len(seqs)))

    # make first seq the source for deriving all possible substrings
    ref = seqs[0]

    # init longest substring
    longest = ""

    # iterate thru all possible substrings of ref
    for i in range(0, len(ref)-1, 1):
        for j in range(1, len(ref), 1):
            sub = ref[i:j]
            # check if current substring is greater than max so far
            if (len(sub) > len(longest)):
                # check if this substring is common
                counter = 0
                for s in seqs:
                    if sub not in s:
                        break
                    # increment counter for occurences of substring
                    counter += 1
                # make this substring the longest if all seqs contain it
                if counter == len(seqs):
                    longest = sub

    print(longest)

main()
