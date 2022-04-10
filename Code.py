d=input("Is it a weekday? Reply with y/n  ")
v=input("Is today a Vacation day? Reply with y/n  ")
#We are using user inputs to find out if you have to go to work
if d=="y": 
   print("Sleep in")
elif v=="y": 
   print("sleep in")
else: 
   print ("Wake up")

d=input("Is a monkey talking? Reply with y/n:  ")
if d=="y": 
   v=input("Is the other monkey talking as well? Reply with y/n:  ")  
#This is a "stacked" input as it is on top of another input. Similar to Jenga, this was hard to make and resulted in bugs the majority of the time.
if d=="n": 
   print("Uh oh") 
if v=="y": 
   print ("Uh oh")
if v=="n": 
   print ("Your good")

e=input("Is N smaller than 21? Reply with y/n:  ")
if e=="y": 
  print(abs(21 - N))
elif e == "n": 
  print(2(21 - N))

x = int(input("insert a number bewteen 0-100  "))
#This problem takes an actual integer and recognizes it to give an answer
if x < 21: 
   print(abs(21 - x))
elif x > 21: 
   print(2 * abs(21 - x))
else: 
   print("That's not a number!") 

d=input("Is the parrot talking? Reply with y/n  ")
if d=="y": 
   v=input("Is it after 7:00 AM AND before 8:00 PM? Reply with y/n  ")  
#Here is another input on top of an input
if d=="n": 
   print("Uh oh") 
if v=="y": 
   print ("Your good")
else: 
   print ("Uh oh")

d=input("Does A or B equal 10? Reply with y/n:  ")
if d=="y": 
   print ("The integers work")
elif d=="n": 
#This is an else if statement to give the user more choice and flexability without making the code to complex
   v=input("Does A and B equal 10 (Reply with y/n  ")
if v=="y": 
   print ("The integers work")
else: 
   print ("The integers don't work")

try:
  x = float(input("Give the total for the person's meal with no $ or cent symbol included. You can include change and cents: "))
except ValueError:
  print('An error occured. You can only type a number in this area with no letters or hashes.')
else:
  print(x*.15 + x*.05 + x)

An error occured. You can only type a number in this area with no letters or hashes.
