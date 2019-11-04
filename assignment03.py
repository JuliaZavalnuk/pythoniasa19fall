def task1(start, end):
	"""
	Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
	between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence
	on a single line.
	"""
	print(','.join(str(i) for i in range(start, end + 1) if i%7 == 0 and i%5 != 0))

def task2(row, col):
    """
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
    The element value in the i-th row and j-th column of the array should be i*j.
    Note: i=0,1.., X-1; j=0,1,¡­Y-1.
    Example:
    Suppose the following inputs are given to the program: 3, 5.
    Then, the output of the program should be:
    >>> task2(3, 5)
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """
    return [[i * j for i in range(col)] for j in range(row)]


def task3(password):
	"""
	A website requires the users to input username and password to register.
	Write a program to check the validity of password input by users.
	Following are the criteria for checking the password:
	1. At least 1 letter between [a-z]
	2. At least 1 number between [0-9]
	3. At least 1 letter between [A-Z]
	4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12
    Your program should accept a password and will check them according to the above criteria.
    Example:
    If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345
    Then, the output of the program should be:
    >>> task3('ABd1234@1')
    True
    >>> task3('a F1#')
    False
	>>> task3('2w3E*')
	False
	>>> task3('2We3345')
	False
	"""
	import re
	if(re.match("((?=.*[a-z])(?=.*[A-Z])(?=.*?[0-9])(?=.*?[$#@])([A-Za-z0-9\d]){6,12})", password) != None):
		return True
	else:
		return False



def task4():
	"""
	Write password generator function that uses the same rules as in Task 3.
	The password generator function must be able to generate all possible correct passwords.
	"""
	import random
	password = [0] * (random.randrange(6, 13))
	ranges = [range(65, 91), range(97, 123), range(48, 58), [35, 36, 64]]
	for i in range(len(password)):
		if i <= 3:
			password[i] = chr(random.choice(ranges[i]))
		else:
			password[i] = chr(random.choice(range(33, 127)))
	random.shuffle(password)
	print (''.join(password))


if __name__ == '__main__':
    import doctest
    doctest.testmod()