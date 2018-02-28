

def main():

    with open('data', 'r') as f:
        data = f.readline()

    nums = data.split(' ')
    dd = float(nums[0]) * 2
    dh = float(nums[1]) * 2
    dr = float(nums[2]) * 2
    hh = float(nums[3]) * 0.75 * 2
    hr = float(nums[4]) * 0.50 * 2
    e = sum([dd, dh, dr, hh, hr])



    # P(d) =  P(d) | dom*dom (case 1)
    #        + P(d)|dom*rec  (case 2)
    #        + P(d)|dom*het  (case 3)
    #        + P(d)|het*het  (case 4)
    #        + P(d)|het*rec  (case 5)

    print("%f" % e)

main()
