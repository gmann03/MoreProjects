import random

words = ["Alexa", "Anna", "Preston", "Michaela", "Rory"]

hint1 = ["two siblings", "three siblings", "three sibling", "one sibling", "one sibling"]

hint2 = ["dancer", "coder", "singer", "hiker", "awesome"]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guesss the secret word")
    print("Type 'hint1', 'hint2', 'length', 'first letter', 'last letter', or 'give up' if you need help")
    guess = input()

   if counter > 4:
       print("You loose!")
       print("The sanswer was" + secretword)
       break

   elif guess == secretword:
        counter +=1
        print("You win!")
        print("It took your " + str(counter) + " guesses")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "length":
        print(len(secretword))

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "last letter":
        print(secretword[-1])

    elif guess == "give up":
        print("The secret word was " + secretword)
        break
    else:
        print("try again.")
        counter += 1
