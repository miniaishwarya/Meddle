# Python3 program for implementation of simple 
# approach to find length of last word 
def lengthOfLastWord(a): 
	l = 0
    
    # creating a copy and trimming the space from both sides
	x = a.strip()

	for i in range(len(x)): 
		if x[i] == " ": 
			l = 0
		else: 
			l += 1
	return l 

# Driver code 
if __name__ == "__main__": 
	inp = raw_input()
	print("The length of last word is", 
				lengthOfLastWord(inp)) 

