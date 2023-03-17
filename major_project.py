# -*- coding: utf-8 -*-
"""MAJOR PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bl2_tVItiK69VXKg1yjSWl7bbvHFnbuE
"""

import pandas as pd
df=pd.read_table("/content/Restaurant_Reviews.tsv")
df

df.info()

df.shape

df.isnull().sum()

import seaborn as sns
sns.countplot("Liked",data=df)

df['Length']=df['Review'].apply(len)
df.head()

df.describe()

#tokenisation
df.Review[2]

df['Liked'].nunique()

print(df['Liked'].unique())

"""dataset is balanced"""

df['Liked'].value_counts()

df.head()

x=df['Review'].values
y=df['Liked'].values

"""Trainining the data"""

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0)

"""COUNT VECTORIZER"""

from sklearn.feature_extraction.text import CountVectorizer
vect=CountVectorizer(stop_words='english')

x_train_vect=vect.fit_transform(x_train)
x_test_vect=vect.transform(x_test)

"""TFID VECTORIZER"""

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english')

x_train_tfid=vectorizer.fit_transform(x_train)
x_test_tfid=vectorizer.transform(x_test)

"""METHOD 1 
USING SVM+count vectorizer
"""

from sklearn.svm import SVC
model=SVC()
model.fit(x_train_vect,y_train)

y_pred=model.predict(x_test_vect)

y_pred

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred,y_test)

"""MODEL 2(SVC+COUNTVECT)PIPELINE


"""

from sklearn.pipeline import make_pipeline
model2=make_pipeline(CountVectorizer(),SVC())
model2.fit(x_train,y_train)
y_pred2=model2.predict(x_test)
y_pred2

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred2,y_test)

"""METHOD 3 NAIVE BAYES+count vectorizer"""

from sklearn.feature_extraction.text import CountVectorizer
vect=CountVectorizer(stop_words='english')

x_train_vect=vect.fit_transform(x_train)
x_test_vect=vect.transform(x_test)

from sklearn.naive_bayes import MultinomialNB
model3=MultinomialNB()
model3.fit(x_train_vect, y_train)

y_pred3=model3.predict(x_test_vect)
y_pred3

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred3,y_test)

"""using pipeline for(count vectorize+NB) method 4"""

from sklearn.pipeline import make_pipeline
model4=make_pipeline(CountVectorizer(),MultinomialNB())
model4.fit(x_train,y_train)
y_pred4=model4.predict(x_test)
y_pred4

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred4,y_test)

"""MODEL5-(SVC+TFID)"""

from sklearn.svm import SVC
model5=SVC()
model5.fit(x_train_tfid,y_train)

y_pred5=model5.predict(x_test_tfid)
y_pred5

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred5,y_test)

"""MODEL 6(TFID+SVC)PIPELINE"""

from sklearn.pipeline import make_pipeline
model6=make_pipeline(TfidfVectorizer(),SVC())
model6.fit(x_train,y_train)
y_pred6=model6.predict(x_test)
y_pred6

y_test

from sklearn.metrics import accuracy_score
accuracy_score(y_pred6,y_test)

"""MODEL 7 LOGISTIC REGRESSION """

from sklearn.linear_model import LogisticRegression
LR = LogisticRegression(random_state=0).fit(x_train_vect, y_train)
y_pred7=LR.predict(x_train_vect)
LR.score(x_train_vect,y_train)#the mean accuracy on the given test data and labels

y_pred7

y_test

from sklearn.metrics import mean_absolute_error 
mean_absolute_error(y_train,y_pred7)

from sklearn.metrics import mean_squared_error
mean_squared_error(y_train,y_pred7)

from sklearn.metrics import r2_score
r2_score(y_train, y_pred7)

"""*  MODEL1-ACCURACY(72%)(SVC)


*  MODEL2-ACCURACY(79.2%)(SVC+COUNTVECTORIZER)PIPELINE
  

*   MODEL3-ACCURACY(74.4%)(NAIVE BAYES)
   

*  MODEL4-ACCURACY(78.4%)(NB+COUNTVECTORIZER)PIPELINE


AFTER ANALYSING 4 MODELS JOBLIB THE MODEL WITH HIGHEST ACCURACY
    
         **MORE ML MODELS AND ALOGORITHMS** 

*   MODEL5-ACCURACY(74%)(TFID+SVC)


*   MODEL6-ACCURACY(82%)(TFID+SVC)PIPELINE

*    MODEL7-ACCURACY(96.6%)(LOGISTIC REGRESSION+COUNT VECTORIZER)

Joblib highest accuracy model ONLY FROM FIRST FOUR MODELS
"""

