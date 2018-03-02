

def main():

    s = ""
    with open('data', 'r') as f:
        for line in f:
            if not line.startswith('>'):
                s += line.strip()

    # find rev comp of s

    palindromes = set()
    for i in range(len(s)-3): # for each starting index in s
        for end in range(i+4, i+13): # for each possible ending index
            if end > len(s):
                end = len(s)
            sub = s[i:end]
            rc = find_rc(sub)
            if (sub == rc):
                palindromes.add((i+1, len(s[i:end])))

    # sort pairs by position
    palindromes = sorted(palindromes, key = lambda x: x[0])
    for pos, length in palindromes:
        print("%s %s" %(pos, length))

    print("Lengh = %d" %(len(s)))
    print(s)


def find_rc(s):
    rc = ""
    base_pairs = dict(A='T', C='G', G='C', T='A')
    for b in s:
        rc += base_pairs[b]
    # reverse the rc
    rc = rc[::-1]
    return(rc)

main()
