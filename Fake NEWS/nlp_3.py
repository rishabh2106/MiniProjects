<<<<<<< HEAD
# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('fake.csv')
# A quick look at the data
dataset.info()
# finding the dimensions
print(dataset.shape)

# Combining Both title and text
dataset['total']=dataset['author']+' '+dataset['title']+' '+dataset['text']

#******************************************************************************
# TRAINING SET
# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(12999):
    # REMOVE PUNTUATIONS AND ANY CHARACTER OTHER THAN ALPHABET
    review = re.sub('[^a-zA-Z]', ' ', str(dataset['total'][i]))
    review = review.lower()
    review = review.split()
    # Stemming object
    ps = PorterStemmer()
    # Stemming + removing stopwords
    review = [ps.stem(word) for word in review if not word in \
              set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

#******************************************************************************
#******************************************************************************

# Creating BAG OF WORDS MODEL :
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 11000)
X = cv.fit_transform(corpus).toarray()

#*****************************************************************************

# Creating TF-IDF MODEL :

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 2)
X =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names()

#*****************************************************************************

Y = dataset.iloc[:,19].values
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
Y = labelencoder.fit_transform(Y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20,random_state = 0)

#*****************************************************************************
#*****************************************************************************
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss

# PREDICTION : Accuracy Score
def acc_score(y_test, y_pred ) :
    acc = accuracy_score(y_test, y_pred)
    return print("Final Accuracy: %0.04f" %(acc))

# PREDICTION : Log-Loss
def log_loss(y_test, y_pred ) :
    acc = log_loss(y_test, y_pred)
    return print("Final Accuracy: %0.04f" %(acc))    

# acc_score(y_test, y_pred )
# log_loss(y_test, y_pred )

#*****************************************************************************
#*****************************************************************************

# Fitting NAIVE BAYES to the Training set

from sklearn.naive_bayes import MultinomialNB
classifier_1 = MultinomialNB()
classifier_1.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier_1.predict(X_test)

# Accuracy of the model
acc_score(y_test, y_pred )

# Final Accuracy: 0.7531 BOW
# Final Accuracy: 0.8846 tfidf

#*****************************************************************************

# Fitting LOGISTIC REGRESSION to the Training set
from sklearn.linear_model import LogisticRegression
classifier_2 = LogisticRegression(random_state = 0)
classifier_2.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier_2.predict(X_test)

# Accuracy of the model
acc_score(y_test, y_pred )

# Final Accuracy: 0.9050 BOW
# Final Accuracy: 0.8869 tfidf

#******************************************************************************
#******************************************************************************

from sklearn.ensemble import ExtraTreesClassifier
                            
Extr = ExtraTreesClassifier(n_estimators=5,n_jobs=4)
Extr.fit(X_train, y_train)

print('Accuracy of Extratrees classifier on test set: %0.04f'
     %(Extr.score(X_test, y_test)))

# Accuracy of Extratrees classifier on test set: 0.9004 BOW
# Accuracy of Extratrees classifier on test set: 0.9115 tfidf

#******************************************************************************

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

Adab= AdaBoostClassifier(DecisionTreeClassifier(max_depth=3),n_estimators=5)
Adab.fit(X_train, y_train)

print('Accuracy of AdaBooost classifier on test set: %0.04f'
     %(Adab.score(X_test, y_test)))

# Accuracy of AdaBooost classifier on test set: 0.8992 BOW
# Accuracy of AdaBooost classifier on test set: 0.9019 tfidf

#******************************************************************************

from sklearn.ensemble import RandomForestClassifier
Rando= RandomForestClassifier(n_estimators=5)

Rando.fit(X_train, y_train)

print('Accuracy of RandomForest classifier on test set: %0.04f'
     %(Rando.score(X_test, y_test)))

# Accuracy of RandomForest classifier on test set: 0.9027 BOW
# Accuracy of RandomForest classifier on test set: 0.8981 tfidf

#******************************************************************************



=======
# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('fake.csv')
# A quick look at the data
dataset.info()
# finding the dimensions
print(dataset.shape)

# Combining Both title and text
dataset['total']=dataset['author']+' '+dataset['title']+' '+dataset['text']

#******************************************************************************
# TRAINING SET
# Cleaning the texts
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(12999):
    # REMOVE PUNTUATIONS AND ANY CHARACTER OTHER THAN ALPHABET
    review = re.sub('[^a-zA-Z]', ' ', str(dataset['total'][i]))
    review = review.lower()
    review = review.split()
    # Stemming object
    ps = PorterStemmer()
    # Stemming + removing stopwords
    review = [ps.stem(word) for word in review if not word in \
              set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

#******************************************************************************
#******************************************************************************

# Creating BAG OF WORDS MODEL :
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 11000)
X = cv.fit_transform(corpus).toarray()

#*****************************************************************************

# Creating TF-IDF MODEL :

from sklearn.feature_extraction.text import TfidfVectorizer
tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 2)
X =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names()

#*****************************************************************************

Y = dataset.iloc[:,19].values
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
Y = labelencoder.fit_transform(Y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.20,random_state = 0)

#*****************************************************************************
#*****************************************************************************
from sklearn.metrics import accuracy_score
from sklearn.metrics import log_loss

# PREDICTION : Accuracy Score
def acc_score(y_test, y_pred ) :
    acc = accuracy_score(y_test, y_pred)
    return print("Final Accuracy: %0.04f" %(acc))

# PREDICTION : Log-Loss
def log_loss(y_test, y_pred ) :
    acc = log_loss(y_test, y_pred)
    return print("Final Accuracy: %0.04f" %(acc))    

# acc_score(y_test, y_pred )
# log_loss(y_test, y_pred )

#*****************************************************************************
#*****************************************************************************

# Fitting NAIVE BAYES to the Training set

from sklearn.naive_bayes import MultinomialNB
classifier_1 = MultinomialNB()
classifier_1.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier_1.predict(X_test)

# Accuracy of the model
acc_score(y_test, y_pred )

#*****************************************************************************

# Fitting LOGISTIC REGRESSION to the Training set
from sklearn.linear_model import LogisticRegression
classifier_2 = LogisticRegression(random_state = 0)
classifier_2.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier_2.predict(X_test)

# Accuracy of the model
acc_score(y_test, y_pred )

#******************************************************************************
#******************************************************************************

from sklearn.ensemble import ExtraTreesClassifier
                            
Extr = ExtraTreesClassifier(n_estimators=5,n_jobs=4)
Extr.fit(X_train, y_train)

print('Accuracy of Extratrees classifier on test set: %0.04f'
     %(Extr.score(X_test, y_test)))

# Accuracy of Extratrees classifier on test set: 0.8374
#******************************************************************************

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

Adab= AdaBoostClassifier(DecisionTreeClassifier(max_depth=3),n_estimators=5)
Adab.fit(X_train, y_train)

print('Accuracy of Extratrees classifier on test set: %0.04f'
     %(Adab.score(X_test, y_test)))

# Accuracy of Extratrees classifier on test set: 0.8224
#******************************************************************************

from sklearn.ensemble import RandomForestClassifier
Rando= RandomForestClassifier(n_estimators=5)

Rando.fit(X_train, y_train)

print('Accuracy of Extratrees classifier on test set: %0.04f'
     %(Rando.score(X_test, y_test)))

# Accuracy of Extratrees classifier on test set: 0.7995

#******************************************************************************



>>>>>>> 374fd8489ca3315961c1d085813734e38d2602a7
