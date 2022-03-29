import week0.swap as swap


def fibterm(a, b, n):
  if n == 1:
    return a
  elif n == 2:
    return b
  elif n > 2:
    return fibterm(a, b, n - 1) + fibterm(a, b, n - 2) # recursive to add the previous two terms in the fibonacci sequence


def term():
  try:
    a = int(input("What is one starting number?\n"))
    b = int(input("What is the other starting number?\n"))
    n = int(input("Which nth term do you want to print?\n"))
    
    a, b = swap.sort(a, b) # to make sure the first number entered into the function is smaller than the second
    print(fibterm(a, b, n))
  except:
    print("integer")

def seq():
  try:
    a = int(input("What is one starting number?\n"))
    b = int(input("What is the other starting number?\n"))
    n = int(input("To which term do you want to print?\n"))
    a, b = swap.sort(a, b)
    print(", ".join([str(fibterm(a, b, i + 1)) for i in range(0, n)])) # Creates a list with all the fibonacci sequence numbers in order with for loop calling the fibterm(a, b, n) function with n increasing each time. Then makes the list into a sequence of numbers separated by commas (", ")
  except:
    print("integer")