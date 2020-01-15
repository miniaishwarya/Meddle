# hamming distance is checking the number of bits which differ in both numbers
def hammingdistance(x,y): 
	
    setbits=0
    # performing xor operation on x and y --> 0 ^ 1 = 1 : 0 ^ 0 = 0 : 1 ^ 1 = 1 : 1 ^ 0 = 0 
    num = x ^ y

    while(num>0):
        setbits +=num & 1
        num >>= 1

	return setbits 

# Driver code 
if __name__ == "__main__":
    x=int(raw_input("Num1 - "))
    y=int(raw_input("Num2 - "))
    print("Hamming distance is ",hammingdistance(x,y))
	#print("Hamming distance is ",hammingdistance(x,y)) 
