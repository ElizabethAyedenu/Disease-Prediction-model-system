from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# import mysql.connector
from sqlalchemy import create_engine
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import seaborn as sns
sns.set_style("whitegrid")


# for sqlalchemy
db_url = "mysql+mysqlconnector://root:pharmacist@localhost/hygieia_disease_management"
sql_engine = create_engine(db_url,echo=False)
sql_query = ("""SELECT * FROM symptom JOIN disease ON symptom.disease_id = disease.disease_id""")
hy_df =pd.read_sql(sql_query, sql_engine)

hy_df.set_index('symptom_id', inplace=True)
hy_df.drop(columns = ['disease_id'], inplace = True)
hy_df.head(10)
hy_df.shape
hy_df.describe()
null_checker = hy_df.apply(lambda x: sum(x.isnull())).to_frame(name='count')
print(null_checker)
unique_disease = hy_df['disease_name'].unique()
disease_freq = hy_df['disease_name'].value_counts()

plt.figure(figsize=(12, 6))
plt.barh(disease_freq.index, disease_freq.values, color='green')
plt.xlabel('Count')
plt.ylabel('Disease')
plt.title('Distribution of Diseases')
plt.xticks(rotation=90)
plt.show()



# Do a correlation analysis here for the features
numerical_cols = ['very_dry_skin', 'sores_that_heal_slowly',
       'more_infections_than_usual', 'nausea', 'stomach_pains',
       'urinate_a_lot', 'feel_very_thirsty', 'lose_weight_without_trying',
       'blurry_vision', 'itching_hands_or_feet', 'feel_very_hungry',
       'fever', 'fatigue', 'loss_of_appetite', 'vomiting',
       'abdominal_pain', 'dark_urine', 'light_colored_stools',
       'joint_pain', 'jaundice', 'rash', 'bone_pain', 'pain_in_joint',
       'muscle_pain', 'cramp', 'eye_pain',
       'cough_with_yellow_or_green_mucus', 'shortness_of_breath',
       'high_temperature', 'chest_pain', 'aching_body',
       'feeling_very_tired', 'wheezing_noises_when_you_breathe',
       'feeling_confused', 'feverish', 'cold', 'sweating', 'headache',
       'pain_in_muscle', 'dizzy', 'cough', 'fatigue_', 'short_of_breath',
       'loss_of_taste_or_smell', 'nasal_congestion', 'runny_nose',
       'throat_soreness', 'diarrhea', 'eye_irritation', 'headaches',
       'kidney_failure', 'respiratory_failure', 'weight_gain',
       'belly_pain', 'feeling_tired', 'muscle_and_joint_pain',
       'hair_loss_and_skin_problems', 'trouble_sleeping', 'memory_loss',
       'hearing_loss', 'depression_and_anxiety', 'throat_sore',
       'dysentry', 'bleeding', 'dizziness', 'hiccups',
       'maculopapular_rash', 'shock']

# Generate Word Cloud for symptoms
all_text = ' '.join(numerical_cols)
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)


# # Plotting Word Cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

target = hy_df['disease_name'].values
features = hy_df.drop(columns = ['disease_name','disease_type']).values

X_train, X_test, y_train, y_test = train_test_split(features, target, train_size=0.8)

model = SVC(kernel="linear")
model_2 = DecisionTreeClassifier()
model_3 = LogisticRegression()
model_4 = RandomForestClassifier()

model.fit(X_train,y_train)
model_2.fit(X_train,y_train)
model_3.fit(X_train,y_train)
model_4.fit(X_train,y_train)

y_predict= model.predict(X_test)
y_predict2= model_2.predict(X_test)
y_predict3= model_3.predict(X_test)
y_predict4= model_4.predict(X_test)

acc_score =accuracy_score(y_test,y_predict)
acc_score2 =accuracy_score(y_test,y_predict2)
acc_score3 =accuracy_score(y_test,y_predict3)
acc_score4 =accuracy_score(y_test,y_predict4)

print ("The accuracy score for SVC model is : ", acc_score)
print ("The accuracy score for DecisionTreeClassifier model is : ", acc_score2)
print ("The accuracy score for LogisticRegression model is : ", acc_score3)
print ("The accuracy score for RandomForestClassifier model is : ", acc_score4)

column_headers = hy_df.drop(columns = ['disease_name','disease_type']).columns.values.tolist()
# symptom_array = hy_df.drop(columns = ['disease_name','disease_type']).columns.values

# patient_symptoms = ['fever', 'fatigue', 'loss_of_appetite', 'vomiting',	'abdominal_pain', 'dark_urine', 'light_colored_stools', 'joint_pain', 'jaundice', 'rash' 'bone_pain', 
#                     'joint_pain', 'muscle_pain']

# selection = ','.join(patient_symptoms)
# arr=[]
# for i in column_headers:
#     if selection.find(i) != -1:
#         arr.append(1)
#     else:
#         arr.append(0)

