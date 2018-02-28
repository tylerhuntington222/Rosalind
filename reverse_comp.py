
def main():

    with open('data', 'r') as f:
        data = f.readline()
    data = data.strip()

    bp = {'A':'T', 'C':'G', 'G': 'C', 'T':'A'}
    r = ""
    for c in data:
        r += (bp[c])
    r = r[::-1]

    print(r)
    expected = "ACCGGGTTTT"
    assert(r == expected)

main()
