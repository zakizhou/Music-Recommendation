import os
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn import preprocessing
os.chdir('D:/Kaggle/reco_music/data')

train = pd.read_csv('train_merged.csv')
test = pd.read_csv('test_merged.csv')


for col in train.columns:
    if train[col].dtype == object:
        train[col] = train[col].astype('category')
        test[col] = test[col].astype('category')

train['target'] = train['target'].astype(np.int8)
train['language'] = train['language'].astype('category')
train['issue_year'] = train['issue_year'].astype(np.int16)
train['city'] = train['city'].astype(np.int8)
train['bd'] = train['bd'].astype(np.int8)
train['gender'] = train['gender'].astype(np.int8)
train['registered_via'] = train['registered_via'].astype(np.int8)
train['issue_year'] = train['issue_year'].astype(np.int16)
train['reg_year'] = train['reg_year'].astype(np.int16)
train['reg_month'] = train['reg_month'].astype(np.int8)
train['reg_day'] = train['reg_day'].astype(np.int8)
train['expire_year'] = train['expire_year'].astype(np.int16)
train['expire_month'] = train['expire_month'].astype(np.int8)
train['expire_day'] = train['expire_day'].astype(np.int8)

test['language'] = test['language'].astype('category')
test['issue_year'] = test['issue_year'].astype(np.int16)
test['city'] = test['city'].astype(np.int8)
test['bd'] = test['bd'].astype(np.int8)
test['gender'] = test['gender'].astype(np.int8)
test['registered_via'] = test['registered_via'].astype(np.int8)
test['issue_year'] = test['issue_year'].astype(np.int16)
test['reg_year'] = test['reg_year'].astype(np.int16)
test['reg_month'] = test['reg_month'].astype(np.int8)
test['reg_day'] = test['reg_day'].astype(np.int8)
test['expire_year'] = test['expire_year'].astype(np.int16)
test['expire_month'] = test['expire_month'].astype(np.int8)
test['expire_day'] = test['expire_day'].astype(np.int8)

test['id'] = range(test.shape[0])
X = train.drop('target', axis=1)
y = train['target'].values

X_test = test.drop('id', axis=1)
ids = test['id'].values
del train, test

d_train = lgb.Dataset(X, y)
watchlist = [d_train]

params = {}
params['learning_rate'] = 0.2
params['application'] = 'binary'
params['max_depth'] = 6
params['num_leaves'] = 2**8
params['verbosity'] = 0
params['metric'] = 'auc'

model = lgb.train(params, train_set=d_train, num_boost_round=50, valid_sets=watchlist, \
verbose_eval=5)


p_test = model.predict(X_test)

subm = pd.DataFrame()
subm['id'] = ids
subm['target'] = p_test
subm.to_csv('submission.csv.gz', compression = 'gzip', index=False, float_format = '%.5f')
print('Done!')




