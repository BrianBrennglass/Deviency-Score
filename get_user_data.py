import praw

reddit = praw.Reddit(
    client_id="RyhoH9FE3QNpXIe5stCQ7A",
    client_secret="YHm3cIWF90PbPykHZEdyYYa4_LgOrQ",
    user_agent="appTester123"
)

submission = reddit.submission(url="""https://www.reddit.com/r/Python/comments/1g22nr/praw_user_agent_im_a_noob/""")


#sub = redditor.submissions.new(limit=100)
#comments = reddit.comments.new(limit=50)
all = reddit.redditor("lothdran").new(limit=100)
l = 0
for i in all:
	l+=1
	print(i.subreddit, i.permalink, i.over_18)

print('\n', all)
