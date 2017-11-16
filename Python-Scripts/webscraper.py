import urllib2, re, string, requests, webbrowser, bs4, urllib

html_text = urllib2.urlopen('https://www.theglobeandmail.com/news/world/china-using-ai-to-censor-sensitive-topics-in-online-group-chats/article33116794/').read()

print "Enter a keyword to check if it is in the webpage"
string = raw_input('> ') #user input for specific keyword
matches = re.findall(string, html_text); #finds all traces of the keyword 'string' in url

if len(matches) == 0: #reverse checking -- if there are no matches, string does not exist
   print 'String is not present in text'
else: #otherwise, string exists
    print 'String is in text'


print('Enter keywords:')
search = raw_input('> ')

url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=' + search + \
      '&rsv_spt=3&rsv_bp=0&ie=utf-8&tn=baiduhome_pg'

print('Searching in Baidu...') #display text while downloading
res = requests.get(url)

res.raise_for_status()

print res.status_code

site = urllib2.urlopen(url)

print "Server:", site.info()['server']




# gmail_user = "bobshah1234223@gmail.com"
# gmail_pwd = "sproutlogix"