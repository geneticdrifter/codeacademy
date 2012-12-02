#importing the os modules
import os
#asking for input about bedtime
bedtime = raw_input("Is it bedtime?")
#always use def and colon at the end when defining functions
def shut_down():
#lowered so that you can put any version of yes in, remember double equals
    if bedtime.lower() == "yes":
        print "Shutting down..."
        #this will suspend the computer
        #os.system ("pmi action suspend")
        #this will shut the computer down
        #os.system("sudo shutdown")
    #for if you change your mind  
    elif bedtime.lower() == "no":
        print "Shutdown aborted!"
    else:
        print "Sorry, I didn't understand you."
		
shut_down()
