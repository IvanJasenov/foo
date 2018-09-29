def fizbuzz(n):
	if (n % 3 == 0):
		print("fiz");
	elif (n % 5 == 0):
		print("buzz");
	elif (n % 5 == 0 and n % 3 == 0):
		print("fizzBuzz");
	else:
		print("nothing");

n = 11;
fizbuzz(n);
