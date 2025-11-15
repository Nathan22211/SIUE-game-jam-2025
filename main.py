import os, random

total_score = 0

def _ascii_gen(photo):
    os.system("ascii-gen " + photo + " -C")

def result_one():
    result = input("""
    (1) Hand him a mannequin used in crash tests
    (2) Hand him a pasifier
    (3) Hand him a virtual monitor output device""")
    return result

#dummy
def prompt_one(total_score):
    panel_score = 1
    print("She's crying, hand me the dummy")
    result = result_one()
    while panel_score != 0:
        if result == "1":
            print("Where'd you have the crash test dummy the entire time!?")
            panel_score -= 1
            total_score -= 1
            result = result_one()
        elif result == "2":
            print("Thank you, hopefully the dog doesn't get her mouth on it.")
            return panel_score
        elif result == "3":
            print("I don't need a fake monitor right now.")
            panel_score -= 1
            total_score -= 1
            result = result_one()
        else:
            print("[System] error, valid inputs are 1-3")
            result = result_one()
    print("You're no help... I'll get it myself. Maybe the dog has it")
    return total_score + panel_score

#battery
def result_two():
    result = input("""
    (1) Mention Physical Voilence
    (2) Mention something that stores an eletrical charge long term
    (3) Mention military weapons
    (4) Mention female chickens
    (5) Mention the drum section of a marching band
    (6) Mention an apparatus for serving meals
    (7) Mention baseball
    """)
    return result

def prompt_two(total_score):
    panel_score = random.randint(1, 3)
    correct = random.randint(1, 2)
    if correct == 1:
        print("So Ma,am, you say that battery was involved?")
    elif correct == 2:
        print("So Ma,am, you say that he snuck an entire battery of these away?")
    result = result_two()
    while panel_score != 0:
        if result == "1":
            if correct == 1:
                print("Yes, he attacked me on 5th Street")
                return total_score + panel_score + 1
            elif correct == 2:
                print("I wasn't attacked...")
                panel_score -= 1
                total_score -= 1
                result = result_two()
        elif result == "2":
            print("what does batteries have to do with this..!")
            panel_score -= 1
            total_score -= 1
            result = result_two()
        elif result == "3":
            if correct == 1:
                print("what does this have to do with anything related to the military")
                panel_score -= 1
                total_score -= 1
                result = result_two()
            elif correct == 2:
                print("Yes, grabbed them and took off in a Ospray")
                return total_score + panel_score + 1
        elif result == "4":
            print("What does this have to do with chickens?")
            panel_score -= 1
            total_score -= 1
            result = result_two()
        elif result == "5":
            print("And a marching band is relevent... Why?")
            panel_score -= 1
            total_score -= 1
            result = result_two()
        elif result == "6":
            print("I'm not a waiter.")
            panel_score -= 1
            total_score -= 1
            result = result_two()
        elif result == "7":
            print("I don't think they were into baseball")
            panel_score -= 1
            total_score -= 1
            result = result_two()
        else:
            print("[System] error, valid inputs are 1-7")
            result = result_one()
    print("Ugh... I'll find someone more compitent")
    return total_score + panel_score

def _result_three_1():
    result = input("""
    (1) Mention limes
    (2) Mention files
    """)
    return result

def _result_three_2():
    result = input("""
    (1) Mention A volume in a book
    (2) Say I took something  
    """)
    return result

def result_three_full():
    return [_result_three_1(), _result_three_2()]

def prompt_three(total_score):
    panel_score = 1
    print("(Partly Translated From Spanish) \" Ok boss, I found the *lima* in the *tomo* you mentioned.\"")
    result = result_three_full()
    while panel_score != 0:
        if result[0] == "1" and result[1] == "1":
            print("You found a lime in a book?")
            panel_score -= 1
            total_score -= 1
            result = result_three_full()
        elif result[0] == "1" and result[1] == "2":
            print("You found lime in a take? Take of what?")
            panel_score -= 1
            total_score -= 1
            result = result_three_full()
        elif result[0] == "2" and result[1] == "1":
            print("Good, now get out of there!")
            return panel_score + total_score + 1
        elif result[0] == "2" and result[1] == "2":
            print("you found the file... In a take...")
            panel_score -= 1
            total_score -= 1
            result = result_three_full()
        else:
            print("[System] error, valid inputs are 1-2 on both")
            result = result_three_full()
    print("You suddenly hear a scuffle as the comms cut off")
    return panel_score + total_score
            
def _result_four_1():
    result = input("""
    (1) Mention bringing things together
    (2) Mention the card game "Casino"
    (3) Mention Half Life
    (4) Mention farming
    """)
    return result
def _result_four_2():
    result = input("""
    (1) Mention a Financial Insitution
    (2) Mention card games
    (3) Mention something used to store currency
    (4) Mention Dominos 
    (5) Mention somewhere safe to store goods
    """)
    return result

def result_four_full():
    return [_result_four_1(), _result_four_2()]

def prompt_four(total_score):
    panel_score = 1
    correct = random.randint(1,2)
    if correct == 1:
        print("Make sure to store the combine's output in our bank")
    elif correct == 2:
        print("Why don't you combine those pennies at the bank, they're not made anymore")
    result = result_four_full()
    while panel_score != 0:
        if result[0] == "1":
            if result[1] == "1" and correct == 2:
                print("I'll be right to it honey")
                return panel_score + total_score + 1
            elif result[1] == "2":
                print("What use are they at a casino?")
                panel_score -= 1
                total_score -= 1
                result = result_four_full()
            elif result[1] == "3":
                print("Can't combine them in that...")
                panel_score -= 1
                total_score -= 1
                result = result_four_full()
            elif result[1] == "4":
                print("What do Dominos have to do with it?")
                panel_score -= 1
                total_score -= 1
                result = result_four_full()
            elif result[1] == "5":
                print("Don't put them in with the food...")
                panel_score -= 1
                total_score -= 1
                result = result_four_full()
        elif result[0] == "2":
            print("What are pips..?")
            panel_score -= 1
            total_score -= 1
            result = result_four_full()
        elif result[0] == "3":
            print("This is not Black Mesa")
            panel_score -= 1
            total_score -= 1
            result = result_four_full()
        elif result[0] == "4":
            if result[1] == "5" and correct == 1:
                print("Right, I do have some left.")
                return panel_score + total_score + 1
            else:
                print("why the harvester...")
                panel_score -= 1
                total_score -= 1
                result = result_four_full()
    print("You seem drunk...")
    return panel_score + total_score
    
    
            
score_one = prompt_one(total_score)
score_two = prompt_two(score_one)
score_three = prompt_three(score_two)
score = prompt_four(score_three)

print("Total Score: " + str(score))
