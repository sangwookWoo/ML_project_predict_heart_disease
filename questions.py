import streamlit as st
import time
import numpy as np
import pandas as pd

def yes_or_no_q(question):
    '''질문에 대한 답을 리턴해줍니다.'''
    answer = st.radio(question, ['네', '아니요'])
    if answer == '네':
        return 1
    elif answer == '아니요':
        return 0
    
def question(placeholder):
    
    # 초기 설정
    base_df = pd.DataFrame(columns = ['BMI', 'Smoking', 'AlcoholDrinking', 'Stroke',
                                    'PhysicalHealth', 'MentalHealth', 'DiffWalking', 'Sex',
                                    'PhysicalActivity', 'SleepTime', 'Asthma', 'KidneyDisease',
                                    'SkinCancer', 'AgeCategory_18-24', 'AgeCategory_25-29',
                                    'AgeCategory_30-34', 'AgeCategory_35-39', 'AgeCategory_40-44',
                                    'AgeCategory_45-49', 'AgeCategory_50-54', 'AgeCategory_55-59',
                                    'AgeCategory_60-64', 'AgeCategory_65-69', 'AgeCategory_70-74',
                                    'AgeCategory_75-79', 'AgeCategory_80 or older',
                                    'Race_American Indian/Alaskan Native', 'Race_Asian', 'Race_Black',
                                    'Race_Hispanic', 'Race_Other', 'Race_White', 'GenHealth_Excellent',
                                    'GenHealth_Fair', 'GenHealth_Good', 'GenHealth_Poor',
                                    'GenHealth_Very good', 'Diabetic_No',
                                    'Diabetic_No, borderline diabetes', 'Diabetic_Yes',
                                    'Diabetic_Yes (during pregnancy)'])
    
    base_df.loc[0, ['AgeCategory_18-24', 'AgeCategory_25-29',
                    'AgeCategory_30-34', 'AgeCategory_35-39', 'AgeCategory_40-44',
                    'AgeCategory_45-49', 'AgeCategory_50-54', 'AgeCategory_55-59',
                    'AgeCategory_60-64', 'AgeCategory_65-69', 'AgeCategory_70-74',
                    'AgeCategory_75-79', 'AgeCategory_80 or older',
                    'Race_American Indian/Alaskan Native', 'Race_Asian', 'Race_Black',
                    'Race_Hispanic', 'Race_Other', 'Race_White', 'GenHealth_Excellent',
                    'GenHealth_Fair', 'GenHealth_Good', 'GenHealth_Poor',
                    'GenHealth_Very good', 'Diabetic_No',
                    'Diabetic_No, borderline diabetes', 'Diabetic_Yes',
                    'Diabetic_Yes (during pregnancy)']] = 0
    
    with placeholder.form("my_form"):
        # 몸무게
        weight = st.number_input('몸무게를 입력해주세요(단위 : kg)')
        # 키
        height = st.number_input(label = '키를 입력해주세요(단위 : cm)')
        # 나이(범주화 필요)
        AgeCategory = st.number_input('당신의 나이는 몇 살입니까(만 나이)?')
        if AgeCategory <= 24:
            base_df.loc[0, 'AgeCategory_18-24'] = 1
        elif AgeCategory <= 29:
            base_df.loc[0, 'AgeCategory_25-29'] = 1
        elif AgeCategory <= 34:
            base_df.loc[0, 'AgeCategory_30-34'] = 1           
        elif AgeCategory <= 39:
            base_df.loc[0, 'AgeCategory_35-39'] = 1    
        elif AgeCategory <= 44:
            base_df.loc[0, 'AgeCategory_40-44'] = 1   
        elif AgeCategory <= 49:
            base_df.loc[0, 'AgeCategory_45-49'] = 1
        elif AgeCategory <= 54:
            base_df.loc[0, 'AgeCategory_50-54'] = 1
        elif AgeCategory <= 59:
            base_df.loc[0, 'AgeCategory_55-59'] = 1
        elif AgeCategory <= 64:
            base_df.loc[0, 'AgeCategory_60-64'] = 1
        elif AgeCategory <= 69:
            base_df.loc[0, 'AgeCategory_65-69'] = 1
        elif AgeCategory <= 74:
            base_df.loc[0, 'AgeCategory_70-74'] = 1
        elif AgeCategory <= 79:
            base_df.loc[0, 'AgeCategory_75-79'] = 1
        else:
            base_df.loc[0, 'AgeCategory_80 or older'] = 1

        # 신체 부상
        PhysicalHealth = int(st.number_input('지난 30일 동안 질병과 부상을 포함해 아픈 일수는 며칠입니까?'))
        base_df.loc[0, 'PhysicalHealth'] = PhysicalHealth
        # 정신건강
        MentalHealth = int(st.number_input('지난 30일 동안 정신 건강이 좋지 않았던 횟수(일수)는 며칠입니까?'))
        base_df.loc[0, 'MentalHealth'] = MentalHealth
        # 수면 시간
        SleepTime = st.number_input('최근 한달 간 평균 수면시간을 입력해주세요(단위 : 시간)')
        base_df.loc[0, 'SleepTime'] = SleepTime
        # 인종
        Race = st.selectbox('당신의 인종은 무엇입니까?', ['아시안', '백인', '히스패닉', '흑인', '기타', '알래스카/미국 원주민'])
        if Race == '아시안':
            base_df.loc[0, 'Race_Asian'] = 1
        elif Race == '백인':
            base_df.loc[0, 'Race_White'] = 1
        elif Race == '히스패닉':
            base_df.loc[0, 'Race_Hispanic'] = 1
        elif Race == '흑인':
            base_df.loc[0, 'Race_Black'] = 1
        elif Race == '기타':
            base_df.loc[0, 'Race_Other'] = 1
        elif Race == '알래스카/미국 원주민':
            base_df.loc[0, 'Race_American Indian/Alaskan Native'] = 1
            
        
        # 당뇨
        Diabetic = st.selectbox('당뇨병인 적이 한번이라도 있습니까?', ['네', '아니요', '애매하다', '임신 중에만 당뇨병이였다(여성만 해당)'])
        if Diabetic == '네':
            base_df.loc[0, 'Diabetic_Yes'] = 1
        elif Diabetic == '아니요':
            base_df.loc[0, 'Diabetic_No'] = 1
        elif Diabetic == '애매하다':
            base_df.loc[0, 'Diabetic_No, borderline diabetes'] = 1
        elif Diabetic == '임신 중에만 당뇨병이였다(여성만 해당)':
            base_df.loc[0, 'Diabetic_Yes (during pregnancy)'] = 1
            
        # 건강
        GenHealth = st.selectbox('본인이 느끼기에 당신의 건강 정도는?', ['훌륭하다', '아주 좋다' , '좋다' , '그저 그렇다' , '나쁘다'])
        if GenHealth == '훌륭하다':
            base_df.loc[0, 'GenHealth_Excellent'] = 1
        elif GenHealth == '아주 좋다':
            base_df.loc[0, 'GenHealth_Very good'] = 1
        elif GenHealth == '좋다':
            base_df.loc[0, 'GenHealth_Good'] = 1
        elif GenHealth == '그저 그렇다':
            base_df.loc[0, 'GenHealth_Fair'] = 1
        elif GenHealth == '나쁘다':
            base_df.loc[0, 'GenHealth_Poor'] = 1        
            
        # 흡연 여부
        Smoking = yes_or_no_q('당신은 평생에 걸쳐 100개비 미만으로 흡연을 하셨습니까?')
        base_df.loc[0, 'Smoking'] = Smoking
        # 술
        AlcoholDrinking = yes_or_no_q('당신은 과음자입니까?(남성은 주에 14잔 이상 , 여성은 주에 7잔 이상')
        base_df.loc[0, 'AlcoholDrinking'] = AlcoholDrinking
        # 뇌졸중
        Stroke = yes_or_no_q('당신은 뇌졸중 경험이 있습니까?')
        base_df.loc[0, 'Stroke'] = Stroke
        # 운동능력
        DiffWalking = yes_or_no_q('계단을 오를 때 힘들다고 느끼십니까?')
        base_df.loc[0, 'DiffWalking'] = DiffWalking
        # 육체활동
        PhysicalActivity = yes_or_no_q('운동을 하십니까?')
        base_df.loc[0, 'PhysicalActivity'] = PhysicalActivity
        # 천식
        Asthma = yes_or_no_q('천식에 걸린 적이 있습니까?')
        base_df.loc[0, 'Asthma'] = Asthma
        # 신장 질환
        KidneyDisease = yes_or_no_q('신장 질환이 있습니까?')
        base_df.loc[0, 'KidneyDisease'] = KidneyDisease
        # 피부암
        SkinCancer = yes_or_no_q('피부암에 걸린 적이 있습니까?')
        base_df.loc[0, 'SkinCancer'] = SkinCancer
        # 성별
        Sex = st.radio('당신의 성별은 무엇입니까?', ['남자', '여자'])
        if Sex == '남자':
            Sex = 1
        else :
            Sex = 0
        base_df.loc[0, 'Sex'] = Sex
        # BMI
        if height > 0:
            # BMI 계산 및 
            BMI = round(weight / ((height/100) ** 2) , 2)
        else:
            BMI = 0
        base_df.loc[0, 'BMI'] = BMI
            
        time.sleep(4)
        submitted = st.form_submit_button("AI 예측")
        return base_df, submitted
