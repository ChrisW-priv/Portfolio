def fizz_buzz(n1 = 3, n2 = 5, how_many = 25):
	for i in range(1, how_many+1):
		if i%n1==0 and i%n2==0:
			print('Fizz Buzz')
		elif i%n1==0:
			print('Fizz')
		elif i%n2==0:
			print('Buzz')
		else:
			print(i)

if __name__ == '__main__':
	fizz_buzz()