"""Grade Calculation:
Ask the user for a student's score.
Assign a letter grade based on the score (e.g., A, B, C, D, F).
Print the letter grade."""
Name = input("Emter your name")
E_Roll_No = int(input("Enter your Roll_No."))
marks = float(input("Enter the marks of student  "))

if marks >= 80: print(f"Student got A grade in the exams")
elif marks >= 70: print(f"Student got B grade in the exams")
elif marks >= 60: print(f"Student got C grade in the exams")
elif marks >= 45: print(f"Student got D grade in the exams")
else: print(f"Student failed in the exams")
