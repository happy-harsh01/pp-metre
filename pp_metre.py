import random
import time


def pp_check(size_of_pp):
    if size_of_pp == 0:
        return "Your one is microscopic, you can't even f.... , die without Lana!"
    elif size_of_pp > 5:
        return "You have a small pp ( no effect )"
    elif size_of_pp == 5:
        return "You have a small pp , you can try a little bit of that...."
    elif size_of_pp > 10:
        return "You have a BIG pp : ) , you can ... Enjoy!"
    elif size_of_pp == 10:
        return "You have a Massive Big one, that will kill them, don't even f...."

def pp_size_state(size_of_pp):
    if size_of_pp == 0:
        return "microscopic"
    elif size_of_pp >= 5:
        return "small pp"
    elif size_of_pp > 10:
        return "BIG pp"
    elif size_of_pp == 10:
        return "Giant pp"

def matchup(pp_size, ass_size):
    if pp_size == 0 and ass_size == "microscopic":
        return True
    elif pp_size <= 5 and ass_size == "small":
        return True
    elif pp_size < 10 and ass_size == "":
        return True
    elif pp_size == 10 and ass_size == "":
        return True
    else: return False

def problem(size):
    if size == 0:
        return "Yes"
    elif size > 5:
        return "Yes"
    elif size == 5:
        return "No"
    elif size > 10:
        return "No"
    elif size == 10:
        return "Yes"
    else:
        return "No"


def solution(size):
    if size == 0 or size == 10:
        return "pp Treatment"
    else:
        return "pp Surgery"


surgery = ['Your pp is being replaced ...', f"Your pp is replaced to a {random.choice(['Dog', 'Pig'])}'s one"]
pp_size_check = False
ass_size_check = False
size = ''
pp_size = random.randint(0, 11)
print("=====Welcome to the pp health care=====\nType help for help")
while True:
    a = input("What do you wanna do ?\n")
    a.lower()
    if a == "help":
        print('''========HELP MENU========
    *Type 1 for checking pp length.
    *Type 2 for pp surgery.
    *Type 3 for pp treatment
    *Type 4 for ass size
    *Type 5 to fuck
    *Type 6 to Exit''')
    elif a == '1':
        print("Checking your pp")
        time.sleep(2)
        print("Gaining pp information")
        time.sleep(1)
        print("===PP REPORT===")
        if problem(pp_size) == "No":
            print(f'''PP SIZE : {pp_size}\n
F...STATUS : {pp_check(pp_size)}
PROBLEM : {problem(pp_size)}''')
        else:
            print(f'''PP SIZE : {pp_size}\n
F...STATUS : {pp_check(pp_size)}
PROBLEM : {pp_problem(pp_size)}
SOLUTION : {solution(pp_size)}''')
        pp_size_check = True
    elif a == '2':
        if pp_size_check:
            if problem(pp_size) == "Yes":
                if pp_size == 0 or pp_size == 10:
                    print('You need to do a pp treatment.')
                print("Checking your pp")
                time.sleep(1)
                print("Validating your surgery...")
                time.sleep(.5)
                print("Cutting your pp")
                time.sleep(.5)
                print("pp removed")
                time.sleep(1)
                print(random.choice(surgery))
                time.sleep(2)
                print("pp replaced")
                print("pp surgery done successfully")

            else:
                print("You don't have a problem, you have a good pp!")
        else:
            print("Yo haven't checked for your pp size do that first")
    elif a == '3':
        print("fuck")
    elif a == "4":
        if pp_size_check:
            if pp_size == 0:
                print("You have a microscopic pp...")
                size = "microscopic"
            elif pp_size <= 5:
                print("You have a small pp...")
                size = "small"
            elif pp_size < 10:
                print("You have a Big pp...")
                size = "Big"
            else:
                print("You have a Giant pp...")
                size = "Giant hole"
            print("hmm")
            time.sleep(2)
            print(f"{size} ass will be best for you!")
            time.sleep(2)
            ass_size_check = True
        else:
            print("You haven't checked your pp size go and check that first.")
    elif a == "5":
        if pp_size_check and ass_size_check:
            if problem(pp_size) == "Yes":
                print("You have a problem , you can't even fuck lmao.")
            else:
                print("You were trying to fuck...")
                time.sleep(2)
                print(f"A {pp_size_state(pp_size)} proceeds...")
                print(f"The pp proceeds towards a {size} ass.")
                time.sleep(1)
                print("And they...they....")
                time.sleep(2)
        else:
            print("Go and check out pp and ass size first.")
    elif a == '6':
        print('Exiting')
        time.sleep(.5)
        print("***")
        time.sleep(1)
        print("******")
        time.sleep(.5)
        print("You have Quited\nThanks for using pp health care")
        time.sleep(2)
        break
    else:
        print("Please Enter a valid option, you Bitch")
