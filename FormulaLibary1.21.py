#This program makes use of a variety of math functions such as the Pythagorean Theorem.

print("*" * 12)
print("""Welcome to the Forumla Libary App
      will serve to be a collection of major simple formulas in which you can plug in the variables.
      """)

# Defining Functions begins here

#Defining Error Messages (Not yet implemented)
def ReqNumbers():
  print("You have entered a wrong value. Please enter a numeric value! ")

def ReqLetters():
  print("You have entered a wrong value. Please enter an alphabetic value! ")

#Defining Equations
def QuadEquation():
  print("""Welcome to the Quadratic Equation Calculator 1.2

  Remember to use numerical values or the program will crash!
    """)
  aq = input("Enter Variable A: ")
  bq = input("Enter Variable B: ")
  cq = input("Enter Variable C: ")

  UXq = ((float(bq)*(-1)) + (float(bq)**2 - 4*float(aq)*float(cq))**(1/2))/(2*float(aq))
  BXq = ((float(bq)*(-1)) - (float(bq)**2 - 4*float(aq)*float(cq))**(1/2))/(2*float(aq))

  print(f""" 
       The upper x value UX is {str(UXq)}
       The bottom x value BX is {str(BXq)}
       """)

def PythagTheorem():
  print("""Welcome to the Pythagorean Theorem Calculator
   
   Remember to use numerical values or the program will crash!
     """)
  ap = input("Enter Variable A: ")
  bp = input("Enter Variable B: ")

  cp2 = float(ap)**2 + float(bp)**2
  cp = cp2**(1/2)

  print(f"""
      C^2 is {str(cp2)}
      C is {str(cp)}
    """)

def DistanceForm():
  print("""
  Welcome to the Distance Formula Calculator")
  d = sqrroot((x1 - x2)^2 + (y1 - y2)^2)
    
  Remember to use numerical values or the program will crash!
       """)

  xd1 = input("Enter x1: ")
  xd2 = input("Enter x2: ")
  yd1 = input("Enter y1: ")
  yd2 = input("Enter y2: ")


  ad = (((float(xd1) - float(xd2))**2) + ((float(yd1) - float(yd2))**2))**(1/2)

  print(f"""
     The distance is {str(ad)}
       """)


#StartFunct() is a critical function that executes the other functions on selection.
def StartFunc():
  print("""
     Please Select a Formula Calculation:
     Q for Quadratic Equation
     P for Pythagorean Theorem
     D for Distance Formula
     QUIT to be lame and end the application
    """)

  sel = input("Enter your selection by typing in the corresponding letter:  ")
  print("   ")

  if sel.upper() == "Q":
    QuadEquation()
    print("*" * 12)
    StartFunc()

  elif sel.upper() == "P":
    PythagTheorem()
    print("*" * 12)
    StartFunc()

  elif sel.upper() == "D":
    DistanceForm()
    print("*" * 12)
    StartFunc()

  elif sel.upper() == "QUIT":
    print("""I suppose you're not cool enough to use math today.
      Now quitting this application
      Enjoy your day!""")
    quit()

  else:
    print("*" * 12)
    print("Please choose another selection")
    StartFunc()

# Defining Functions ends here

# Application's Function Begins Here
StartFunc()





