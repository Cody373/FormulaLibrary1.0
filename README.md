# FormulaLibrary1.0
This code serves as a beginner project to create a formulaic calculator for functions. The Quadratic Equation, Pythagorean Theorem, and Distance Formula are included as of now. I created it with the foresight to add future formulas as well as have those formulas talk to each other when needed. Therefore, there will be many local variables with unique names rather than repeating the use of variable "x" and such.

My code can be broken down into 3 segments: Introduction, defining functions, and execution.

Line 1 of the code starts with an opening message that presents the title of the app and a brief description on what it does. I found I preferred this to be at the top of the code rather than where I actually start executing the code at line 95. To a stranger, this primes the idea of what this application does and how to use it.

Line 8 begins defining my functions for this code. This was a great learning experience. I originally thought I would make a couple functions and have much more code outside of those functions to run them. It turns out that defining the functions took up the most amount of my code. I thought keeping track of larger portions of code would be difficult, but the functions created readable "sections". Once I understood each function, I could easily see how my Starting Function flowed into the rest of the functions without needing to keep track of those functions' deeper code.

Line 8 to Line 51 defines functions for each of the aforementioned formulas: (Quadratic Equation, Pythagorean Theorem, and Distance Formula). They all require numerical inputs from the user. Using anything but a float or integer will result in an error. I imagine I could create a way to request for the variable again, but it's not necessary to practice at this time.

Line 55 to 90 defines StartFunc() which is the function that begins execution of the application. It creates opening dialogue for navigation and requests a string command from the user to execute a specific calculator. 

The StartFunc() also contains an if else statement to execute each function based on the user input. Each if else statement loops back around until the user executes the QUIT command or if the lesser functions get incorrect input as described in Line 10 of this README.

As of 5/28/2022, this code runs as intended. In the future, I will add more formulas for my own utility's sake, learn to round complex numbers (Quadratic Equation) for readability and practical use, and improve the user experience such as finding the outputted answer/values before the StartFunct() runs again without adding more user keystrokes.
