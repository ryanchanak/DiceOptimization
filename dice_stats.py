def dice_statistics(dice_sums, n):
    for i in range(2, ((2 * n) + 1)):
        print("The odds of two dice equaling {} is: {}%.".format(i, dice_sums.count(i) * 100.00 / n ** 2))
