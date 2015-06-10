import sys, time, msvcrt #msvcrt allows keystrokes to be read.


#readInput continuously checks to see if 15 seconds has been reached
#and breaks out of loop if an input has not been given.
def readInput( caption, default, timeout = 15):
    start_time = time.time()
    sys.stdout.write('%s[Default=%s]:'%(caption, default));
    input = ''
    while True:
        if msvcrt.kbhit(): #kbhit functuion returns true if a key is hit
            chr = msvcrt.getche() #reads the key pressed on keyboard and stores it as chr
            if ord(chr) == 13: # enter_key
                break
            elif ord(chr) >= 32: #space_char
                input += chr
        if len(input) == 0 and (time.time() - start_time) > timeout:
            break

    print ''  # needed to move to next line
    if len(input) > 0:
        return input
    else:
        return default #this returns default value for weapon if the user can't select in the appropriate time.

        
if __name__ == "__main__":
    # and some examples of usage
    ans = readInput('Please select a weapon', 'Ruler Slap') 
    print 'The name is %s' % ans