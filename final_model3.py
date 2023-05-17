import pandas as pd
import numpy as np
import joblib
import streamlit as st
import sklearn
import base64

model = joblib.load('final_model_pipeline_test.pkl')
def predict_damage_grade(gender, age, edu_level, income, bank_acc, no_floors_pre,
       no_floor_post, age_building, height_ft_pre_eq,
       height_ft_post_eq, land_surface_condition,foundation_type,
       plan_configuration,tec_solution):
    
    prediction = model.predict(pd.DataFrame({'gender':gender, 'age':age,'edu_level':edu_level, 'income':income
                                               , 'bank_acc':bank_acc,
                                             'no_floors_pre':no_floors_pre,'no_floor_post':no_floor_post,'age_building':age_building,
                                             'height_ft_pre_eq':height_ft_pre_eq,'height_ft_post_eq':height_ft_post_eq,
                                             'land_surface_condition':land_surface_condition,
                                             'foundation_type':foundation_type,
                                              'plan_configuration':plan_configuration,'tec_solution':tec_solution}))
    label=['Grade 1','Grade 2', 'Grade 3','Grade 4','Grade 5']
        
    return  label[prediction[0]]
    
def main():
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    add_bg_from_local('C:\\Users\\tasne\\Downloads\\final project\\detail-nepalmap.jpg')    
      
    st.title('Damage Grade Prediction')
   
    html_temp = """
        
        <div style='background-color:white'>
        <h2 style="color:red;text-align:center;">Nepal's Earthquak</h2>
        </div>
                  """
    st.audio('C:\\Users\\tasne\\Downloads\\final project\\Nepal.mp3')
    
    st.markdown(html_temp,unsafe_allow_html=True)
    gender = st.selectbox('choose the gender_household_head',['Male','Female'])
    age = st.text_input('Age','household age')
   
    edu_level=st.selectbox('Education level',['Illiterate', 'Class 5', 'Class 4', 'SLC or equivalent',
       'Class 10', 'Class 9', 'Non-formal education',
       'Intermediate or equivalent', 'Class 7', 'Class 2', 'Class 1',
       'Class 8', 'Class 3', 'Class 6', 'Bachelors or equivalent',
       'Other', 'Masters or equivalent', 'Nursery/K.G./Kindergarten',
       'Ph.D. or equivalent'])
    income = st.text_input('household income','income')
    
    bank_acc = st.selectbox('Bank account ',['0','1'])
    no_floors_pre = st.text_input('Number of floors pre earthquake','')
    no_floor_post = st.text_input('Number of floors post earthquake','')
    age_building=st.slider('age_building',0,100)
    height_ft_pre_eq = st.slider('building height pre',0,100)
    height_ft_post_eq = st.slider('building height post',0,100)
    
    land_surface_condition=st.multiselect('land_surface_condition',['Flat', 'Moderate slope', 'Steep slope'])
    foundation_type=st.multiselect('foundation_type',['Rc', 'Brick', 'Bamboo'])
    plan_configuration = st.selectbox('plan_configuration',['Rectangular', 'T-shape', 'Square'])
    tec_solution = st.radio('pick the tech solution done',['Major repair', 'Reconstruction', 'Minor repair', 'No need'])        
    result = ""
    if st.button('predict'):
        result = predict_damage_grade(gender, age, edu_level, income, bank_acc, no_floors_pre,no_floor_post, age_building, height_ft_pre_eq, height_ft_post_eq, land_surface_condition,foundation_type, plan_configuration,tec_solution)
    st.success('The damage grade is {} '.format(result)) 

    

if __name__ =='__main__':
    main()
        
