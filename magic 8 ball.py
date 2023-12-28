#Magic 8 Ball

#random number gen
import random
random_number = random.randint(1, 9)

#Name, Question and answer
name = input("What is your name?\n")

question = input("What is your question?\n")

answer = ""

print(name + " asks: " + question)

print("Magic 8-Ball's answer: " + answer)

#Random Answer Gen
if(random_number) == 1:
    answer += "Yes - Defintley"
    print(answer)
elif(random_number) == 2:
    answer += "It is decidely so"
    print(answer)
elif(random_number) == 3:
    answer += "Without a doubt"
    print(answer)
elif(random_number) == 4:
    answer += "Reply hazy, try again"
    print(answer)
elif(random_number) == 5:
    answer += "Ask again later"
    print(answer)
elif(random_number) == 6:
    answer += "Better not tell you now"
    print(answer)
elif(random_number) == 7:
    answer += "My sources say no"
    print(answer)
elif(random_number) == 8:
    answer += "Outlook not so good"
    print(answer)
elif(random_number) == 9:
    answer += "Very doubtful"
    print(answer)