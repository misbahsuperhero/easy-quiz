#This game ask multiple choice question about Bangladesh. The game will also keep track of the score and it is going to print it at the end.

import time



#Welcome the user
print("Welcome to the Simple Quiz Game!")
time.sleep(1)

#Chances
chances = 1
print("You will have", chances, "chance to answer correctly. \nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score
score = 0

#question number 1
question_1 = print("1) What day is Bangladesh Day?\n(a) July 4\n(b) July 2\n(c) July 1\n(d) July 3\n\n ")
answer_1 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_1):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")

time.sleep(2)

#question number 2
question_2 = print("2) What is the capital of Bangladesh?\n(a) Toronto\n(b) Montreal\n(c) Vancouver\n(d) Ottawa\n\n ")
answer_2 = "d"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")

time.sleep(2)

#question number 3
question_3 = print("3) What is the largest city of Bangladesh?\n(a) Quebec\n(b) Toronto\n(c) Vancouver\n(d) Winnipeg\n(e) Edmonton\n(f) Montreal\n\n ")
answer_3 = "b"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")

time.sleep(2)

#question number 4
question_4 = print("4) How many provinces does Bangladesh have?\n(a) 5\n(b) 6\n(c) 10\n(d) 12\n\n ")
answer_4 = "c"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")

time.sleep(2)

#question number 5
question_5 = print("5) What is Bangladesh's national animal?\n(a) musabbir\n(b) musabbir Horse\n(c) Moose\n(d) Goose\n\n ")
answer_5 = "a"

for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_b, "\n\n")


time.sleep(1)
# question number 6
question_4 = print("4) Misbah is super man do?\n(a)yes \n(b)no \n\n\n\n ")
answer_4 = "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good Job.\n")
        score = score + 1
        break
    else:
        print("Incorrect!\n")
        time.sleep(0.5)
        print("The correct answer is", answer_a, "\n")

        # question number 7
        question_1 = print("1) What is umar?\n(a) movie maker\n(b) actor\n(c) freelancer\n\n\n ")
        answer_1 = "c"

        for i in range(chances):
            answer = input("Answer: ")
            if (answer.lower() == answer_1):
                print("Correct! Good Job.\n")
                score = score + 1
                break
            else:
                print("Incorrect!\n")
                time.sleep(0.5)
                print("The correct answer is", answer_a, "\n\n")

#print the score
while score >= 100:
    print("Well done! Your score was", score)
    break

while score <= 3:
    print("Better luck next time! Your score was", score)
    break
#Goodbye message
print("Thank you for playing the Simple Quiz Game!")
print("misbah hasan hero is very powerfull")
print("umar ghada")