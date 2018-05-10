
for counter in range(0,101):
	if counter % 3 == 0 and counter % 5 == 0:
		print "FizzBuzz"
	elif counter % 5 == 0:
		print "Buzz"
	elif counter % 3 == 0:
		print "Fizz"
	else:
		print counter
