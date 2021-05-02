# Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending q*s" to the end of the input string.

word = input()
password = ' '

for i in word:
    if i == "i":
        password = password + "!"
    elif i == 'a':
        password  += "@"
    elif i == 'm':
        password += "M"
    elif i == 'B':
        password += "8"
    elif i == 'o':
        password += "@"
    else:
        password += i

password+= "q*s"
print(password)


