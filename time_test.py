import sys, time, msvcrt #msvcrt allows keystrokes to be read.


#readInput continuously checks to see if 15 seconds has been reached
#and breaks out of loop if an input has not been given.
def readInput( caption, default, timeout = 15):
    start_time = time.time()
    sys.stdout.write('%s[Default=%s]:'%(caption, default));
    print("")
    input = ''
    while True:
        if msvcrt.kbhit(): #kbhit functuion returns true if a key is hit
            chr = msvcrt.getche() #reads the key pressed on keyboard and stores it as chr
            if ord(chr) == 13: # enter_key
                break
            elif ord(chr) == 8: # backspace
                input = input[0:-1]
            elif ord(chr) == 224: #Special Characters like arrows, ins, delete, etc.
                chr = msvcrt.getche()
                if ord(chr) == 72: # Up Arrow
                    pass
                elif ord(chr) == 75: # Left Arrow
                    pass
                elif ord(chr) == 77: # Right Arrow
                    pass
                elif ord(chr) == 80: # Down Arrow
                    pass
                elif ord(chr) == 83: # Delete Key
                    pass
                else:
                    pass
                
            elif chr.isalnum(): #>= 32: #Any other characters
                input += chr
            elif chr == " ":
                input += chr
                
        print("\r"+" "*70+"\r" + input),
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    print ''  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        return default #this returns default value for weapon if the user can't select in the appropriate time.

def debugKeyStroke():
    while True:
        print(ord(msvcrt.getche()))
        
if __name__ == "__main__":
    print (readInput("Test Input:",""))