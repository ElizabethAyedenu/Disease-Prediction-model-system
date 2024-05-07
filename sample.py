# THE DESIGN

# arr = []
# arr1 = []

        

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication,QMainWindow,QListWidgetItem
# import sys




# class Ui_MainWindow(object):
#     def run(self):
#       app=QApplication(sys.argv)
#       win=QMainWindow()
#       self.setupUi(win)
#       win.show()
#       sys.exit(app.exec_())


#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(534, 389)
#         MainWindow.setStyleSheet("background-color: rgb(108, 221, 255);\n"
# "background-color: rgb(243, 243, 243);")
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
#         self.gridLayout.setObjectName("gridLayout")
#         self.symp_listWidget = QtWidgets.QListWidget(self.centralwidget)
#         self.symp_listWidget.setMaximumSize(QtCore.QSize(16000000, 16777215))
#         self.symp_listWidget.setStyleSheet("background-color: rgb(145, 218, 218);")
#         self.symp_listWidget.setObjectName("symp_listWidget")
#         self.gridLayout.addWidget(self.symp_listWidget, 1, 0, 11, 1)
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setMinimumSize(QtCore.QSize(450, 0))
#         self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
#         self.label_2.setStyleSheet("background-color: rgb(165, 0, 0);\n"
# "color: rgb(255, 255, 255);")
#         self.label_2.setObjectName("label_2")
#         self.gridLayout.addWidget(self.label_2, 7, 4, 1, 1)
#         self.check_pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.check_pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Corbel")
#         font.setPointSize(10)
#         font.setBold(True)
#         font.setWeight(75)
#         self.check_pushButton.setFont(font)
#         self.check_pushButton.setStyleSheet("background-color: rgb(60, 187, 255);\n"
# "color: rgb(255, 255, 255);")
#         self.check_pushButton.setObjectName("check_pushButton")
#         self.gridLayout.addWidget(self.check_pushButton, 12, 0, 1, 2)
#         self.title_label = QtWidgets.QLabel(self.centralwidget)
#         self.title_label.setMaximumSize(QtCore.QSize(16777215, 45))
#         font = QtGui.QFont()
#         font.setFamily("Corbel")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         self.title_label.setFont(font)
#         self.title_label.setLayoutDirection(QtCore.Qt.RightToLeft)
#         self.title_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
# "color: rgb(0, 63, 189);\n"
# "background-color: rgb(209, 209, 209);")
#         self.title_label.setAlignment(QtCore.Qt.AlignCenter)
#         self.title_label.setObjectName("title_label")
#         self.gridLayout.addWidget(self.title_label, 0, 0, 1, 5)
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Corbel")
#         font.setPointSize(10)
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton.setFont(font)
#         self.pushButton.setStyleSheet("background-color: rgb(60, 187, 255);\n"
# "color: rgb(255, 255, 255);")
#         self.pushButton.setObjectName("pushButton")
#         self.gridLayout.addWidget(self.pushButton, 14, 0, 1, 1)
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setMinimumSize(QtCore.QSize(450, 150))
#         self.label.setMaximumSize(QtCore.QSize(2000, 100))
#         font = QtGui.QFont()
#         font.setFamily("Corbel Light")
#         font.setPointSize(20)
#         self.label.setFont(font)
#         self.label.setStyleSheet("background-color: rgb(178, 178, 178);")
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setObjectName("label")
#         self.gridLayout.addWidget(self.label, 6, 4, 1, 1)
#         MainWindow.setCentralWidget(self.centralwidget)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def get_selected(self,item):
#        arr1.append(item.text())

#     def refresh_button(self):

#         arr.clear()
#         arr1.clear()
#         print(arr)
#         print(arr1)

#         self.symp_listWidget.clear()
#         self.label.clear() 

#         for i in col_header:
#             # print(i)
#             item = QListWidgetItem(i)
            
#             item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
#             item.setCheckState(QtCore.Qt.Unchecked)
#             self.symp_listWidget.addItem(item)

        

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         self._translate = _translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label_2.setText(_translate("MainWindow", "Result"))
#         self.check_pushButton.setText(_translate("MainWindow", "Check"))
#         self.title_label.setText(_translate("MainWindow", "Hygieia Hospital Health Checkup"))
#         self.pushButton.setText(_translate("MainWindow", "Refresh"))
#         self.label.setText(_translate("MainWindow", "Predicted disease"))

#     # for the checklist
#         for i in col_header:
#             item = QListWidgetItem(i)
#             item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
#             item.setCheckState(QtCore.Qt.Unchecked)
#             self.symp_listWidget.addItem(item)

#         self.symp_listWidget.itemClicked.connect(self.get_selected)  
        
 
# # for the check button
#         # add signal and slot
#         self.check_pushButton.clicked.connect(self.btn_predict) 

#     def btn_predict(self):
              
#         selection = ','.join(arr1)
#         for i in col_header:
#             if selection.find(i) != -1:
#                 arr.append(1)
#             else:
#                 arr.append(0)
#         # print(arr)


#         df_data=pd.Series(arr)
#         xdata = df_data.values.reshape(1,-1)
#         print(arr1)
#         print(arr)
#         predicted_disease = model_4.predict(xdata)
#         predict = predicted_disease[0]
#         self.label.setText(self._translate("MainWindow", predict))

# #  for refresh button
        
    
        
#         self.pushButton.clicked.connect(self.refresh_button)




# Ui_MainWindow().run()
 
