import pandas as pd
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from category_encoders import OneHotEncoder
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle
import numpy as np

hy_df = pd.read_csv('Hygieia_Management_System.csv')
hy_df.drop(columns =['diagnosis_id','patient_id','confirmatory_test_id','symptom_id',
                    'symptom_type', 'cause', 'disease_type', 'result'], inplace=True)
hy_df.fillna('bleeding', inplace=True)

hy_df.info()
hy_df.isnull().sum()
hy_df.columns
hy_df.value_counts()


y_label = hy_df['disease_id']
X_symptoms = hy_df['symptom_name']

# nltk.download('punkt')
# nltk.download('stopwords')

# stop_words = set(stopwords.words('english'))


# def preprocess_text(text):
#     # Tokenization
#     words = word_tokenize(text.lower())
#     # Removing stopwords and non-alphabetic characters
#     words = [word for word in words if word.isalpha() and word not in stop_words]
#     return ' '.join(words)

# preprocessed_symptoms = X_symptoms.apply(preprocess_text)
# print(X_symptoms)
# print(preprocessed_symptoms)

# Generate Word Cloud for symptoms
all_text = ' '.join(X_symptoms)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)


# # Plotting Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

disease_counts = hy_df['disease_name'].value_counts()

# # Plotting a bar chart
plt.figure(figsize=(12, 6))
plt.bar(disease_counts.index, disease_counts.values, color='green')
plt.xlabel('Disease')
plt.ylabel('Count')
plt.title('Distribution of Diseases')
plt.xticks(rotation=90)
plt.show()

# # Split data into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(X_symptoms, y_label, train_size=0.8, random_state=42)

model =    RandomForestClassifier()


model.fit(X_train,y_train)

y_predict= model.predict(X_test)
acc_score =accuracy_score(y_test,y_predict)
print(X_train)
print(acc_score)

# # print(classification_report(y_test, y_predict))

# # # Example Usage
# symptom = (1,2,3,4)
# symptom_array = np.asarray(symptom)
# symptom_reshape = symptom_array.reshape(1,-1)


# # Preprocess the input symptom
# preprocessed_symptom = preprocess_text(symptom)

# # Transform the preprocessed symptom using the same vectorizer used during training
# symptom_tfidf = tfidf_vectorizer.transform([preprocessed_symptom])

# predicted_disease = model.predict(symptom_tfidf)
# print('There are chances you may have',predicted_disease[0],'See your Doctor immediately')

pickle.dump(model, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[55]]))

