print("*" * 12)
print("Welcome to the Calculator App")
print("This will serve to be a collection of major simple formulas in which you can plug in the variables.")
print("   ")

# Defining Functions begins here

def QuadEquation():
  print("Welcome to the Quadratic Equation Calculator 1.0!")
  print("  ")
  aq = input("Enter Variable A: ")
  bq = input("Enter Variable B: ")
  cq = input("Enter Variable C: ")

  UXq = ((float(bq)*(-1)) + (float(bq)**2 - 4*float(aq)*float(cq))**(1/2))/(2*float(aq))
  BXq = ((float(bq)*(-1)) - (float(bq)**2 - 4*float(aq)*float(cq))**(1/2))/(2*float(aq))

  print("   ")
  print("The upper x value UX is " + str(UXq))
  print("The bottom x value BX is " + str(BXq))
  print("   ")

def PythagTheorem():
  print("Welcome to the Pythagorean Theorem Calculator")
  print("   ")
  ap = input("Enter Variable A")
  bp = input("Enter Variable B")

  cp2 = float(ap)**2 + float(bp)**2
  cp = cp2**(1/2)

  print("  ")
  print("C^2 is " + str(cp2))
  print("C is " + str(cp))
  print("  ")

def DistanceForm():
  print("  ")
  print("Welcome to the Distance Formula Calculator")
  print("d = sqrroot((x1 - x2)^2 + (y1 - y2)^2) ")
  print("   ")

  xd1 = input("Enter x1: ")
  xd2 = input("Enter x2: ")
  yd1 = input("Enter y1: ")
  yd2 = input("Enter y2: ")


  ad = (((float(xd1) - float(xd2))**2) + ((float(yd1) - float(yd2))**2))**(1/2)

  print("The distance is " + str(ad))


#StartFunct() is a critical function that executes the other functions on selection.
def StartFunc():
  print("  ")
  print("Please Select a Formula Calculation: ")
  print("Q for Quadratic Equation")
  print("P for Pythagorean Theorem")
  print("D for Distance Formula")
  print("QUIT to be lame and end the application")
  print("   ")

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
    print("I suppose you're not cool enough to use math today.")
    print("Now quitting this application")
    print("Enjoy your day!")
    quit()

  else:
    print("*" * 12)
    print("Please choose another selection")
    StartFunc()

# Defining Functions ends here

StartFunc() # Application's Function Begins Here




