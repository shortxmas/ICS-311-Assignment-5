# this is for task 4 of the assignment
import math
import datetime
import numpy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from classes.Post import Post

class InterestingPostCloud:
     def __init__(self,user_list):
	self.user_list = user_list


# create word cloud with text from posts 
def make_cloud(words):
	visual = WordCloud.generate(words)
	plt.imshow(visual)
	plt.show()


# KMP computing prefix algorithm
def kmp_prefix(pattern,length):
	matcher = []
	k = 0
	matcher[1] = 0

	for q in range(2,length+1):
		while k > 0 && pattern[k+1] != pattern[q]:
			k = matcher[k]
		if pattern[k+1] == 	pattern[q]:
			k = k+1
		matcher[q] = k
	return matcher


# KMP matching algorithm()
def kmp_match(sorted_posts):
	plist = ["dog", "pup", "poodle", "malamute"]
	mlist = [len(plist[0]),len(plist[1]),len(plist[2]),len(plist[3])]
	matches = []
	funcs = []
	txt = []
	nlist = []
	body = " "

	for x in sorted_posts:
		nlist[x] = len(sorted_posts[x].content)	
		txt[x] = sorted_posts[x].content
		if x <5:
			matches[x] = sorted_posts[x].content
	
	for y in plist:
		funcs[y] = kmp_prefix(plist[y],mlist[y])
	
	for z in txt:
		q = 0
		for i in range(1,nlist[z]+1):
			while q > 0 && plist[z][i+1] != txt[z][i]:
				q = funcs[q][i]
			if plist[z][i+1] == txt[z][i]:
				q = q+1
			if q == mlist[(j for j in mlist if j==q)]:
				body = body + txt[z] + " "
				break

	make_cloud(body)				


# merge portion of merge-sort algorithm	
def merge(left,right): 
	right_len = len(right)
	left_len = len(left)
	i,j,k = 0,0,0
	new_list = []

	while i<left_len and j< right_len:
		if len(left[i].views) <= len(right[j].views)
			new_list[k] = left[i]
			i = i+1
		else:
			new_list[k] = right[j]
			j = j+1
		k = k+1

	while i<left_len:
		new_list[k] = left[i]
		i = i+1
		k = k+1
	while j<right_len:
		new_list[k] = right[j]
		j = j+1
		k = k+1

	kmp_prefix(new_list)


# merge-sort portion of merge-sort algorithm
def merge_sort(posts):
	if len(posts) <= 1:
		return posts

	middle = math.floor(len(posts)/2)
	beginning = merge_sort(posts[:middle])	
	end = merge_sort(posts[middle:])	
	merge(beginning,end)


# restricting demographics based on user attributes: age 28-37, zip range
def restrictions(self.user_list):
	blank = self.user_list
	acceptable = []
	current = datetime.datetime.now().year

	for x in blank: 
		if blank[x].zipcode >=43001 && blank[x].zipcode <=69367 && (current - blank[x].birth_year) >= 28 && (current - blank[x].birth_year) <=37:
			acceptable.extend(blank[x].posts)
	
	merge_sort(acceptable)
