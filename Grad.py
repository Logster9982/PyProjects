print("Senior Role-Placement Program 12.1 by Logan Altomonte. Thank you for using this program")
#I am attempting to make the program feel more "Commercial" and user friendly.
d=input("Before we begin, is there any non-seniors in this program? Please reply with y for yes and n for no:  ")
#This is far more convenient to the user than to say if a person is a senior every time a GPA is asked.
if d=="y":
   print("Non-seniors cannot be counted in this program. Please remove seniors from your calculations and restart the program")
if d=="n":
  z = int(input("Input how many students you want to have placed: "))
  #I spent a solid 20 minutes finding out where to put the while statement because it always gave me indent errors or syntax errors. In the end, I had to re-indent the entire program for the program to function.
  while z >= 1:
    #What happens here is "Z" is how long you want the program to run for, and this program will run until Z is less than 1.
    x = float(input("Please give the GPA of a student: "))
    if x < 3:
      print("This student needs to take the final exam.")
      z=(z - 1)
      #These "Z" statements will minus by 1 and reassign Z as the solution, allowing me to have a certain amount of students be counted.
    elif 3 <= x < 3.5:
      print("This student passed and does not need to take the final exam.")
      z=(z - 1)
    elif 3.5 <= x < 3.9:
      print("This student made the honor roll!")
      z=(z - 1)
    elif 3.9 <= x <= 4:
      print("This student made the principles list!")
      z=(z - 1)
    else:
      break
      #In the event the program encounters an error, I have set the program to kill itself. (You can't kill a non-living thing but it sounds dramatic and I have seen it be used to stop programs so I found it fitting to be used here.)
