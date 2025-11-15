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
    while panel_score > 0:
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
    while panel_score > 0:
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

#lima
def _result_three_1():
    result = input("""
    (1) Mention limes
    (2) Mention files
    """)
    return result

#tomo
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
    while panel_score > 0:
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

#combine            
def _result_four_1():
    result = input("""
    (1) Mention bringing things together
    (2) Mention the card game "Casino"
    (3) Mention Half Life
    (4) Mention farming
    """)
    return result

#bank
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
    panel_score = 2
    correct = random.randint(1,2)
    if correct == 1:
        print("Make sure to store the combine's output in our bank")
    elif correct == 2:
        print("Why don't you combine those pennies at the bank, they're not made anymore")
    result = result_four_full()
    while panel_score > 0:
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
        else:
            print("[System] error, valid inputs are 1-4 on the 1st prompt, 1-5 on the 2nd")
            result = result_four_full()
    print("You seem drunk...")
    return panel_score + total_score

#capital
def _result_five_1():
    result = input("""
    (1) Mention goods made to make other goods
    (2) Mention a means to aquire goods
    (3) Mention where the authority of a government is located
    (4) Mention the most important city in a certain field
    """)
    return result

#console
def _result_five_2():
    result = input("""
    (1) Mention a cabinet integrated with home entertainment equipment
    (2) Mention a computer monitor and keyboard'
    (3) Mention a video game device
    (4) Mention a storage tray or container mounted between the seats in a automobile 
    """)
    return result

def result_five_full():
    return [_result_five_1(), _result_five_2()]

def prompt_five(total_score):
    panel_score = random.randint(1,2)
    correct_1 = random.randint(1,2) #capital
    correct_2 = random.randint(1,2) #console
    if correct_1 == 1:
        person = "senator"
    elif correct_1 == 2:
        person = "intern"
    print("The " + person + " was trying to figure out how to use the console at the capital")
    result = result_five_full()
    while panel_score > 0:
        if correct_1 == 1:
            if correct_2 == 1:
                if result[0] == "3" and result[1] == "2":
                    print("correct")
                    return panel_score + total_score + 1 
                else:
                    print("incorrect")
                    panel_score -= 1
                    total_score -= 1
                    result = result_five_full()
            elif correct_2 == 2:
                if result[0] == "3" and result[1] == "3":
                    print("correct")
                    return panel_score + total_score + 1 
                else:
                    print("incorrect")
                    panel_score -= 1
                    total_score -= 1
                    result = result_five_full()
        elif correct_1 == 2:
            if correct_2 == 1:
                if result[0] == "4" and result[1] == "2":
                    print("correct")
                    return panel_score + total_score + 1 
                else:
                    print("incorrect")
                    panel_score -= 1
                    total_score -= 1
                    result = result_five_full()
            elif correct_2 == 2:
                if result[0] == "4" and result[1] == "3":
                    print("correct")
                    return panel_score + total_score + 1 
                else:
                    print("incorrect")
                    panel_score -= 1
                    total_score -= 1
                    result = result_five_full()
    print("out of score")
    return panel_score + total_score

#club
def result_six(order=None):
    if order == 1:
        result = input("""
        (1) Mention a heavy kind of stick
        (2) Mention an accociation of memebers
        (3) Mention an establishment that provides staged entertainment
        (4) Mention playing cards
        (5) Mention sandwitches 
        """) 
    elif order == 2:
        result = input("""
        (1) Mention playing cards
        (2) Mention an establishment that provides staged entertainment
        (3) Mention an accociation of memebers
        (4) Mention a heavy kind of stick
        (5) Mention sandwitches 
        """) 
    elif order == 3:
        result = input("""
        (1) Mention playing cards
        (2) Mention the propeller of an aeroplane
        (3) Mention sandwitches
        (4) Mention an accociation of memebers
        (5) Mention a heavy kind of stick
        """) 
    elif order == 4:
        result = input("""
        (1) Mention sandwitches
        (2) Mention an accociation of memebers
        (3) Mention an establishment that provides staged entertainment
        (4) Mention the propeller of an aeroplane
        (5) Mention a heavy kind of stick
        """) 
    return result

