import pandas as pd

f1 = '../data/designer_websites.csv'
f2 = '../data/designer_websites_cleaned_part2.csv'
f3 = '../data/designer_websites_cleaned_part3.csv'

d1 = pd.read_csv(f1, names = ['site', 'description'], encoding = 'utf-8')
d2 = pd.read_csv(f2, names = ['site', 'description'], encoding = 'utf-8')
d3 = pd.read_csv(f3, names = ['site', 'description'], encoding = 'utf-8')

dat = pd.concat([d1, d2, d3])

ems = {'email' : [], 'houzz' : []}
for i, r in dat.iterrows():
    if '@' in r['site']:
        ems['email'].append(r['site'][7:])
        ems['houzz'].append(r['description'])


dat2 = pd.DataFrame(ems)
dat2.to_csv('../data/sites_that_were_actually_emails.csv', encoding = 'utf-8')
