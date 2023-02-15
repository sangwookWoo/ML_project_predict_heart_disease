import streamlit as st
import time
import numpy as np

def yes_or_no_q(question):
    '''질문에 대한 답을 리턴해줍니다.'''
    answer = st.radio(question, ['네', '아니요'])
    if answer == '네':
        return 1
    elif answer == '아니요':
        return 0
    
def question(placeholder):
    with placeholder.form("my_form"):
        # 몸무게
        weight = st.number_input('몸무게를 입력해주세요(단위 : kg)')
        # 키
        height = st.number_input(label = '키를 입력해주세요(단위 : cm)')
        # 나이(범주화 필요)
        AgeCategory = st.number_input('당신의 나이는 몇 살입니까(만 나이)?')
        # 신체 부상
        PhysicalHealth = int(st.number_input('지난 30일 동안 질병과 부상을 포함해 30일 동안 아픈 일수는 며칠입니까?'))
        # 정신건강
        MentalHealth = int(st.number_input('지난 30일 동안 정신 건강이 좋지 않았던 횟수(일수)는 몇회입니까?'))
        # 수면 시간
        SleepTime = st.number_input('수면시간을 입력해주세요(단위 : 시간)')
        # 인종
        Race = st.selectbox('당신의 인종은 무엇입니까?', ['아시안', '백인', '히스패닉', '흑인', '기타', '알래스카/미국 원주민'])
            
        # 당뇨
        Diabetic = st.selectbox('당뇨병인 적이 한번이라도 있습니까?', ['네', '아니요', '애매하다', '임신 중에만 당뇨병이였다(여성만 해당)'])
        # 건강
        GenHealth = st.selectbox('본인이 느끼기에 당신의 건강 정도는?', ['매우 좋다', '좋다' , '적당하다' , '별로다' , '나쁘다'])
        # 흡연 여부
        smoking_answer = yes_or_no_q('당신은 평생에 걸쳐 100개비 미만으로 흡연을 하셨습니까?')
        # 술
        drinking_answer = yes_or_no_q('당신은 과음자입니까?(남성은 주에 14잔 이상 , 여성은 주에 7잔 이상')
        # 뇌졸중
        stroke_answer = yes_or_no_q('당신은 뇌졸중 경험이 있습니까?')
        # 운동능력
        DiffWalking = yes_or_no_q('계단을 오를 때 힘들다고 느끼십니까?')
        # 육체활동
        PhysicalActivity = yes_or_no_q('운동을 하십니까?')
        # 천식
        Asthma = yes_or_no_q('천식 걸린적이 있습니까?')
        # 신장 질환
        KidneyDisease = yes_or_no_q('신장 질환이 있습니까?')
        # 피부암
        SkinCancer = yes_or_no_q('피부암 경험이 있습니까?')
        # 성별
        Sex = st.radio('당신의 성별은 무엇입니까?', ['남자', '여자'])
        # BMI
        if height > 0:
            # BMI 계산 및 
            BMI = round(weight / ((height/100) ** 2) , 2)
        else:
            BMI = 0
            
        time.sleep(4)
        submitted = st.form_submit_button("AI 예측")
        return np.array([BMI, smoking_answer, drinking_answer, stroke_answer,
                        PhysicalHealth, MentalHealth, DiffWalking, Sex,
                        AgeCategory, Race, Diabetic, PhysicalActivity,
                        GenHealth, SleepTime, Asthma, KidneyDisease, SkinCancer]), submitted
