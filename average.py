#! /bin/python3

with open('input.txt') as f:
	sum = 0
	cnt = 0

	for num in f:
		sum += int(num)
		cnt += 1
	print('The average of the numbers in input.txt is ' + str(sum/cnt))
