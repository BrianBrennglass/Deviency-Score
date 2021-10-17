import json

# the content here could be read from a file instead

result = []
with open('./nswf_subs.ndjson', 'r') as ndjson, open('./nsfw_subs.json', 'w') as json_file:
	for line in ndjson.splitlines():
		print(line)
		if not line.strip():
			continue
		next_line = json.loads(line)
		result.append(next_line)
	json_file.write(result)




