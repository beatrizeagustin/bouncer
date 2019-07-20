#ask for age
#age = input("How old are you: ") # dont try to have int here, it will mess up the error/ else
# always change int to str
#if age: # for errors .. checking for an empty string can be "if age" to be truthy
#	age = int(age)
#	if age >= 18 and age <= 21:
		#18-21 wristband
#		print("You can enter but need a wristband")
#	elif age >= 21:
		#21+ drink, normal entry
#		print("You can come in")
#	else:
		#too young, sorry
#		print("Sorry, you can't come in")
#else:
#	print("You didnt enter anything")

# refactored

age = input("How old are you: ") # dont try to have int here, it will mess up the error/ else
# always change int to str
if age: # for errors .. checking for an empty string can be "if age" to be truthy
	age = int(age)
	if age >= 21:
		print("You can enter")
	elif age >= 18:
		print("You can come in but need a wristband")
	else:
		#too young, sorry
		print("Sorry, you can't come in")
else:
	print("You didnt enter anything")







