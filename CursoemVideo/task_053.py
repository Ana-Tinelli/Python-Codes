phrase = str(input('Enter the phrase to check if it is palindrome: ').strip().replace(' ', '')).lower()

if phrase == phrase[ : :-1]:
        print('The phrase is palindrome.')
else:
    print('The phrase is not palindrome.')








