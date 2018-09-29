# n > 0
def fizbuzz(n):
	if (n % 3 == 0):
		print("fiz");
	elif (n % 5 == 0):
		print("buzz");
	elif (n % 5 == 0 and n % 3 == 0):
		print("fizzBuzz");
	else:
		print("nothing in common");
	print("end");
	
# range just for max int on 64 bit machine
# n <= 2^64 / 2 - 1, -1 for the zero(0)
n = 11;
print(fizbuzz(n);)
