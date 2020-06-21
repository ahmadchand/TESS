import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv('animals.csv')
df_names = df
df_names.classes.replace({'Mammal': 0, 'Bird': 1}, inplace=True)
Xfeatures = df_names['name']
cvect = CountVectorizer()
X = cvect.fit_transform(Xfeatures)
y = df_names.classes
clf = MultinomialNB()
clf.fit(X, y)


def giveMeName(val):
 new = cvect.transform([val])
 y_pred = clf.predict(new)
 if (y_pred == 0):
  return "Mammal"
 else:
  return "Bird"

# print(giveMeName("deer"))
