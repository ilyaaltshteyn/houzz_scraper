import pandas as pd
import numpy as np

filename = 'grabby Output'

dat = pd.read_csv(filename, encoding = 'utf-8', names = ['email', 'website'])
normalSuffix = lambda x: 1 if x[-3:] in ('com', 'net', 'org', 'biz', 'nyc', 'us') else 0

dat['normalSuffix'] = dat.email.apply(normalSuffix)
dat_clean = dat[dat.normalSuffix == 1]

print len(dat_clean), len(set(dat_clean.website))

dat.to_csv(filename[:-4] + '_CLEAN.csv', encoding = 'utf-8', index = False)
