import json

# the content here could be read from a file instead

result = []
with open('./nsfw_subs.ndjson', 'r') as ndjson_file, open('./nsfw_subs.json', 'w') as json_file:
	ndjson = ndjson_file.read()
	result = []
	for line in ndjson.splitlines():
		print(line)
		if not line.strip():
			continue
		next_line = json.loads(line)
		result.append(next_line)
	json_file.write(json.dumps(result))




