# Guess-Game
###Small-scale guess game from the 'Programming with Python' course

## The user should guess the secret word which is "baguette".

s = "baguette"
\ni = 0
\na = input("Guess the word: ")
\nsentinel = "-9"
\nwhile s != a and i < 4 and a != sentinel:
    \nif a != s:
        \na = (input("Try another time: "))
    \nif i < 4:
        \nprint("You still have ", (3-i), "attempts.")
    \ni = i + 1
\nif a == s:
    \nprint("CONGRATULATIONS!")
\nelif a == sentinel:
    \nprint("See you next time!")
\nelif a != s:
    \nprint("You have exceeded the number of attempts.")
