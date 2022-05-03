{% include navigation.html %}


This is my create task project:

[Written Reponse](https://docs.google.com/document/d/1_nrFpaxsFv2YobHlV51FNnMBLl7nVFk4hVXPjioW8K8/edit?usp=sharing)

[Video]()

```
import random
import re


def run():
    try:
        print("Mean, Median, Mode, Range Calculator\n-------------------------------------")
        # Get choice input of quiz or choice, 1 or 2 respectively after removing all characters except numbers
        inp = int(re.sub('[^0-9]', '', input("Would do you like to use the calculator or test yourself with a quiz?\n1: Calculator\n2: Quiz\n3: Exit\n\nChoice: ")))
        option(inp)
    except ValueError:
        print("Error: Numbers only")
        run()


def option(n):
    try:
        # Uses if statements to decide what option to run
        if n == 1:
            # Get input and split it into a list using delimiters of anything that aren't numbers with regex
            l =  re.split('[^0-9]+', input("Enter your numbers separated by spaces, commas, colons, or semicolons:\n"))
            # Removes the list of any empty elements with a for loop (iteration) and makes each element an integer
            l = [int(i) for i in l if i]
            # runs the calculate function with the nums list as a parameter
            print("Calculations for", ', '.join([str(i) for i in l]))
            all(l)
        elif n == 2:
            # Runs quiz function
            quiz()
        elif n == 3:
            # Returns nothing and ends the program
            return
        else:
            # When the user inputs an integer not associated with a choice
            print("Please enter 1, 2, or 3")
            run()
    except ValueError:
        print("Error: Numbers only")
        run()


def all(l):
    # Returns the mean, median, range, and mode of the inputted numbers, formatted
    print("Mean: ", mean(l), "\nMedian: ", median(l), "\nRange: ", ran(l), "\nMode: ", ', '.join(mode(l)))
    # Reruns the option choosing
    run()


def mean(l):
    # Returns the average by summing up all terms in the list and dividing by the length of the list (the amount of numbers)
    return sum(l)/len(l)


def median(l):
    # Returns the number in the middle of the sorted inputted numbers, or the median
    if len(l) % 2 == 1:
        return sorted(l)[len(l)//2]
    # Returns the average of the numbers in the middle of the sorted inputted numbers, or the median
    elif len(l) % 2 == 0:
        return (sorted(l)[len(l)//2 - 1] + sorted(l)[len(l)//2]) / 2


def ran(l):
    # Returns the difference between the largest and smallest numbers in the inputted numbers, or the range
    return max(l) - min(l)


def mode(l):
    d = {}
    # Creates a dictionary where the keys are the numbers that appear in the list and the values are the respective times the number appears in the inputted numbers.
    for i in range(len(l)):
        if l[i] not in d:
            # Creates a dictionary item if the number checked isn't already in the dictionary
            d[l[i]] = 1
        else:
            # Adds 1 to the dictionary value which corresponds to the number checked if a key with the number already exists
            d[l[i]] += 1
    nd = {}
    for k, v in d.items():
        # Adds items in the previously defined dictionary which has the largest values (number of times they appear in the inputted numbers) to the newly defined dictionary
        if v == max(list(d.values())):
            nd[str(k)] = v
    # Returns a list of all keys in the new dictionary, which are the numbers with the greatest number of appearance in the inputted numbers
    return list(nd.keys())


def quiz():
    l = []
    # Creates a list with a random length between 1 and 15 inclusive where each element has a random value between 0 and 100 inclusive
    for i in range(random.randint(1, 15)):
        l.append(random.randint(0, 100))
    # Creates a random number between 1 and 4 inclusive to decide which problem type will be asked if the user doesn't specify which one they want
    types = int(re.sub('[^0-9]', '', input("Would you like to do a mean, median, range, or mode question?\n1: Mean\n2: Median\n3: Range\n4: Mode\n5: Random\n\nChoice: ")))
    answer = 100000
    if types == 5:
        types = random.randint(1, 4)
    if types == 1:
        solution = int(round(mean(l)))
        while int(round(answer)) != solution:
            try:
                answer = int(input("What is the mean of " + ', '.join([str(i) for i in l]) + " (Please round to the nearest whole number)?\n"))
            except ValueError:
                print("Please enter an integer")
            if int(round(answer)) != solution:
                print("Incorrect\n")
        print("Correct\n")
        next()        
    elif types == 2:
        solution = median(l)
        while float(answer) != solution:
            try:
                answer = float(input("What is the median of " + ', '.join([str(i) for i in l]) + " (Please don't round)?\n"))
            except ValueError:
                print("Numbers only")
            if float(answer) != solution:
                print("Incorrect\n")
        print("Correct\n")
        next()
    elif types == 3:
        solution = ran(l)
        while answer != solution:
            try:
                answer = int(input("What is the range of " + ', '.join([str(i) for i in l]) + " ?\n"))
            except ValueError:
                print("Please enter an integer")
            if answer != solution:
                print("Incorrect\n")
        print("Correct\n")
        next()
    elif types == 4:
        for i in range(random.randint(1, len(l)//2)):
            for i in range(random.randint(1, 3)):
                l.insert(random.randint(0, len(l) - 1), l[i])
        solution = sorted(mode(l))
        while answer != solution:
            try:
                answer = re.split(r'[^0-9]+', input("What is the mode of " + ', '.join([str(i) for i in l]) + " (Separated by spaces, commas, colons, or semicolons if there are multiple?\n"))
                answer  = sorted([i for i in answer if i])
            except ValueError:
                print("Please enter an integer")
            if answer != solution:
                print("Incorrect\n")
        print("Correct\n")
        next()
    else:
        print("Enter a number between 1 and 5 inclusive")


def next():
    try:
        n = int(re.sub(r'[^0-9]', '', input("Would do you like to go to the next question?\n1: Yes\n2: No\n\nChoice: ")))
        # Uses if statements to decide whether to ask another quiz question or to go back and give choices of calculator, quiz, or exit
        if n == 1:
            quiz()
        elif n == 2:
            run()
        else:
            # Asks again if choice isn't valid
            print("Please enter 1 or 2")
            next()
    except ValueError:
        # Asks again if the input isn't an integer
        print("Error: Numbers only")
        next()


if __name__ == "__main__":
    run()
```
