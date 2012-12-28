'''
This function will get the contents of a webpage
'''
def get_page(url):
	import urllib
	try:
		return urllib.urlopen(url).read()
	except:
		return ""

'''
this link extracts the first link in the page content passed
start_link finds the location of the start of the links

when no more link is found, start_link = -1 and it return None and 0
starting from the start of the link tag search for the link start
find the end of the link
return the url and the end_quote. We need the end_quote to start finding the next links
'''
def get_link(page):
    start_link = page.find('<a href=')     
	if start_link == -1:					   
		return None, 0
	start_quote = page.find('"', start_link)	
	end_quote = page.find('"', start_quote + 1) 
	url = page[start_quote+1:end_quote]			
	return url, end_quote						

'''
This function keeps on working till it store all the link in the list_name
that list is empty at first. find the url. if the url is there, then store the url into the list
and make the page start from the end_quote. The page contents will have the contents after the url. BUT if no url is found, break the loop. Return all the urls found on that page.
'''	
def get_all_links(page):
	list_name = []				
	while True:					
		url, endpos = get_link(page)
		if url:								
			list_name.append(url)
			page = page[endpos:]
		else:								
			break
	return list_name						

'''
These are some extra utility functions.
'''
def print_list(p):
	for e in p:
		print e	

def union(list1, list2):
	for e in list2:
		if e not in list1:
			list1.append(e)
			
#======================Crawler===================================
'''
This is the main crawler function. It starts with a seed link and keeps on adding links found on that page to the list tocrawl. Now it goes to the last url in tocrawl list and extracts all urls from the new page. they all get stored in tocrawl and the page url get stored in crawled list. It keeps on going till it finds all the links and the links on those links and so on. 
but we should remember that we do not crawl on the the already crawled pages. so we make a check if current_link not in crawled to see that.
'''          
def crawl(seed):
	tocrawl = [seed]
	crawled = []
	while tocrawl:
		current_link = tocrawl.pop()
		if current_link not in crawled:
			union(tocrawl, get_all_links(get_page(current_link)))
			crawled.append(current_link)
	return crawled

print_list(crawl('http://www.udacity.com/cs101x/index.html'))