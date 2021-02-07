import streamlit as st
import pickle
import pandas as pd


st.title('Employee Churn Prediction')
st.sidebar.title("Enter the features of the employee")
from PIL import Image
im = Image.open("Turnover.jpg")

st.image(im, width = 450, caption = "Turnover")

model = st.selectbox("Select Your Model",  ["Gradient Boosting", "Random Forest"] )
st.write("Selected Model:", model) # From now on I can use occupation as 


if model == "Gradient Boosting":
    model = pickle.load(open("saved_model", "rb"))
#elif model == "K-Nearest Neighbor":
     #model = pickle.load(open("saved_knn_model", "rb"))
else:
     model = pickle.load(open("saved_rf_model", "rb"))
        

satisfaction_level = st.sidebar.slider("Satisfaction with job", 1, 100, step=1)
last_evaluation = st.sidebar.slider("Employee Performance", 1, 100, step=1)
number_project = st.sidebar.selectbox(("Number of Projects"), (1,2,3,4,5,6,7))
average_monthly_hours = st.sidebar.text_input("Average monthly hours") 
time_spent_company = st.sidebar.slider(("Employee Experience"), 1, 20, step=1)
Work_accident = st.sidebar.selectbox(("Has Accident?"), ["Yes", "No"])
promotion_last_5years = st.sidebar.selectbox(("Promotion in last five years?"), ["Yes", "No"])
Departments = st.sidebar.selectbox("Department",  ['sales', 'accounting','hr', 'technical', 'support', 'management', 'IT','product_mng', 'marketing', 'RandD'])
salary = st.sidebar.selectbox("Salary", ["low", "medium", "high"])  

my_dict = {"satisfaction_level": satisfaction_level/100,
        "last_evaluation" : last_evaluation/100,
        "number_project" : number_project,
        "average_monthly_hours" : int(average_monthly_hours),
        "time_spent_company" : time_spent_company,
        "Work_accident" : Work_accident,
        "promotion_last_5years": promotion_last_5years,
        "Departments": Departments,
        "salary" : salary
     
     
    }
    
df = pd.DataFrame.from_dict([my_dict])

accident_map = {'Yes': 1, 'No': 0}
df['Work_accident'] = df['Work_accident'].map(accident_map)

promotion_map = {'Yes': 1, 'No': 0}
df['promotion_last_5years'] = df['promotion_last_5years'].map(promotion_map)
                                                              
salary_map = {'high': 0, 'medium': 2, "low":1}
df['salary'] = df['salary'].map(salary_map)

department_map = {"sales":7, "technical": 9, "support": 8, "IT":0, "product_mng":6, "marketing":5, "RandD":1, "accounting":2,
                  "hr":3, "management":4}
df['Departments'] = df['Departments'].map(department_map)
    
st.header("Churn or Not?")

st.table(df.head())

prediction = model.predict(df)
    
if int(prediction[0]) == 0:
       st.success(int(prediction[0]))
else: st.warning(int(prediction[0]))
       

