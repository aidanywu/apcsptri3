import re


class Palindrome:
  def __call__(self, n):
    n = re.sub(r'[^a-zA-Z0-9]', '', n).lower()
    if n == n[::-1]:
      return " "
    else:
      return " not "


def test():
  pal = Palindrome()
  n = "palindrome"
  print(f'"{n}" is' + pal(n) + "a palindrome")
  n = "taco cat"
  print(f'"{n}" is' + pal(n) + "a palindrome")
  n = "Sit on a potato pan, Otis."
  print(f'"{n}" is' + pal(n) + "a palindrome")
  n = "Able was I, ere I saw Elba."
  print(f'"{n}" is' + pal(n) + "a palindrome")
  n = "Able waOs I, ere I saw Elba."
  print(f'"{n}" is' + pal(n) + "a palindrome")
  n = "this is not a palindrome"
  print(f'"{n}" is' + pal(n) + "a palindrome")


def run():
  pal = Palindrome()
  try:
    n = input("Enter your string ")
    print(f'"{n}" is' + pal(n) + "a palindrome")
  except:
    print("string")
