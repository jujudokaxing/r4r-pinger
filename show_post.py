import praw
import ctypes  # An included library with Python install.   
import sys

def msgb0x(text, title):
	ctypes.windll.user32.MessageBoxW(0, text, title, 0)

g = sys.argv # submission id not fixed
subm_id = g[-1]


# login to reddit
reddit = praw.Reddit(client_id = 'qd3fFRnBK468ud50B-D-lA',
					client_secret = 'wXZctO0d2rQb2fujr2pnschuAPN3aA', 
					username = 'DempseyCallz',
					password = 'Mountaindew!1',
					user_agent = 'NANANA',)

post_red = reddit.submission(id=subm_id)

content = str(post_red.title) + '\n\n' + str(post_red.selftext)
a = '[F4M] FOUND!'
b = content

msgb0x(str(b), str(a))
