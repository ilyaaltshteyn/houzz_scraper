# Just some messy code to scrape down some data quickly

from bs4 import BeautifulSoup
import urllib2
import codecs
from numpy import random
from time import sleep
import numpy as np

def get_designer_website(url):
    head = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'}
    try:
        r = urllib2.Request(url, None, head)
        soup = BeautifulSoup(urllib2.urlopen(r).read())
    except:
        print 'Had problem pulling page, sleeping for 3 min. '
        sleep(180)
        return None, None

    link = soup.find('a', {'compid': 'Profile_Website'})
    try:
        l = link['href']
    except:
        l = None

    description = soup.find('div', {'class' : 'profile-about'})
    try:
        d = description.contents
        d = str(d).replace(',', '')
    except:
        d = None

    return l, d


with codecs.open('/Users/ilya/Projects/houzz_scraper/data/houzz_pages.csv',
                 'r', encoding = 'utf-8') as infile:

    lines = infile.readlines()
    counter = 11787

    for line in lines[11787:]:
        line = line.replace('\n', '')
        l, d = get_designer_website(line)
        if l and d:
            with codecs.open('/Users/ilya/Projects/houzz_scraper/data/designer_websites_part3.csv',
                             'a', encoding = 'utf-8') as outfile:
                outfile.write(l + ',' + d + '\n')

        counter += 1
        # sleeptime = random.uniform(0, 2)
        msg = 'finished page {} out of {}.' # Sleeping for {} secs.'
        print msg.format(counter, len(lines)) #, np.round(sleeptime, 2))
        # sleep(sleeptime)
