infodb = [{
            "Name": "John",
            "Favorite Subject": "Taking APs",
            "Top 3 Universities": ["Harvard", "MIT", "Stanford"],
            "favorite letter": 'A'
          },
          {
            "Name": "Jon",
            "Favorite Subject": "Taking more APs than John",
            "Top 3 Universities": ["MIT", "Caltech", "Princeton"],
            "favorite letter": 'B'
          },
          {
            "Name": "Bob",
            "Favorite Subject": "Physical Education",
            "Top 3 Universities": ["I Shou University", "National Yunlin University Science and Technology", "University of Mazandaran"],
            "favorite letter": 'S'
          },
          {
            "Name": "BobbY",
            "Favorite Subject": "Intangible Education",
            "Top 3 Universities": ["California State University--Long Beach", "Worcester Polytechnic Institute", "Oakland University"],
            "favorite letter": 'Z'
          }
          ]


def print_data(n): # used to print a dictionary from infoDB
    print("\t", infodb[n]["Name"])
    print("Favorite Subject: ", end="")
    print(infodb[n]["Favorite Subject"])
    print("Top 3 Universities: ", end="")
    print(", ".join(infodb[n]["Top 3 Universities"]))
    print("favorite letter: ", end="")
    print(infodb[n]["favorite letter"])
    print()


def forl(): # prints all the data from InfoDB with a for loop
  for i in range(len(infodb)):
    print_data(i)


def whilel(): # prints all the data from InfoDB with a while loop
  n = 0
  while n < len(infodb):
    print_data(n)
    n += 1
  return


def recursive(n): # prints all the data from InfoDB through recursive means
  if n >= len(infodb):
    return
  elif n < len(infodb):
    print_data(n)
    return recursive(n + 1)


def recursivel(): # calls the recursive function with a parameter of 0
  recursive(0)
