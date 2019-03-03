
import sys, string, nltk
from nltk.tokenize import sent_tokenize, word_tokenize

fileObj = dict()	# map each file to its purpose
for key in ["input", "remarks", "dict", "vocab"]:
	fileObj[key] = None

sentList = list()	# list of sentences in the input file
diction = list()	# list of dictionary words from dictionary file
vocab = dict()		# map of vocabulary words to its frequency
tense = {'past':0, 'present':0, 'future':0}

def print_all_sent():
	'''
	prints all sentences delimited by the line number.
	'''
	for i in range(len(sentList)):
		print(i, sentList[i], i)

def sent_check(sent):
	'''
	checks for any syntactical errors in 'sent'
	'''
	if sent[0].islower():
		print("ERROR: sentences must start with title case. (", sent, ")")

def remove_all_punc(word):
	'''
	remove all punctuations from 'word'
	'''
	for punc in string.punctuation:
		word = word.replace(punc, '')
	return word

def spellcheck():
	'''
	run spellcheck over all sentences
	'''
	for i in range(len(sentList)):
		run_spellcheck(i)

def run_spellcheck(i):
	'''
	tokenize sentence 'i' into words, check for spelling errors or
	delimiter errors.
	'''
	words = word_tokenize(sentList[i])
	for word in words:
		if word in string.punctuation or binarySearch(word) >= 0:
			continue
		print("Error found in sentence", i, ":", word)

def syntax(i):
	'''
	checks for any syntax errors by tokenizing each word in
	sentence i, classifies each sentence by its tense based
	on a verb in the sentence.
	'''
	# TODO implement context-free grammars for a complete syntax check
	words = word_tokenize(sentList[i])
	for a,b in nltk.pos_tag(words):
		if 'V' in b:
			if 'ed' in a:
				tense['past'] += 1
			if 'ing' in a:
				tense['present'] += 1
		if a == 'will':
			tense['future'] += 1

def syntax_check(i):
	# drives the syntax check algorithms
	for i in range(len(sentList)):
		syntax_check(i)

def vocab_freq():
	# counts the number of occurences of each vocab word
	for i in range(len(sentList)):
		words = word_tokenize(sentList[i])
		for word in words:
			if binarySearch(word):
				vocab[word] += 1

def output_remarks():
	# TODO output remarks to the target file
	pass

def binarySearch(word):
	'''
	binary search if 'word' is in the dictionary 'dict'.
	assume 'dict' contains all English words in sorted array.
	'''
	word = word.lower()
	lo = 0
	hi = len(diction) - 1
	while lo <= hi:
		mid = (lo+hi)//2
		if diction[mid] == word:
			return mid
		elif diction[mid] < word:
			lo = mid+1
		else:
			hi = mid-1
	return -1

if __name__ == '__main__':

	# command: python3 grade.py -in=essay1.txt -out=remarks.txt 
	# [-voc=vocab.txt] -dict=dictionary.txt
	for fileTitle in sys.argv:
		if fileTitle[0:4] == '-in=':
			fileObj['input'] = fileTitle[4:]
		elif fileTitle[0:5] == '-out=':
			fileObj['remarks'] = fileTitle[5:]
		elif fileTitle[0:5] == '-voc=':
			fileObj['vocab'] = fileTitle[5:]
		elif fileTitle[0:6] == '-dict=':
			fileObj['dict'] = fileTitle[6:]

	# Read input essay
	if fileObj['input'] is None:
		print('No input file provided.')
		sys.exit()
	else:
		
		# tokenize sentences from the essay
		with open(fileObj['input'], 'r+') as essayFile:
			tmp = ""
			for line in essayFile:
				tmp += line.strip()

			sentList = sent_tokenize(tmp)

	# input dictionary words, if dictionary provided
	if fileObj['dict'] is None:
		print('No dictionary provided.')
	else:
		with open(fileObj['dict'], 'r+') as wordsFile:
			for word in wordsFile:
				diction.append(word.strip())

	if fileObj['vocab'] is None:
		print('No vocabulary requirement provided.')
	else:
		with open(fileObj['vocab'], 'r+') as wordsFile:
			for word in wordsFile:
				vocab[word] = 0

