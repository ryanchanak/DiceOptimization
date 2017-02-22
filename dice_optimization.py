from matplotlib import pyplot as plt

from dice_simulator import dice_simulator

from dice_stats import dice_statistics
n = int(raw_input("Enter sides of dice: "))

dice1 = dice_simulator(n**2, n) #Rolls n sided dice n-squared number of times and stores it into dice1.
dice2 = dice_simulator(n**2, n) #Rolls n sided dice n-squared number of times and stores it into dice2.

sum_of_dice = [x + y for x, y in zip(dice1, dice2)] #List comprehension using zip that will add each value of the list (x1+y1), (x2+y2), etc
xexperimental = [] #initializing a bunch of empty lists. this could be: xexperimental = range(2, (2 * n) + 1)
yexperimental = []
yplaceholder = []
xactual = [] # could be xactual = range(2, (2 * n) + 1)
yactual = []

for i in range(2, (2 * n) + 1):
    xexperimental.append(i) #Could do this another way, it's convenient to do it here. 
    yexperimental.append(sum_of_dice.count(i))#Counts the number of times it sees 'i' in sum_of_dice and orders based on entry.

for i in range(1, n + 1): #Rolls each possiblity exactly one time. 
    for j in range(1, n + 1):
        yplaceholder.append(i + j)

for i in range(2, (2 * n) + 1): #Same method as the first for loop.
    xactual.append(i)
    yactual.append(yplaceholder.count(i))


difference_in_rolls = [x - y for x, y in zip(yactual, yexperimental)] #Shows a numerical difference for each roll.
print difference_in_rolls
dice_statistics(yplaceholder, n) 
print "______________________________________________________________________________________________________________\n"
dice_statistics(sum_of_dice, n)
print(sum(difference_in_rolls) / len(difference_in_rolls)) #Should ALWAYS be 0.
plt.plot(xexperimental, yexperimental, 'ro', xactual, yactual, 'bo') #plots experimental values in red, statistical values as blue.
plt.show() #displays the plot.
