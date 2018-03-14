import webbrowser
import pyautogui as pg

videos = ["https://www.youtube.com/watch?v=_EvMYEfF_hQ", "https://www.youtube.com/watch?v=y6oryHiBm4E", "https://www.youtube.com/watch?v=fYoXeBtiWsk"]

shows = ["http://onceonthisisland.com/", "https://dearevanhansen.com/", "https://waitressthemusical.com/index.php"]

below = ["https://www.youtube.com/watch?v=uDDad5MrWsc", "https://www.youtube.com/watch?v=ruDp_cFRhkE", "https://www.youtube.com/watch?v=rujaYS0s85E", "https://www.youtube.com/watch?v=OFz1xw1MRYY", "https://www.youtube.com/watch?v=fmA7JJ-CkNo"]

answer = pg.prompt(
"""
What do you want to do?
a)videos
b)shows
c)54 below

"""
    )
if answer == "a":
    for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in shows:
        webbrowser.open(i)

elif answer == "c":
    for i in below:
        webbrowser.open(i)
