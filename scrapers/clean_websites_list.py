# Removes websites that are not personal sites, but rather are profiles on social
# networks etc.

import codecs
import re

with codecs.open('../data/designer_websites_part2.csv',
                 encoding = 'utf-8') as infile:
     lines = infile.readlines()

pattern = re.compile("(.com)(\/)(\w.*)")

to_delete = []
for i, l in enumerate(lines):
    url = l.split(',')[0]
    result = pattern.search(url)
    if result:
        to_delete.append(i)
    elif 'ethanallen' in url or 'blogspot' in url:
            to_delete.append(i)


for i in to_delete:
    print lines[i]
    lines[i] = '  ,  \n'

with codecs.open('../data/designer_websites_cleaned_part2.csv', 'a',
    encoding = 'utf-8') as outfile:
    for l in lines:
        outfile.write(l)
