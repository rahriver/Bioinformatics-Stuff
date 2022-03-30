from statistics import mean, median, mode, stdev, variance

# Calculates mean, median, mode, standard deviation, and variance
def statis(*nums):
    print("Mean:", mean(nums))
    print("Median:", median(nums))
    print("Mode:", mode(nums))
    print("Sum", sum(nums))
    print("Stdev:", round(stdev(nums), 2))
    print("Variance:", round(variance(nums), 2))


# Reads in numbers from user and calculates statistics with some conditions
def run():
    while True:
        nums = input("Enter numbers separated by comma: ").split(',')
        if nums != [""]:
            nums = [int(i) for i in nums]
            statis(*nums)
            cont = input("Continue? (y/n): ")
            while cont != "y" and cont != "n":
                print("Invalid input")
                cont = input("Continue? (y/n): ")
            if cont == "n":
                print("Bye!")
                break
            elif cont == "y":
                continue
        else:
            print("Please enter numbers!")

run()
