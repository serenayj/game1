import time

def countdown(t):
    while t:
    	status = False 
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print "\n",timeformat
        time.sleep(1)
        t -= 1
    print('Goodbye!\n\n\n\n\n')
    status = True 
    return status

