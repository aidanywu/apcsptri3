import random


class Factorial:
  def __call__(self, n):
    if n <= 1:
      return 1
    return n * self(n - 1)


def test():
  fac = Factorial()
  n = random.randint(0, 100)
  print(f"Factorial of {n}:", fac(n))
  n = random.randint(0, 100)
  print(f"Factorial of {n}:", fac(n))
  n = random.randint(0, 100)
  print(f"Factorial of {n}:", fac(n))


def run():
  fac = Factorial()
  try:
    n = int(input("What factorial? "))
    if n > 500 or n < 0:
      print("input a number between 0 and 500")
    else:
      print(fac(n))
  except:
    print("integer")
