#complex currency converter

def converter():
  user = input("Press 1 to convert to Canadian, press 2 to convert to yen, press 3 to convert to euros: ")

  if(user == "1"):
    currency = int(input("How many us dollars to Canadian: "))
    convert = currency * 1.25
    return(convert)

  elif(user == "2"):
    currency = int(input("How many us dollars to Yen: "))
    convert = currency * 114.2
    return(convert)

  else:
    currency = int(input("How many us dollars to Euros: "))
    convert = currency * 0.88
    return(convert)

print(converter())




