import praw
from collections import Counter

reddit = praw.Reddit(
    client_id="RyhoH9FE3QNpXIe5stCQ7A",
    client_secret="YHm3cIWF90PbPykHZEdyYYa4_LgOrQ",
    user_agent="appTester123"
)

#submission = reddit.submission(url="""https://www.reddit.com/r/Python/comments/1g22nr/praw_user_agent_im_a_noob/""")


#sub = redditor.submissions.new(limit=100)
#comments = reddit.comments.new(limit=50)
#all = reddit.redditor("lothdran").new(limit=100)

#subs = [sub.subreddit for sub in all]
#subCount = Counter(subs)
#print(subCount)

user = reddit.subreddit('random').new(limit=1)
for i in user:
	print(i.subreddit, i.author)


#user_engagements = reddit.redditor(user).new(limit=100)
#for engagement in user_engagements:
#	print(engagement.subreddit)
	
#for i in subreddit:
#	print(i.author)
#help(subreddit)
#print(subreddit)
