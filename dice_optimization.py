from matplotlib import pyplot as plt

from dice_simulator import dice_simulator

from dice_stats import dice_statistics
n = int(raw_input("Enter sides of dice: "))

dice1 = dice_simulator(n**2, n)
dice2 = dice_simulator(n**2, n)

sum_of_dice = [x + y for x, y in zip(dice1, dice2)]
xexperimental = []
yexperimental = []
yplaceholder = []
xactual = []
yactual = []

for i in range(2, (2 * n) + 1):
    xexperimental.append(i)
    yexperimental.append(sum_of_dice.count(i))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        yplaceholder.append(i + j)

for i in range(2, (2 * n) + 1):
    xactual.append(i)
    yactual.append(yplaceholder.count(i))


difference_in_rolls = [x - y for x, y in zip(yactual, yexperimental)]
print difference_in_rolls
dice_statistics(yplaceholder, n)
print "______________________________________________________________________________________________________________\n"
dice_statistics(sum_of_dice, n)
print(sum(difference_in_rolls) / len(difference_in_rolls))
plt.plot(xexperimental, yexperimental, 'ro', xactual, yactual, 'bo')
plt.show()
