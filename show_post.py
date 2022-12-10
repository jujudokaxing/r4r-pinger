import praw
import ctypes  # An included library with Python install.   
import sys
from tkinter import *

def msgb0x(text, title):
	ctypes.windll.user32.MessageBoxW(0, text, title, 0)

g = sys.argv # submission id not fixed
subm_id = g[-1]

# login to reddit
reddit = praw.Reddit(client_id = '',
					client_secret = '', 
					username = '',
					password = '',
					user_agent = '',)


post_red = reddit.submission(id=subm_id)

content = str(post_red.title) + '\nBy: ' + str(post_red.author) + '\n\n' + str(post_red.selftext)
a = '[F4M] FOUND!'
b = content
'''
# new message box, bigger
msg = Message(text=b)
msg.config(bg='white', font=('Calibri', 16))
msg.pack()
mainloop()
'''
# old message box, smaller
msgb0x(str(b), str(a))
