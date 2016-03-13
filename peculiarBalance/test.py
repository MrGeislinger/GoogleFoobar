from solution import answer

# Ask user for a start and end for the range of weights to test
while True:
	start = input("Enter an integer (between 0 and 10^9) from where to start the test range: ")
	end = input("Enter an integer (between 0 and 10^9) from where to end the test range: ")
	if(start > end):
		print("The end occurs after the beginning: \n\tStart:%d \n\tEnd:%d" %(start,end))
	elif(end > pow(10,9)):
		print("Start or end is out of bounds; pick a start or end in the bounds of 0 to 10^9")
	else:
		for i in range(start,end):
			print "%d: " %(i),answer(i)
