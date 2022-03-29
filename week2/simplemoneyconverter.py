#simple currency converter 

dol = int(input("How much money do you have? "))
def usTaiconverter(dollar):
  convert = dollar * 27.59
  return convert

print("Taiwanese Dollars:" + str(usTaiconverter(dol)))
