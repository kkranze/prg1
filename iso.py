number = input ("enter a number")

def isogram(number):
	for int in number:
		if number.count(int) > 1:
			return ("False")
		else:
			return ("True")


answer = isogram(number)
print (answer)
