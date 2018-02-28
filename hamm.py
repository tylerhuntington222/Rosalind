
def main():

    with open('data', 'r') as f:
        s1 = f.readline()
        s2 = f.readline()
    ham = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ham += 1

    print(ham)

main()
