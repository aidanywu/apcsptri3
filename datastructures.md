{% include navigation.html %}


<div class="container py-4">
    <header class="pb-3 mb-4 border-bottom border-primary text-dark">
        <span class="fs-4"><a href="https://github.com/aidanywu/apcsptri3/">Code on Github</a></span>
    </header>
    <header class="pb-3 mb-4 border-bottom border-primary text-dark">
        <span class="fs-4">Replit</span>
    </header>
    <div class="row justify-content-center" style="margin: 10%;">
        <iframe height="800px" width="100%" src="https://repl.it/@aidanywu/apcsptri3?lite=true"></iframe>
    </div>
</div>


InfoDB:
```
infodb = [{
            "Name": "John",
            "Favorite Subject": "Taking APs",
            "Top 3 Universities": ["Harvard", "MIT", "Stanford"]
          },
          {
            "Name": "Jon",
            "Favorite Subject": "Taking more APs than John",
            "Top 3 Universities": ["MIT", "Caltech", "Princeton"]
          },
          {
            "Name": "Bob",
            "Favorite Subject": "Physical Education",
            "Top 3 Universities": ["I Shou University", "National Yunlin University Science and Technology", "University of Mazandaran"]
          },
          {
            "Name": "BobbY",
            "Favorite Subject": "Intangible Education",
            "Top 3 Universities": ["California State University--Long Beach", "Worcester Polytechnic Institute", "Oakland University"]
          }
          ]
```
This is infodb which is a list of dictionaries that stores the data.

InfoDB Loops
```
def forl():
  for i in range(len(infodb)):
    print_data(i)


def whilel():
  n = 0
  while n < len(infodb):
    print_data(n)
    n += 1
  return


def recursive(n):
  if n >= len(infodb):
    return
  elif n < len(infodb):
    print_data(n)
    return recursive(n + 1)


def recursivel():
  recursive(0)
```
These are the functions called to display infodb's data.


Fibonacci Algorithmn:
```
def fibterm(a, b, n):
  if n == 1:
    return a
  elif n == 2:
    return b
  elif n > 2:
    return fibterm(a, b, n - 1) + fibterm(a, b, n - 2) # recursive to add the previous two terms in the fibonacci sequence
```
This function returns the specified term of the fibonacci sequence with the non-optional options of choosing the two starting numbers.


Classes:
```
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
```
The class Factorial is defined and within it the call function is implemented. We have to do ```fac = Factorial()``` to convert the class to an object. And then when we call the object, the call function within it is called.
