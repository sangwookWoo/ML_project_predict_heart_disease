import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score

class model_selecting:
    def __init__(self, model, *xytt):
        
        self.X_train = xytt[0][0]
        self.X_test = xytt[0][1]
        self.y_train = xytt[0][2]
        self.y_test = xytt[0][3]
        self.model = model
        self.X_train_over,self.y_train_over = self.get_SMOTE()
        
    def get_clf_eval(self,y_test, pred=None, pred_proba=None):
        confusion = confusion_matrix(y_test, pred)
        accuracy = accuracy_score(y_test , pred)
        precision = precision_score(y_test , pred)
        recall = recall_score(y_test , pred)
        f1 = f1_score(y_test,pred)
        
        # ROC-AUC 추가 
        roc_auc = roc_auc_score(y_test, pred_proba)
        print('오차 행렬')
        print(confusion)
        # ROC-AUC print 추가
        print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f},\
        F1: {3:.4f}, AUC:{4:.4f}'.format(accuracy, precision, recall, f1, roc_auc))
        
    def get_SMOTE(self):
        # SMOTE train 함수
        from imblearn.over_sampling import SMOTE
        smote = SMOTE()
        return smote.fit_resample(self.X_train,self.y_train)
    
    def get_model_apply(self,SMOTE = False):
        if SMOTE == False:
            reg = self.model.fit(self.X_train,self.y_train)
        else:
            reg = self.model.fit(self.X_train_over,self.y_train_over)
        y_pred = reg.predict(self.X_test)
        y_pred_proba = reg.predict_proba(self.X_test)[:,1]
        self.get_clf_eval(self.y_test,y_pred,y_pred_proba)    
        