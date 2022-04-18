import week0.swap as swap
import week0.christmastree as christmastree
import week0.keypad as keypad
import week0.animation1 as animation1
import week0.animation2 as animation2
import week1.infodb as infodb
import week1.fib as fib
import week2.factorial as fac
import week2.palindrome as pal
import week2.multifactorialimperative as macimp
import week2.multifactorialoop as macoop

##### Main Menu
main_menu = [
]

# Second Menu with functions, separated by Math, Manipulation, and Print
mathsub_menu = [
]

manipulationsub_menu = [
    ["\u001b[32;1mSwap", swap.run]
]

printsub_menu = [
    ["Keypad", keypad.run],
    ["Christmas Tree", christmastree.options]
]

## Third Menu of all the Functions within optins from the second menu
animationsub_menu = [
    ["Animation 1", animation1.run],
    ["Animation 2", animation2.ship]
]

infodbsub_menu = [
    ["InfoDB (For loop)", infodb.forl],
    ["InfoDB (While loop)", infodb.whilel],
    ["InfoDB (Recursive loop)", infodb.recursivel]
]

fibsub_menu = [
    ["Fibonacci Sequence", fib.seq],
    ["Fibonacci Term", fib.term]
]

facsub_menu = [
    ["Factorial Calculator", fac.run],
    ["Factorial Test", fac.test]
]


palsub_menu = [
    ["Palindrome Calculator", pal.run],
    ["Palindrome Test", pal.test]
]


macimpsub_menu = [
    ["Multifactorial Calculator", macimp.run],
    ["Multifactorial Test", macimp.test]
]


macoopsub_menu = [
    ["Multifactorial Calculator", macoop.run],
    ["Multifactorial Test", macoop.test]
]
#####

def mathsubmenu():
    title = "Math" + banner
    mathmenu_list = mathsub_menu.copy()
    mathmenu_list.append(["Fibonacci", fibsubmenu])
    mathmenu_list.append(["Factorial", facsubmenu])
    mathmenu_list.append(["Multifactorial (Imperative)", macimpsubmenu])
    mathmenu_list.append(["Multifactorial (OOP)", macoopsubmenu])
    mathmenu_list.append(["Simple Currency Converter", "week2/simplemoneyconverter.py"])
    mathmenu_list.append(["Complex Currency Converter", "week2/complexmoneyconverter.py"])
    mathmenu_list.append(["Number Guessing Game", "week2/guessinggame.py"])
    mathmenu_list.append(["Calculator", "week2/calculator.py"])
    buildMenu(title, mathmenu_list)


def manipulationsubmenu():
    title = "Manipulation" + banner
    manipulationmenu_list = manipulationsub_menu.copy()
    manipulationmenu_list.append(["\u001b[32;1mPalindrome", palsubmenu])
    buildMenu(title, manipulationmenu_list)


def printsubmenu():
    title = "Print" + banner
    printmenu_list = printsub_menu.copy()
    printmenu_list.append(["Animations", animationsubmenu])
    printmenu_list.append(["InfoDB", infodbsubmenu])
    buildMenu(title, printmenu_list)

##
def animationsubmenu(): # this function builds the aminiation submenu
    title = "Animation" + banner
    buildMenu(title, animationsub_menu)


def infodbsubmenu(): # this function builds the infoDB submenu
    title = "InfoDB" + banner
    buildMenu(title, infodbsub_menu)


def fibsubmenu(): # this function builds the fibonacci submenu
    title = "Fibonacci" + banner
    buildMenu(title, fibsub_menu)


def facsubmenu(): # this function builds the factorial submenu
    title = "Factorial" + banner
    buildMenu(title, facsub_menu)


def palsubmenu(): # this function builds the palindrome submenu
    title = "Palindrome" + banner
    buildMenu(title, palsub_menu)


def macimpsubmenu():
    title = "Multifactorial (Imperative)" + banner
    buildMenu(title, macimpsub_menu)


def macoopsubmenu():
    title = "Multifactorial (OOP)" + banner
    buildMenu(title, macoopsub_menu)
#####

border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


def buildMenu(banner, options): # the function that actually builds all the menus with all the options and functions
    print(banner)
    prompts = {0: ["\u001b[1mExit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("\u001b[37;1mType your choice> ")
    try:
        choice = int(choice)
        if choice == 0: # exits out of this recursive fucntion
            return
        try:
            action = prompts.get(choice)[1]
            action() # runs the function inside the files
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)


def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["\u001b[34mMath", mathsubmenu])
    menu_list.append(["\u001b[32mManipulation", manipulationsubmenu])
    menu_list.append(["\u001b[35mPrint", printsubmenu])
    buildMenu(title, menu_list)


if __name__ == "__main__":
    menu()