def prompt_six(total_score):
    panel_score = total_score % 3 + 1
    correct = random.randint((total_score % 2) + 1, 3)
    answers= [[1, "4", 1],[1, "1", 2],[1, "1", 3],[2, "5", 1],[2, "5", 2],[2, "3", 3],[2, "1", 4],[3, "3", 1],[3, "2", 2], [3, "3", 4]]
    if correct == 1:
        print("There's a club carved into this")
        order = random.randint(1,3)
        result = result_six(order)
    elif correct == 2:
        print("I'll take a club please")
        order = random.randint(1,4)
        result = result_six(order)
    elif correct == 3:
        print("I'll meet you at the club")
        order = random.randint(random.randint(1,2), 4)
        if order == 3:
            order = random.randint(1,2)
        result = result_six(order)
    combo = [correct, result, order]
    while panel_score > 0:
        if combo in answers:
            print("correct")
            return panel_score + total_score + 1
        else:
            print("incorrect")
            panel_score -= 1
            total_score -= 1
            result = result_six_full(order)
            combo = [correct, result, order]
    print("out of score")
    return panel_score + total_score

#date
def _result_seven_1(order):
     if order == 1:
        result = input("""
        (1) Mention going out with one you're engaged/married to
        (2) Mention a fruit
        """)
     elif order == 2:
        result = input("""
        (1) Mention a fruit
        (2) Mention going out with one you're engaged/married to
        """)
     return result

#effect
def _result_seven_2(order):
    if order == 1:
        result = input("""
        (1) Mention special illusions in done by techinal means
        (2) Mention an alteration done to sound
        (3) Mention a scientific phenomenon
        (4) Mention the outcome of a cause
        """)
    elif order == 2:
        result = input("""
        (1) Mention the outcome of a cause
        (2) Mention a scientific phenomenon
        (3) Mention an alteration done to sound
        (4) Mention special illusions in done by techinal means
        """)
    return result

def result_seven_full(order_1,order_2):
    return [_result_seven_1(order_1), _result_seven_2(order_2)]

def prompt_seven(total_score):
    panel_score = 2
    correct = random.randint(1,(total_score % 2) + 1)
    answers = [[1, ["2","4"],1,1],[1,["2","1"],1,2],[1,["1","1"],2,2],[1,["1","4"],2,1],[2,["1","1"],1,1],[2,["1","4"],1,2],[2,["2","4"],2,2],[2,["2","1"],2,1]]
    if correct == 1:
        print("The date had a weird effect on him")
    elif correct == 2:
        print("The date went really well till a certain effect triggered a seizere")
    order_1 = random.randint(1,2)
    order_2 = random.randint(1,2)
    result = result_seven_full(order_1,order_2)
    combo = [correct, result, order_1, order_2]
    while panel_score > 0:
        if combo in answers:
            print("correct")
            return panel_score + total_score + 1
        else:
            print("incorrect")
            panel_score -= 1
            total_score -= 1
            order_1 = random.randint(1,2)
            order_2 = random.randint(1,2)
            result = result_seven_full(order_1,order_2)
            combo = [correct, result, order_1, order_2]
    print("out of score")
    return panel_score + total_score
    
                                                        
score_one = prompt_one(total_score)
score_two = prompt_two(score_one)
score_three = prompt_three(score_two)
score_four = prompt_four(score_three)
score_five = prompt_five(score_four)
score_six = prompt_six(score_five)
score = prompt_seven(score_six)

print("Prompt One: " + str(score_one) + "\n")
print("Prompt Two: " + str(score_two) + "\n")
print("Prompt Three: " + str(score_three) + "\n")
print("Prompt Four: " + str(score_four) + "\n")
print("Prompt Five: " + str(score_five) + "\n")
print("Prompt Six: " + str(score_six) + "\n")
print("Total Score: " + str(score))
