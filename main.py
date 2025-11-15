import os

total_score = 0

def _ascii_gen(photo):
    os.system("ascii-gen " + photo + " -C")

def result_one():
    result = input("""
    (1) Hand him a mannequin used in crash tests
    (2) Hand him a pasifier
    (3) Hand him a virtual monitor output device""")
    return result

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

prompt_one(total_score)
