import time
import random

operators = ["+", "-", "*"]
max_num = 15
min_num = 3
total_prob = int(input("How many problems would you like to solve: "))

def easy_questions():
    left = random.randint(min_num, max_num)
    right = random.randint(min_num, max_num)
    operator = random.choice(operators)

    ques = str(left) + " " + operator + " " + str(right)
    ans = eval(ques)

    return ques, ans

def med_questions():
    left = random.randint(min_num, max_num)
    centre = random.randint(min_num, max_num)
    right = random.randint(min_num, max_num)
    operator1 = random.choice(operators)
    operator2 = random.choice(operators)

    ques = str(left) + " " + operator1 + " " + str(centre) + " " + operator2 + " " + str(right)
    ans = eval(ques)

    return ques, ans

def hard_questions():
    left = random.randint(min_num, max_num)
    centre1 = random.randint(min_num, max_num)
    centre2 = random.randint(min_num, max_num)
    right = random.randint(min_num, max_num)
    operator1 = random.choice(operators)
    operator2 = random.choice(operators)
    operator3 = random.choice(operators)

    ques = str(left) + " " + operator1 + " " + str(centre1) + " " + operator2 + " " + str(centre2) + " " + operator3 + " " + str(right)
    ans = eval(ques)

    return ques, ans

level = int(input("-----Press-----\n'1' for easy questions\n'2' for moderate questions\n'3' for difficult questions: "))

print("Press any key to start!")
print("-"*50)

wrong = 0
start = time.time()

if level == 1:
    for i in range(total_prob):
        ques, ans = easy_questions()
        while True:
            guess = input("Question " + str(i + 1) + ": " + ques + " = ")
            if guess == str(ans):
                break
            wrong += 1

elif level == 2:
    for i in range(total_prob):
        ques, ans = med_questions()
        while True:
            guess = input("Question " + str(i + 1) + ": " + ques + " = ")
            if guess == str(ans):
                break
            wrong += 1

elif level == 3:
    for i in range(total_prob):
        ques, ans = hard_questions()
        while True:
            guess = input("Question " + str(i + 1) + ": " + ques + " = ")
            if guess == str(ans):
                break
            wrong += 1

else:
    print("Invalid input!")

end = time.time()
final_time = end - start    
print("No of wrong answer given: " + str(wrong))
print("You fineshed the quiz in:", round(final_time, 2), "seconds")

print("Nice work!")

print("-"*50)