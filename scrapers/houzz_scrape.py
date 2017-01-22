# Just some messy code to scrape down some data

from urls_list import cities
from bs4 import BeautifulSoup
import urllib2
import codecs
from numpy import random
from time import sleep
import numpy as np

def write_houzz_pages(url):
    """ Scrapes urls for all designer profiles from a houzz results page. """
    head = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
    r = urllib2.Request(url, None, head)
    soup = BeautifulSoup(urllib2.urlopen(r).read())

    imgs = soup.findAll('div', {'class': 'pro-cover-photos'})
    failures = 0
    new_links_count = 0
    with codecs.open('../data/houzz_pages.csv', 'r', encoding = 'utf-8') as infile:
        old_links = infile.readlines()
        with codecs.open('../data/houzz_pages.csv', 'a', encoding = 'utf-8') as outfile:
            for i in imgs:
                links = i.findAll('a', href = True)
                for l in links:
                    new_link = l['href']
                    if new_link[0] !='j':
                        if new_link+'\n' not in old_links:
                            outfile.write(new_link + '\n')
                            new_links_count += 1.0
                        else:
                            failures += 1

    if new_links_count < failures or new_links_count == 0:
        return False
    return True

for c in cities:
    for p in xrange(15, 4975, 15):
        # For each city name, add the page number and scrape scrape scrape
        allGood = write_houzz_pages(c.format(p))
        if not allGood:
            print 'Failrate too high, breaking.'
            break
        sleeptime = random.uniform(0, 4)
        msg = 'finished page {} out of about 300 for city {}. Sleeping for {} secs.'
        print msg.format(p/15, c.split('/')[-5], np.round(sleeptime, 2))
        sleep(sleeptime)
