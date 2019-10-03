import time

name = input("What is your name?  ")
print('Hello {0}'.format(name))
feeling = input("How are you today? ")
feeling_split = feeling.split(' ')
if len(feeling_split) > 1:
	for word in feeling_split:
		word = word.lower().replace('.','').replace('!','').replace(',','')
		if word in ['sad','sonely','depressed']:
			print('I am sorry to hear that {0}'.format(name))
			break
		if word in ['happy','glad','excited']:
			print('That is really awesome. Cheers ^_^!')
			break
		if word in ['fine','ok','okay']:
			solution = input('What would make your day better? ')
			solution_split = solution.split(' ')
			if len(solution_split) > 1:
				for word in solution_split:
					word = word.lower().replace(',','').replace('!','').replace(',','')
					if word.lower().replace('.','') == 'hug':
						print('*gives virtual hug*')
						print('...')
						time.sleep(1)
						print('...')
						time.sleep(1)
						print('I hope that helps ^_^!')
						break
			if len(solution_split) == 1:
				print('Hmm...Interesting.')
				break
if len(feeling_split) == 1:
	word = feeling_split[0].lower().replace('.','').replace('!','').replace(',','')
	if word in ['sad','sonely','depressed']:
		print('I am sorry to hear that {0}'.format(name))
	if word in ['happy','glad','excited']:
		print('That is really awesome. Cheers!')
	if word in ['fine','ok','okay']:
		solution = input('What would make your day better? ')
		solution_split = solution.split(' ')
		if len(solution_split) > 1:
			for word in solution_split:
				word = word.lower().replace('.','').replace('!','').replace(',','')
				if word == 'hug':
					print('*gives virtual hug*')
					print('...')
					time.sleep(1)
					print('...')
					time.sleep(1)
					print('I hope that helps ^_^!')
					break
		if len(solution_split) == 1:
			print('Hmm...Interesting.')


