import random


def create_file(fname):
	with open(fname, 'w') as file:
		i = 1
		while i <= 10000:
			a = random.randint(0, 9)
			file.write(str(a)+'\n')
			i += 1


def give_line(fname):
	res = 0
	with open(fname, 'r') as file:
		list_lines = [int(line.rstrip()) for line in file.readlines()]
		return sum(list_lines)

create_file('file.txt')
print(give_line('file.txt'))
