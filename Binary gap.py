def solution(N):
    binary = [] #holds each binary digit to later be appended
    power = 0 #the power 2 is put to
    PoBiGap = 0 #potetial binary gap, i.e the program hasn't encountered the 2nd 0    
    BiGap = 0 #binary gap
    bitsFound = False #the bool for if the program has found the minimum bits used to represent the denary number
    bits = 0 # the thing storing the amount of bits used
    blank = "" #to append the binary list
    while bitsFound == False:
        #checks how many bits are needed to represent the binary number
        difference = N - pow(2, bits)
        if difference <= 0:
            if difference == 0:
                power = bits + 1
            else:
                power = bits 
            bitsFound = True
        else:
            bits += 1
    tempint = N
    #appends a 1 if int take away bit is greater than 0 and ends a binary gap check, appends a 0 if not and starts a binary gap check
    for i in range (power):
        tempint -= pow(2, (power-(i+1)))
        print("the power is", pow(2, (power-(i+1))))
        if tempint >=0:
            N = tempint
            binary.append("1")
            if PoBiGap >= BiGap:
                BiGap = PoBiGap
                PoBiGap = 0
        else:
            binary.append("0")
            PoBiGap += 1
            tempint = N
        
    print(blank.join(binary))
    return BiGap
        
       
integer=int(input("enter an integer"))
print("the binary gap is: ", solution(integer))

           
       
       
       
