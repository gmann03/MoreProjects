import pyautogui as pg
import time
import webbrowser

points = 0

answer = pg.prompt(
"""
Where would you want to live?

a)A rainforest
b)Alone
c)small house in a small town
d)Large house with a large garden

"""
    )
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4




answer = pg.prompt(
"""
What is your favorite color?

a)grey/black/white
b)pink/red
c)blue/green
d)yellow/orange

"""
    )
if answer == "a":
    points +=2
elif answer == "b":
    points +=3
elif answer == "c":
    points +=1
elif answer == "d":
    points +=4



answer = pg.prompt(
"""
What is your favorite animal?

a)fish
b)Goats
c)Swan
d)Chicken

"""
    )
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4




answer = pg.prompt(
"""
Pick a movie.

a)Mean Girls
b)The Notebook
c)Jaws
d)Anything Disney

"""
    )
if answer == "a":
    points +=2
elif answer == "b":
    points +=3
elif answer == "c":
    points +=1
elif answer == "d":
    points +=4







answer = pg.prompt(
"""
How would you get around?

a)On a goat
b)In daniel's car
c)On a boat
d)On a bike (enviorment friendly!!!!)

"""
    )
if answer == "a":
    points +=2
elif answer == "b":
    points +=3
elif answer == "c":
    points +=1
elif answer == "d":
    points +=4



answer = pg.prompt(
"""
Who is your favorite character??

a)Tonton and Mama
b)Ti Moune
c)Daniel
d)Little Girl

"""
    )
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer == "d":
    points +=4




#END OF SURVEY
pg.alert("You are...")

#Agwe
if points < 11:
    pg.alert("Agwe")
    webbrowser.open("https://d2npu017ljjude.cloudfront.net/images/custom/w1400/94796-0.jpg")
#Papa Ge
if points > 10 and points < 16:
    pg.alert("Papa Ge")
    webbrowser.open("https://admin.broadway.com/images/custom/w1400/94845-0.jpg")
#Erzulie
if points > 15 and points < 21:
    pg.alert("Erzulie")
    webbrowser.open("https://admin.broadway.com/images/custom/w1400/94942-0.jpg")
#Asaka
if points > 20:
    pg.alert("Asaka")
    webbrowser.open("https://d2npu017ljjude.cloudfront.net/images/custom/w1400/94844-0.jpg")

