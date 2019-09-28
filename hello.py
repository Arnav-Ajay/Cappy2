import add
import diff
import mult
import division

#print("Enter 1 for sum \n Enter 2 for difference \n Enter 3 for product \n Enter 4 for division \n Enter 0 to exit")

#g = int(input("Enter 1 for sum \n Enter 2 for difference \n Enter 3 for product \n Enter 4 for division \n Enter 0 to exit"))
g=2

if g == 1 :
	c = add.sum(5, 6) 
	print(c)
elif g == 2 :
	c = diff.diff(6, 5)
	print(c)
elif g ==3 :
	c = mult.mult(5, 2)
	print(c)
elif g==4 :
	c = division.division_numbers(10, 2)
	print(c)
else:
	print("exiting")
	exit(0)

