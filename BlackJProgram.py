import random
import sys 
#I had trouble porting multiple imports in one python program, but little needed to be done here to make these two imports work. Strange.

deck = ['1', '1', '1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10']
#I had a incredibly difficult time attempting to add aces, and all results ended in failure. After around two hours, I decided to remove all code referencing aces from the 0.7 "extra credit" Beta.
house = ['17', '18', '19', '20', '21']
y = int(random.choice(deck))
x = int(random.choice(deck))
z = int(random.choice(deck))
l = int(random.choice(deck))
b = int(random.choice(deck))
house = int(random.choice(house))
print("Black Jack Special Extra credit Beta 0.7.3")
#The X.X.X line actully means something. I have the first number say if the Code is 100% functional with minor error. The second number shows how many features were put in and program-ending bugs patched out, so if I added a new feature like holding, or fixed a bug that resulted in the program failing to run, the number goes up by 1. The final number means a really minor error like a indent error or missing print statement added. This code, while playable, does not function correctly in some areas, so I'm deeming it not a finished build.
print("Face card is: ", y)
f=input ('Draw or hold? d/h:  ')
if f=="h":
  print("You are:")
  print(y + x)
  print("house is:")
  print(house)
  sys.exit("Please restart program")
  #This is Replit's fault. Python should normally give the message and shut down, but Replit believes the program stopped unexpectedly.
elif (y + x) > 21:
  print(y + x)
  print("You have gone past 21, and can no longer play. House wins")
  sys.exit("Please restart program")
  #A bug is resulting in choosing the option "hold" not showing the "over 21" message. Credit to Toshi for finding this bug.
if f=="d":
  print(y + z)
elif (y + z) > 21:
  print(y + z)
  print("You have gone past 21, and can no longer play. House wins")
  sys.exit("Please restart program")
e=input ('Draw or hold? d/h:  ')
if e=="h":
  print(y + x + z)
  print("house is")
  print(house)
  sys.exit("Please restart program")
elif (y + x + z) > 21:
  print(y + x + z)
  print("You have gone past 21, and can no longer play. House wins")
  sys.exit("Please restart program")
if e=="d":
  print(y + l + z)
elif (y + l + z) > 21:
  print(y + l + z)
  print("You have gone past 21, and can no longer play. House wins")
  sys.exit("Please restart program")
w=input ('Draw or hold? Last time you can hold. d/h:  ')
if w=="h":
  print(y + x + z + l)
  print("house is")
  print(house)
  sys.exit("Please restart program")
elif (y + x + z + l) > 21:
  print(y + x + z + l)
  print("You have gone past 21, and can no longer play. House wins")
  sys.exit("Please restart program")
if w=="d":
  print(y + l + z + b + x)
elif (y + l + z + b + x) > 21:
  print(y + l + z + b + x)
  #There is an error here where the "Over 21" feature does not function. Credit to Grant for finding this bug.
  print("You have gone past 21, and can no longer play. House wins")
  sys.exit("Please restart program")
