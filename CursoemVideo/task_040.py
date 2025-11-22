grade_1 = float(input('Enter your first grade: ').strip())
grade_2 = float(input('Enter your second grade: ').strip())

average = (grade_1 + grade_2) / 2

if average < 50:
    print('Sorry, you did not pass.')
elif  50 <= average <= 69:
    print('Sorry, you need to do the recovery test.')
else:
    print('Excellent! You passed!')



