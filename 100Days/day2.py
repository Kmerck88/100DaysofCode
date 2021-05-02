# Given a line of text as input, output the number of characters excluding spaces, periods, or commas.

# Ex: If the input is:

# Listen, Mr. Jones, calm down.


text = input()

charCount = 0

for char in text:
    if char not in [, '.', ',']:
        charCount = charCount + 1

print(charCount)
