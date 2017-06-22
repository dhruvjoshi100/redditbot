import praw
import pdb
import re
import os

reddit=praw.Reddit('bot1')


if not os.path.isfile('replied_to.txt'):
	replied=[]

else:
	with open('replied_to.txt')as f:
		replied=f.read()
		replied=replied.split('\n')
		replied=list(filter(None,replied))

subreddit=reddit.subreddit('pythonforengineers')
for submissions in subreddit.hot(limit=10):
	if submissions.id not in replied:
		if re.search("i love python", submissions.title, re.IGNORECASE):
			submissions.reply('Affirmative!!\n')
			print ('Bot replied to ',submissions.title)
			replied.append(submissions.id)


with open('replied_to.txt') as f:
	for i in replied:
		f.write(i+'\n')

