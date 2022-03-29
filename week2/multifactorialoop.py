import random


class Factorial:
  def __call__(self, n, k):
    if n <= 1:
      return 1
    return n * self(n - k, k)


def test():
  macoop = Factorial()
  n = random.randint(0, 750)
  k = random.randint(0, 900)
  print(f"{n}!({k}) =", macoop(n, k))
  n = random.randint(0, 750)
  k = random.randint(0, 900)
  print(f"{n}!({k}) =", macoop(n, k))
  n = random.randint(0, 750)
  k = random.randint(0, 900)
  print(f"{n}!({k}) =", macoop(n, k))


def run():
  macoop = Factorial()
  try:
    n = int(input("What multifactorial? "))
    k = int(input("How many steps? "))
    if n > 750 or n < 0:
      print("input a number between 0 and 750")
    elif k < 0:
      print("input a number greater than 0")
    else:
      print(f"{n}!({k}) =", macoop(n, k))
  except:
    print("integer")
