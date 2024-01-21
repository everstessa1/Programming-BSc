# Problem Set 6
# Name: Tessa Evers (#10550062)
# Time: 22:00
# mariomore.py: Prints a piramid with a height between zero and 23.


import cs50

def main():

    # Get a positive integer for the height of te wall.
    print ('Hi there! Please enter a int between 0 and 23.\n')
    h = get_positive_int()
    wall(h)

    # Fuction to import right value for height.
    def get_positive_int():
        while True:
            height = cs50.get_int()
            if height > 0 and height < 24:
                break
            print ("Please make sure the height is between zero and 23.")
        return height

    # Function which prints the wall.
    def wall(h):
        i = 1
        j = 1
        n = 1
        k = 1
        m = 1

        # for every row print the right hashes and spaces.
        for n in range(1, h + 1):
            for i in range(1, h - n + 1):
                print(" ", end ='')
            for j in range(1, n + 2):
                print("#", end ='')
            print(" ", end='')
            for k in range(1, n + 2):
                print("#", end ='')
            for m in range(1, h - n + 1):
                print(" ", end ='')
            print("\n")


if __name__ == "__main__":
    main()