# df_data=pd.Series(arr)
# xdata = df_data.values.reshape(1,-1)
# predicted_disease = model.predict(xdata)
# print('There are chances you may have',predicted_disease[0],'See your Doctor immediately')


# print(symptom_array)
# print("column_headers: ",column_headers)


# THE DESIGN

arr = []
arr1 = []
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    

    def run(self):
      app=QApplication(sys.argv)
      win=QMainWindow()
      self.setupUi(win)
      win.show()
      sys.exit(app.exec_())
      
	
      


    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 600)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setStyleSheet("background-color: rgb(22, 228, 231);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 20, 811, 31))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("font: 75 22pt \"Century Gothic\";\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"font: 75 20pt \"Century Gothic\";\n"
"color: rgb(50, 0, 151);\n"
"background-color: rgb(182, 182, 182);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(10)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 140, 241, 441))
        self.widget.setStyleSheet("background-color: rgb(0, 131, 197);\n"
"border-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label_8.setStyleSheet("color: rgb(249, 249, 249);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.label_9.setStyleSheet("color: rgb(249, 249, 249);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(10, 200, 51, 16))
        self.label_10.setStyleSheet("color: rgb(249, 249, 249);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_10.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(10, 300, 51, 16))
        self.label_11.setStyleSheet("color: rgb(249, 249, 249);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_11.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_11.setObjectName("label_11")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(160, 360, 56, 17))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 211, 22))
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setMaxVisibleItems(15)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 130, 211, 22))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_2.setMaxVisibleItems(15)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 220, 211, 22))
        self.comboBox_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setMaxVisibleItems(15)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setGeometry(QtCore.QRect(10, 320, 211, 22))
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setMaxVisibleItems(15)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(380, 240, 351, 241))
        self.label_2.setStyleSheet("font: 75 14pt \"Century Gothic\";\n"
"color: rgb(170, 85, 127);\n"
"background-color: rgb(144, 144, 215);\n"
"background-color: rgb(218, 218, 218);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 241, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 83, 86);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(241, 241, 241);\n"
"font: 75 15pt \"Century Gothic\";")
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 210, 351, 31))
        self.label_4.setStyleSheet("background-color: rgb(255, 83, 86);\n"
"background-color: rgb(103, 157, 180);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(241, 241, 241);\n"
"font: 75 15pt \"Century Gothic\";")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        


    def get_selected(self,text):
       arr1.append(text)
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self._translate = _translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HYGIEIA HOSPITAL HEALTH CHECKUP"))
        self.label_8.setText(_translate("MainWindow", "Symptom 1"))
        self.label_9.setText(_translate("MainWindow", "Symptom 2"))
        self.label_10.setText(_translate("MainWindow", "Symptom 3"))
        self.label_11.setText(_translate("MainWindow", "Symptom 4"))
        self.pushButton.setText(_translate("MainWindow", "Check"))
        self.comboBox.setItemText(0, _translate("MainWindow", ''))
        self.comboBox_2.setItemText(0, _translate("MainWindow", ''))
        self.comboBox_3.setItemText(0, _translate("MainWindow", ''))
        self.comboBox_4.setItemText(0, _translate("MainWindow", ''))
        self.label_2.setText(_translate("MainWindow", ''))
        self.label_3.setText(_translate("MainWindow", "Symptom Checker"))
        self.label_4.setText(_translate("MainWindow", "Result"))
        self.comboBox.addItems(column_headers)
        self.comboBox_2.addItems(column_headers)
        self.comboBox_3.addItems(column_headers)
        self.comboBox_4.addItems(column_headers)
        
        self.comboBox.currentTextChanged.connect(self.get_selected)
        self.comboBox_2.currentTextChanged.connect(self.get_selected)
        self.comboBox_3.currentTextChanged.connect(self.get_selected)
        self.comboBox_4.currentTextChanged.connect(self.get_selected)
        
		# add signal and slot
        self.pushButton.clicked.connect(self.btn_predict) 
         
        # slot
    def btn_predict(self):
        selection = ','.join(arr1)
        # print(selection)
        for i in column_headers:
            if selection.find(i) != -1:
                arr.append(1)
            else:
                arr.append(0)

    

        df_data=pd.Series(arr)
        xdata = df_data.values.reshape(1,-1)
        # print(len(df_data))
        # print(arr)
        # print(len(column_headers))
        # print(len(arr1))
        predicted_disease = model.predict(xdata)
        predict = predicted_disease[0]
        self.label_2.setText(self._translate("MainWindow", predict))

        # arr = []

        # preprocessed_symptom = preprocess_text(symptoms_entered)
        # symptom_tfidf = tfidf_vectorizer.transform([preprocessed_symptom])
        # print('There are chances you may have',predicted_disease[0],'See your Doctor immediately')
        # predicted_disease = model.predict(symptom_tfidf)
        
        
 

Ui_MainWindow().run()


