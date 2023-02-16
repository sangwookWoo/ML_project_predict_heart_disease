'''authours : 우상욱, 민병창, 김경목'''

import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import roc_auc_score
import time
import joblib
# 사용자 함수
from questions import *
from visualization import *
from catboost import CatBoostClassifier

def main():

    # 스트림릿 페이지 레이아웃 및 제목
    st.set_page_config(page_title = '심장질환 AI 무료 예측')

    # 저장해놓은 csv 불러오기(캐싱)
    df = load_data()

    
    # 제목
    st.markdown('## 😊당신의 심장질환을 AI를 통해 예측합니다')
    st.write(' ')
    
    # 빈공간 채우기
    placeholder = st.empty()
    answers, submitted = question(placeholder)
    
    if submitted:
        
        ## 여기 모델 들어갈 자리
        with st.spinner('⚙️ AI가 예측 중입니다...'):
            placeholder.write(' ')
            
            # 로지스틱 모델 불러오기
            filePath, fileName = os.path.split(__file__)
            # reg = joblib.load(os.path.join(filePath, 'data', 'logistic.pkl'))
            reg = CatBoostClassifier()
            reg.load_model(os.path.join(filePath, 'data', 'cat.pkl'))
            
            # 예측하기
            percent = round(reg.predict_proba(answers)[0][1] * 100, 2)
            heart = reg.predict(answers)[0]
            
            st.markdown('##### 💻 AI 예측')
                
            progress = st.progress(0)
            latest_iteration = st.empty()
                
            for i in range(int(percent) + 1):
                progress.progress(i)
                time.sleep(0.01)
            latest_iteration.markdown(f'##### 심장질환이 있을 확률은 **:red[{percent}]**%입니다')
            if heart == 1:
                st.markdown(f'##### AI 예측상 당신은 심장질환을 **:red[가졌습니다]**')
            else :
                st.markdown(f'##### AI 예측 상 당신은 심장질환이 **:blue[없습니다]**')
                
            
            st.write(' ')
            st.write(' ')
            st.markdown('##### 🚴 AI가 예측한 당신의 개선 방향입니다')
            
            col1, col2, col3 = st.columns(3)
            with col1 :
                
                no_smoke_percent = round(reg.predict_proba(answers)[1][1] * 100, 2)
                no_drink_percent = round(reg.predict_proba(answers)[2][1] * 100, 2)
                no_sleep_percent = round(reg.predict_proba(answers)[3][1] * 100, 2)
                normal_weight_percent = round(reg.predict_proba(answers)[4][1] * 100, 2)
                exercise_percent = round(reg.predict_proba(answers)[5][1] * 100, 2)
                
                # 당신이 담배를 피우지 않았다면
                if (answers.at[0, 'Smoking'] == 1) & ((no_smoke_percent - percent) < 0):
                    st.metric('흡연을 하지 않았다면', str(no_smoke_percent) + '%', str(round(no_smoke_percent - percent,2)) + '%')
                    
                # 당신이 과음을 하지 않는다면
                if (answers.at[0, 'AlcoholDrinking'] == 1) & ((no_drink_percent - percent) < 0):
                    st.metric('과음을 하지 않는다면', str(no_drink_percent) + '%', str(round(no_drink_percent - percent, 2)) + '%')
            with col2:
                # 잠이 부족한 당신이 숙면을 취한다면
                if (answers.at[0, 'SleepTime'] <= 6) & ((no_sleep_percent - percent) < 0):
                    st.metric('숙면을 취한다면', str(no_sleep_percent) + '%', str(round(no_sleep_percent - percent,2)) + '%')

                # 당신이 정상 범주의 BMI 지수를 가질 경우
                if ((answers.at[0, 'BMI'] < 18.5) or (answers.at[0, 'BMI'] > 25)) & ((normal_weight_percent - percent) < 0):
                    st.metric('정상범위의 체중을 가진다면', str(normal_weight_percent) + '%', str(round(normal_weight_percent - percent, 2)) + '%')

            with col3:
                # 당신이 육체활동을 한다면
                if (answers.at[0, 'PhysicalActivity'] == 0) & ((exercise_percent - percent) < 0):
                    st.metric('당신이 운동을 한다면', str(exercise_percent) + '%', str(round(exercise_percent - percent, 2)) + '%')
                    
                    
            st.write(' ')
            st.write(' ')
            col1, col2 = st.columns(2)
            with col1:
                # BMI 지수 시각화
                st.markdown('##### 🍠 BMI 지수')
                bmi_visualization(answers.loc[0,'BMI'])
                # st.markdown(f'심장질환 있을 확률<br>{percent}%입니다.', unsafe_allow_html= True)
            with col2:
                pass
            
            if st.button('다시 진단하기'):
                st.experimental_rerun()
                
                
        

@st.cache
def load_data():
    filePath, fileName = os.path.split(__file__)
    data =  pd.read_csv(os.path.join(filePath, 'data', 'heart_2020_final.csv'))
    return data
    
if __name__ == "__main__":
    main()
    