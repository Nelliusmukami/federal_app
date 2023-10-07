import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the trained model
model = joblib.load(r"C:\Users\nelli\Downloads\rf_optimized3.pkl")

# Define the app title and layout
st.title("Type of Institution prediction app")

# Define input fields for features
Masters = st.number_input("Masters", min_value=0, max_value=2000, value=200, step=1)
Total = st.number_input("Total", min_value=85, max_value=4000, value=800, step=10)
Bachelors= st.number_input("Bachelors", min_value=0, max_value=4000, value=500, step=1)
Diploma = st.number_input("Diploma", min_value=0, max_value=600, value=60, step=1)
Academic_year=st.number_input("Academic_year",min_value=2013,max_value=2030,value=2017,step=1)
Certificate=st.number_input("Certificate",min_value=0,max_value=400,value=20,step=1)
Doctorate=st.number_input("Doctorate",min_value=0,max_value=400,value=80,step=1)
Gender_EN_Male = st.selectbox("Gender(male=1,female=0)", [0,1])
Higher_Diploma= st.number_input("Higher Diploma", min_value=0, max_value=600, value=60, step=1)
Graduate_Diploma= st.number_input("Graduate Diploma", min_value=0, max_value=600, value=60, step=1)
LocalFlag_EN_Local=st.selectbox("Nationality (local=1,expatriates=0)",[0,1])


# Create selectboxes for each campus zone
Campus_Zone_EN_Dubai= st.selectbox("Campus in Dubai", [0,1])
Campus_Zone_EN_Ajman= st.selectbox("Campus in Ajman", [0,1])
Campus_Zone_EN_Umm_Al_Quwain=st.selectbox("Campus in Umm Al Quwain", [0,1])
Campus_Zone_EN_Sharjah=st.selectbox("Campus in Sharjah", [0,1])
Campus_Zone_EN_Fujairah=st.selectbox("Campus in Fujairah", [0,1])
Campus_Zone_EN_Ras_Al_Khaimah=st.selectbox("Campus in Ras Al Khaimah", [0,1])
Campus_Zone_EN_Abu_Dhabi=st.selectbox("Campus in Abu Dhabi", [0,1])


# Process input values
input_data ={
    "Masters": [Masters],
    "Total": [Total],
    "Bachelors": [Bachelors],
    "Diploma": [Diploma],
    "Academic_year": [Academic_year],
    "Certificate": [Certificate],
    "Doctorate": [Doctorate],
    "Higher Diploma":[Higher_Diploma ],
    "Graduate Diploma":[Graduate_Diploma  ],
    "Campus_Zone_EN_Dubai":[Campus_Zone_EN_Dubai ],
    "Campus_Zone_EN_Ajman ":[Campus_Zone_EN_Ajman],
    "LocalFlag_EN_Local":[LocalFlag_EN_Local],                                      
    "Campus_Zone_EN_Umm_Al_Quwain":[Campus_Zone_EN_Umm_Al_Quwain],
    "Campus_Zone_EN_Sharjah":[Campus_Zone_EN_Sharjah],          
    "Campus_Zone_EN_Fujairah":[Campus_Zone_EN_Fujairah],          
    "Campus_Zone_EN_Ras_Al_Khaimah":[Campus_Zone_EN_Ras_Al_Khaimah],   
    "Gender_EN_Male":[Gender_EN_Male],

    
}

# Create the input_data dataframe
input_data_df = pd.DataFrame(input_data)

# Scale input data using the same scaler used during training
scaler = StandardScaler()
input_data_scaled = scaler.fit_transform(input_data_df)


if st.button("Predict"):
    # Check the selected campus zones and take action accordingly
    selected_campus_zones = [
        Campus_Zone_EN_Dubai, 
        Campus_Zone_EN_Ajman, 
        Campus_Zone_EN_Umm_Al_Quwain,
        Campus_Zone_EN_Sharjah,
        Campus_Zone_EN_Fujairah,
        Campus_Zone_EN_Ras_Al_Khaimah,
        Campus_Zone_EN_Abu_Dhabi
    ]
    
    # Count the number of selected campus zones
    num_selected = sum(selected_campus_zones)
    
    # If only one campus zone is selected, make the prediction
    if num_selected == 1:
        # Make a prediction using the trained model
        prediction = model.predict(input_data_scaled)
        
        # Display the prediction
        if prediction[0] == 1:
            st.success("The institution is a non-federal institution")
        else:
            st.success("The institution is a federal institution")
    else:
        st.error("Please select only one campus zone")