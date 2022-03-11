def sort(a, b):
    if b < a:
        a, b = b, a
    return a, b


if __name__ == "__main__":
  a = input("first number")
  b = input("second numer")
  print(', '.join(sort(a, b)))
