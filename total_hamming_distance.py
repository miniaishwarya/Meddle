def totalHammingDistance(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def hammingdistance(x,y):
            a=x ^ y
            setbits=0
            
            while(a>0):
                setbits += a & 1
                a >>= 1
            
            return setbits
        
        tot=0
        
        for i in range(0,len(nums)):
            for j in range(0,i):
                tot+= hammingdistance(nums[j],nums[i])  
            
        return tot

if __name__ == "__main__":
    nums = []
    for i in range(0,3):
        nums = raw_input("Numbers: ")
    print("Total hamming distance is: ",totalHammingDistance(nums))