# Logical Operator = Evaluate multiple conditions.
"""(1) OR = Using multiple conditions joinig with 'OR' operator
one of the condition is True.
Then whole condition is True."""

temp = 25
is_raining = False
if temp > 30 or  temp < 0 :
    print ('I am going to beech for excercise')
else: print('I go to the gym for excersice')

"""(2) AND = Using multiple conditions joinig with 'AND' operator
all the conditions must be True then whole condition is True."""

HR_approved = True
assessment_marks = 70
if assessment_marks > 45 and HR_approved: # If Both conditions must be True
    print('Candidate is passed and ready for GD of interview')
else: print('Candidate is failed and not ready for interview')

"""(3) NOT = Using single condition to negate the condition.
(Not False, Not True)"""
prepared_for_interview  = True
if not prepared_for_interview :
    print('I am going for the Interview')
else: print('I have to prepare for interview before next interview')
