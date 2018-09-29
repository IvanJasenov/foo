def fizbuzz(n):
	if (n % 3 == 0):
		print("fiz");
	elif (n % 5 == 0):
		print("buzz");
	elif (n % 5 == 0 and n % 3 == 0):
		print("fizzBuzz");
	else:
		print("nothing");

# range for max int on 64 bit machine
# n <= 2^64 / 2 - 1
n = 11;
fizbuzz(n);
