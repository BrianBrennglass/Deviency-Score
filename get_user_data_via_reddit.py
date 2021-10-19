import praw

reddit = praw.Reddit(
    client_id="RyhoH9FE3QNpXIe5stCQ7A",
    client_secret="YHm3cIWF90PbPykHZEdyYYa4_LgOrQ",
    user_agent="appTester123"
)

def getUserData(user):
	users_engagements_object = reddit.redditor(user).new(limit=100)
	user_engagements_extracted = {'subreddit': [], 'user': [], '18+_engagement': []}
	for engagement in users_engagements_object:
		#help(engagement)
		user_engagements_extracted['subreddit'].append(engagement.subreddit)
		user_engagements_extracted['user'].append(engagement.author)
		user_engagements_extracted['18+_engagement'].append(engagement.over_18)
	return user_engagements_extracted

