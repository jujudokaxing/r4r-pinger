import praw
import time
import ctypes  # An included library with Python install.   
from winsound import Beep
import datetime
import os
from colorama import Fore, Back, Style, init
import sys
import time
import threading

pause_time_wait = 1		# pause before finding new one; default is 60 (1 minute)
usernumberlimit = 5 	# declare how many posts to check every refresh
						# default is 1

subrdd = 'phr4r'		# declare what subreddit



# reddit login
reddit = praw.Reddit(client_id = '',
					client_secret = '', 
					username = '',
					password = '',
					user_agent = '',)



init()
os.system('cls')



# spinner class, for effect
class Spinner:
    busy = False
    delay = 0.1

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False

# function for box pop-up if enabled
def box_pop(l):
	ctypes.windll.user32.MessageBoxW(0, l, "F4M Found!!!", 1)

# function to get time
def get_date(submission):
	time = submission.created
	d = datetime.datetime.fromtimestamp(time)
	d = str(d)
	d = d.split()
	return d[1]



subreddit = reddit.subreddit(subrdd) # declare what subreddit
flag = 0
new_submission = subreddit.new(limit=50)

print('\n Latest 7 posts in r/' + subrdd + ': \n')
for submission in new_submission:
	if "[F4M]" in str(submission.title).upper():
		if flag > 6:
			break
		else:
			flag = flag + 1
		dd = submission.title.split()
		if int(dd[0]) <= 22:
			print(Fore.WHITE, end='') 
		
		show_con = '\t [' + str(flag) +  ']  ' + str(get_date(submission)) + '\t' + str(submission.title)
		show_auth = '\t\tUser: ' + str(submission.author)
		print(show_con)
		print(show_auth)
		print(Style.RESET_ALL)
	#	os.system('python show_post.py ' + str(submission)) # linked with show_post, to show text box


new_submission = subreddit.new(limit=usernumberlimit) # redeclare userlimit

print('\nFetching latest posts...\n')
with Spinner():
# checks every submission
	flag2 = []

	while True:
		new_submission = subreddit.new(limit=usernumberlimit)
		for submission in new_submission:
			if "[F4M]" in str(submission.title).upper():

				if submission in flag2:
					break

				dd = submission.title.split()
				if int(dd[0]) <= 22:
					print(Fore.WHITE, end='') 

				show_con = '\t [*]  ' + str(get_date(submission)) + '\t' + str(submission.title)
				show_auth = '\t\tUser: ' + str(submission.author)

				print(show_con)
				print(show_auth)
				print(Style.RESET_ALL)

			# pop-up box	
			#	content = str(submission.title) + ' \n ' + str(get_date(submission))
			#	box_pop(content)
				flag2.append(submission)
				Beep(2000, 1100) # make a beep sound; frequency, duration
				os.system('python show_post.py ' + str(submission))
	#	time.sleep(pause_time_wait) # activate to allow waiting
