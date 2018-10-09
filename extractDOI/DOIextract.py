with open('dois.txt', 'r') as f:
	lines = f.readlines()

li = {}

for _ in lines:
	splits = _.split(':')
	file = splits[0]
	link = ''.join(splits[2:])
	if file in li:
		continue
	else:
		li[file] = 'https:' + link

for key in li:
	print li[key]