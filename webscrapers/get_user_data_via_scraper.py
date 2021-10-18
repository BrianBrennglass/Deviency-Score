import requests
import json
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
user_responses = []
loop = 0
save_file = input('save file name ')
while loop < 1000:
	if loop % 10:
		time.sleep(3)
		
	random_subreddit = requests.get('https://old.reddit.com/random.json', headers=headers)

	status_code = random_subreddit.status_code

	if status_code != 200:
		print('status code failed ', status_code, '\n')
		raise Exception('status failed')

	subreddit_json = random_subreddit.json()
	user_object = subreddit_json[0]
	user_data = user_object['data']
	random_author = user_data['children'][0]['data']['author']
	user_url = f'https://old.reddit.com/user/{random_author}.json?limit=100'
	user_data = requests.get(user_url, headers=headers)
	user_json = user_data.json()
	user_json = user_json['data']['children']
	print(len(user_json))
	if len(user_json) != 100:
		continue
		
	for user in user_json:
		data = user['data']
		sub = data['subreddit']
		username = data['author']
		over_18 = data['over_18']
		user_outline = {'subreddit': sub, 'username': username, 'over_18': over_18}
		user_responses.append(user_outline)
	
	with open(save_file, 'a') as test:
		json_string = json.dumps(user_responses)
		ready_for_saving = json_string.replace('},', '}\n').replace('[', '\n').replace(']', '')
		test.write(ready_for_saving)
		user_responses = []
	loop += 1
	print('loop = ', loop)


	
	

