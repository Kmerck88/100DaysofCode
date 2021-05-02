# Ask the user to enter the current temperature
temp = int(input('What is the current temperature '))

# Compare the current temperature to provide outfit suggestions
if temp >= 80:
	outfit = 'shorts and pack sunglasses'
elif 70 >= temp >= 60:
	outfit = 'light jacket'
else:
	outfit = 'coat in addition to a hat. gloves and scarf'

# Advice
advice = f'Today you should wear a {outfit}'

print(advice)
