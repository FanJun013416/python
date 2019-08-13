from sys import argv

script, first, second, third, forth = argv

print("The script is called:", script)
print("The first variable is:", first)
print("The second variable is:", second)
print("The third variable is:", third)
print("The forth variable is:", (int(forth) + 1))
name = input ("What is your name?  ")
print("So. your name is %r" % name)