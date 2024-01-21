# Problem Set 6
# Name: Tessa Evers (#10550062)
# Time: 22:00
# greedy.py: prints the amount of coins necessary to give the change owned

import cs50
from array import array

def main():
    print ('Hi there! How much change is owned? \n')
    change = round(100 * get_change_float())
    countcoins(change)

def get_change_float():
    while True:
        change = cs50.get_float()
        if change > 0:
            break
        print ("Please make sure the change is positive and in euro's.")
    return change

def countcoins(c):
    coins_sort = array('I', [25, 10, 5, 1])
    coins_total = 0
    for i in range (0, 3) :
        coins_total = coins_total + c/coins_sort[i]
        c = c % coins_sort[i]

    if c == 0:
        print(" ", coins_total)
    if c > 0:
        print("something went wrong \n", c)

if __name__ == "__main__":
    main()