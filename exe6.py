x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." %y)

hilarious = False
joke_evaluation = "Is n't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "This is left side of ..."
e = "a string with a right side."

print (w + e)