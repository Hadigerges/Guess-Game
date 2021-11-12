# Guess-Game
Small-scale guess game from the Programming with Python course at ICL

Guess-Game
###Small-scale guess game from the 'Programming with Python' course

The user should guess the secret word which is "baguette".
s = "baguette"
i = 0
a = input("Guess the word: ")
sentinel = "-9"
while s != a and i < 4 and a != sentinel:
  if a != s:
    a = (input("Try another time: "))
  if i < 4:
    print("You still have ", (3-i), "attempts.")
  i = i + 1
  
if a == s:
  print("CONGRATULATIONS!")
elif a == sentinel:
  print("See you next time!")
elif a != s:
  print("You have exceeded the number of attempts.")
