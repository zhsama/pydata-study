# @Version : Python3.6
# @Time    : 2018/9/10 19:22
# @Author  : zhcf1ess
# @Site    : 
# @File    : test.py
# @Software: PyCharm

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# print(train[:5])
# print(train.isnull().sum())
# print(test.isnull().sum())
#
impute_value = train['Age'].median()
train['Age'] = train['Age'].fillna(impute_value)
test['Age'] = test['Age'].fillna(impute_value)
train['IsFemale'] = (train['Sex'] == 'female').astype(int)
test['IsFemale'] = (test['Sex'] == 'female').astype(int)

predictors = ['Pclass', 'IsFemale', 'Age']
X_train = train[predictors].values
X_test = test[predictors].values
y_train = train['Survived'].values

# print(X_train[:5])
# print(y_train[:5])

model = LogisticRegression()
model.fit(X_train, y_train)
LogisticRegression(C=1.0, class_weight=None, dual=False,
                   fit_intercept=True,
                   intercept_scaling=1, max_iter=100, multi_class='ovr',
                   n_jobs=1,
                   penalty='l2', random_state=None, solver='liblinear',
                   tol=0.0001,
                   verbose=0, warm_start=False)

y_predict = model.predict(X_test)
print(y_predict[:10])