import joblib
joblib.dump(model4,"sentiment analysis")

reloaded_model=joblib.load("sentiment analysis")
reloaded_model

reloaded_model.predict(["i loved it"])

!pip install streamlit --quiet

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import joblib
# st.title("Restaurant_Reviews")
# reloaded_model=joblib.load('sentiment analysis')
# reloaded_model
# input1=st.text_input("enter the message:")
# output1=reloaded_model.predict([input1])
# if st.button("sentiment analysis"):
#    st.title([output1[0]])

!streamlit run app.py & npx localtunnel --port 8501

import joblib
joblib.dump(LR,"sentiment analysis2")
reloaded_model2=joblib.load("sentiment analysis")
reloaded_model2

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import joblib
# st.title("Restaurant_Reviews")
# reloaded_model2=joblib.load('sentiment analysis')
# reloaded_model2
# input2=st.text_input("enter the message:")
# output2=reloaded_model2.predict([input2])
# if st.button("sentiment analysis2"):
#    st.title([output2[0]])

!streamlit run app.py & npx localtunnel --port 8501

"""**SENTIMENT ANALYSIS:**

SENTIMENT ANALYSIS IS ANALYSING GIVEN BODY OF TEXT OR REMARK TO BE POSITIVE OR NEGATIVE OR NEUTRAL.

IS OPINION MINING,IS AN APPROACH TONATUAL LANGUAGE PROCESSING(NLP)THAT IDENTIFIES EMOTIONAL TONE BEHIND A SENTENCE OR REMARK.THIS IS A POPULAR WAY FOR ORGANIZATIONS TO DETERMINE AND CATEGORIZE OPINIONS ABOUT A PRODUCT,SERVICE,OR IDEA.
SENTIMENT ANALYSIS IS THE USE OF NATURAL LANGUAGE PROCESSING ,TEXT ANALYSIS,TO KNOW THE CUSTOMER FEEDBACK.
SENTIMENT ANALYSIS STUDIES THE SUBJECTIVE INFORMATION IN A EXPRESSION,THAT IS,THE OPINIONS,APPRAISALS,EMOTIONS,OR ATTITUDES TOWARDS A TOPIC,PERSON OR ENTITY.EXPRESSIONS CAN BE CLASSIFIED AS POSITIVE,NEGATIVE,OR NEUTRAL.

FOR EXAMPLE:
"I REALLY LIKED THE NEW DESIGN OF THE WEBSITE"->POSTIVE.

WE USE SENTIMENT ANALYSIS TOOLS TO DETECT  AND UNDERSTAND CUSTOMER FEELINGS.COMPANIES USE THIS FEEDBACK TO IMPROVE THEIR PRODUCTS.

THERE ARE MULTIPLE ALGORITHMS USED FOR SENTIMENT ANALYSIS LIKE SUPPORT VECTOR MACHINE(SVM),RECURRENT NEURAL NETWORK(RNN),COVOLUTIONAL  NEURAL NETWORK(CNN),RANDOM FOREST,NAIVE BAYES.THIS IS TECHNIQUE WIDELY USED FOR TEXT MINING.

**TWITTER SENTIMENTS:**
TWITTER SENTIMENT ANALYSIS MEANS USING ADVANCED TEXT MINING TECHNIQUES TO ANALYZE THE SENTIMENT OF THE TEXT INT HE FORM OF POSITIVE,NEGATIVE AND NEUTRAL.IT IS PRIMARILY FOR ANALYZING CONVERSATIONS,OPINIONS,AND SHARING OF VIEWS(ALL IN THE FORM OF TWEETS) FOR DECIDING BUSSINESS STRATEGY,POLITICAL ANALYTICS,AND ALSO FOR ACCESSING PUBLIC ACTIONS.

IT IS USED TWITTER SENTIMENTS TO ANALYZE THE TWEET OR AD TWEETED ON THE SOCIAL MEDIA PLATFORM TO KNOW NUMBER OF LIKES,DISLIKES,REPLIES OF THE TWEET OR AD
THE TWEETED ORGANIZATION OR PERSONS ANALYZE THIS SENTIMENTS TO KNOW THE PRODUCT VALUE AND REQUIREMENT WITHOUT READING EACH AND EVERY REPLY.
 TWITTER USES XGBOOST AND NAIVE BAYES ALGORITHM WERE TIED FOR THE HIGHEST ACCURACY OF THE 12 TWITTER SENTIMENT ANALYSIS APPROACHES TESTED.
"""