import json
import urllib2
from selenium import webdriver
from socket import error as SocketError
import socket

site = 'http://www.bing.com'

def is_bad_proxy(pip):
    
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req = urllib2.Request(site)  # change the URL to test here
        sock = urllib2.urlopen(req)
        print sock.geturl()
        print sock.getcode()
        #print "Server:", sock.info()
        
    except urllib2.HTTPError, e:
        print 'Error code: ', e.code
        return e.code
    except Exception, detail:
        print "ERROR:", detail
        return True
    return False

def proxy_nova():
    
    driver = webdriver.PhantomJS('/usr/local/bin/phantomjs') #Changed this part of code
    
    print('Opening browser in background...')
    driver.get('https://www.proxynova.com/proxy-server-list/country-cn/')

    data = []
    print('Extracting proxy table...')
    for tr in driver.find_elements_by_xpath('//table[@id="tbl_proxy_list"]//tr'):
        tds = tr.find_elements_by_tag_name('td')
        if tds:
            data.append([td.text for td in tds])
    
    print('Closing browser...')
    driver.close()
    
    print('Extracting proxies...')    
    
    proxyNova_list = []
    for i in xrange(12):
        proxyNova_list.append(str(data[i][0] + ':' + data[i][1]))
            
    for i in xrange(13, len(data), 1):
        proxyNova_list.append(str(data[i][0] + ':' + data[i][1]))
    
    return proxyNova_list
    
    
def gatherproxy():
    
    driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
    
    print('Opening browser in background...')
    driver.get('http://www.gatherproxy.com/proxylist/country/?c=China')

    list = []
    print('Extracting proxy table...')
    for tr in driver.find_elements_by_xpath('//table[@id="tblproxy"]//tr'):
        tds = tr.find_elements_by_tag_name('td')
        if tds:
            list.append([td.text for td in tds])
    
    print('Closing browser...')
    driver.close()
    
    print('Extracting proxies...')    
    
    gatherproxy_list = []
    
    for i in xrange(1, len(list), 1):
        gatherproxy_list.append(str(list[i][1] + ':' + list[i][2]))

    return gatherproxy_list


def main(mylist):

    socket.setdefaulttimeout(30)
    
    goodProx = []    
    
    for currentProxy in mylist:
        print('Reading and analyzing proxy...')
        if is_bad_proxy(currentProxy):
            print "Bad Proxy %s" % (currentProxy)

        else:
            print "%s is working" % (currentProxy)
            goodProx.append(currentProxy)
            
    with open('good-proxies.txt', 'a') as myfile:
        for item in goodProx:
            myfile.write("%s\n" % item)
            # print item

# main(proxy_nova())
# main(gatherproxy())



with open('textfile.txt', 'r') as txtfile:
    for line in txtfile:
        line = line.replace(' ', '+')
        
        site = 'http://cn.bing.com/search?q=' + line + '&qs=n&form=QBRE&sp=-1&sc=8-4&sk=&cvid=6F4CEF6072CD4AD7BC70B5E25268F9CD'
        
        proxy_handler = urllib2.ProxyHandler({'http': '111.62.251.106:80'})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req = urllib2.Request(site)  # change the URL to test here
        sock = urllib2.urlopen(req)
        print sock.geturl()
        print sock.getcode()
        






