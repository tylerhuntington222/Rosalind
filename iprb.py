
def main():

    with open('data', 'r') as f:
        data = f.readline()

    nums = data.split(' ')
    dom = float(nums[0])
    het = float(nums[1])
    rec = float(nums[2])
    pop = dom + het + rec

    print("%d %d %d %d" % (dom, het, rec, pop))

    # P(d) =  P(d) | dom*dom (case 1)
    #        + P(d)|dom*rec  (case 2)
    #        + P(d)|dom*het  (case 3)
    #        + P(d)|het*het  (case 4)
    #        + P(d)|het*rec  (case 5)

    # case 1:
    p1 = dom/pop * (dom-1)/(pop-1)
    print(str(p1))

    # case 2:
    p2 = dom/pop * (rec)/(pop-1)
    print(str(p2))

    # case 3:
    p3 = (dom/pop) * (het)/(pop-1)
    print(str(p3))

    # case 4:
    p4 = (het/pop) * (het-1)/(pop-1) * 0.75
    print(str(p4))

    # case 5:
    p5 = (het/pop) * (rec)/(pop-1) * 0.5
    print(str(p5))

    p_d = sum([p1, 2*p2, 2*p3, p4, 2*p5])

    print("%f" % p_d)

main()
