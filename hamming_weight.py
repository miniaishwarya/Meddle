def hammingWeight(n):
        """
        :type n: int
        :rtype: int
        """
        
        setbits=0
        
        while(n>0):
            setbits += n & 1
            n >>= 1
        return setbits

if __name__ == "__main__":
    n=int(raw_input("Number in binary"))
    print("Hamming weight: ",hammingWeight(n))