import praw
import json
from collections import Counter
import time

reddit = praw.Reddit(
    client_id="RyhoH9FE3QNpXIe5stCQ7A",
    client_secret="YHm3cIWF90PbPykHZEdyYYa4_LgOrQ",
    user_agent="appTester123"
)


list_of_random_users = []
desired_samples = 20
current_sample = 0
while current_sample != desired_samples:
	start = time.process_time()
	random_user = str(next(reddit.subreddit('random').new(limit=1)).author)
	print(time.process_time() - start, ' fetch random user ', random_user)

	start = time.process_time()
	users_engagements = reddit.redditor(random_user).new(limit=100)
	print(time.process_time() - start, 'user engagements, received ', users_engagements)
	
	start = time.process_time()	
	subs = [{'subreddit': str(sub.subreddit), 'user': random_user} for sub in users_engagements]
	print(time.process_time() - start, 'list of subs/users created')
	
	if len(subs) != 100:
		print(len(subs), 'len too small\n\n')
		continue
	
	start = time.process_time()
	list_of_random_users = list_of_random_users + subs
	print(time.process_time() - start, current_sample, 'current sample copied \n\n')
	current_sample += 1
		
with open('./test.json', 'a') as test:
	json_string = json.dumps(list_of_random_users)
	json = json_string.replace('},', '}\n').replace('[[', '').replace(']]', '')
	test.write(json)








































#submission = reddit.submission(url="""https://www.reddit.com/r/Python/comments/1g22nr/praw_user_agent_im_a_noob/""")


#sub = redditor.submissions.new(limit=100)
#comments = reddit.comments.new(limit=50)
#all = reddit.redditor("lothdran").new(limit=100)

#subs = [sub.subreddit for sub in all]
#subCount = Counter(subs)
#print(subCount)





#user_engagements = reddit.redditor(user).new(limit=100)
#for engagement in user_engagements:
#	print(engagement.subreddit)
	
#for i in subreddit:
#	print(i.author)
#help(subreddit)
#print(subreddit)
