
def main():

    with open('data', 'r') as f:
        data = f.readline()

    t = ""
    for i in data:
        if i == "T":
            t += "U"
        else:
            t += i
    t = t.strip()
    print (t)

main()
