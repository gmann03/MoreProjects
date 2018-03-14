while True:
    print("What's your favorite musical?")
    musical=input().title()

    if musical == "Dear Evan Hansen":
        print("yes! Great choice! Nice job! I approve!")
    elif musical == "Hamilton":
        print("awesome. wow")
    elif musical == "Great Comet":
        print("snazzy")
    elif musical == "Waitress":
        print("Ogie says YES!")
    else:
        print("Sounds good. maybe I'll look into it")


    print("What's your favorite tv show?")
    tvshow =input().title()

    if tvshow == "Riverdale":
        print("Who's your favorite character?")
        character=input().title()

        if character == "Jughead":
            print("Nice!")
        elif character == "Archie":
            print("He is so great!")
        elif character == "Betty":
            print("Ponytail for life!")
        elif character == "Veronica":
            print("Yes! Pearls are amazing!")
        elif character == "Cheryl":
            print("Red Queen!")
        else:
            print("Pretty cool!")

    elif tvshow == "The Office":
        print("never watched that, but it sounds good!")
    elif tvshow == "Girl Meets World":
        print("such a good show!")
    else:
        print("nice choice!")


    print("What's your favorite color?")
    color=input().title()

    if color == "Blue":
        print("Me too!")
    elif color == "Purple":
        print("nice!")
    elif color == "Green":
        print("wow!")
    else:
        print("that's such a pretty color")

    print("What's your favorite animal?")
    animal=input().title()

    if animal == "Dog":
        print("so cute")
    elif animal == "Cat":
        print("wow")
    elif animal == "Unicorn":
        print("magical!")
    else:
        print("adorable!")

    languagesubject = ["Spanish", "French", "Chinese", "Mandrin", "Latin", "Language"]

    print("What's your favorite subject?")
    subject=input().title()

    if subject == "Math":
        print("a^2 + b^2 = c^2")
    elif subject == "English":
        print("If music be the food of love, PLAY ON!")
    elif subject == "History":
        print("What's your favorite time period/unit of History")
        history=input().title()
        if history == "American History":
            print("That's mine too!")
        else:
            print("So Fascinating!")
    elif subject in languagesubject:
        print("Hola! Bonjour!")
    elif subject == "Science":
        print("So interesting!")

    print("Thanks for taking this survey! Want to play again? (YES/NO)")
    again=input().title()

    if again == "Yes":
        print("Okay! Let's go!")
    else:
        print("Bye Now.")
        break

    

