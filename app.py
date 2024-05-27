import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

model = pk.load(open('breastcancerprediction.pkl','rb'))

data = pd.read_csv('breast-cancer.csv')

st.header('Breast Cancer Predictor')


radiusmean = st.number_input('Radius Mean')
areamean =st.number_input('Area Mean')
concavitymean =  st.number_input('Concavity Mean')
concavepointsmean =   st.number_input('Concave Points Mean')
symmetry_mean =   st.number_input('Symmetry Mean')
radiusse =   st.number_input('Radius Standard Error')
area_se =  st.number_input('Area Standard Error')
concavityse =  st.number_input('Concavity Standard Error')
Concavepointsse =  st.number_input('Concavepoints Standard Error')
symmetryse =  st.number_input('symmetry Standard Error')
radiusw =   st.number_input('Radius Worst')
areaw =  st.number_input('Area Worst')
concavityw =  st.number_input('Concavity Worst')
Concavepointsw =  st.number_input('Concavepoints Worst')
symmetryw =  st.number_input('symmetry Worst')

if st.button ('Predict'):
    input =np.array([[radiusmean,areamean,concavitymean,concavepointsmean,symmetry_mean,radiusse,area_se,concavityse,Concavepointsse,symmetryse ,radiusw,areaw,concavityw,Concavepointsw,symmetryw ]])
    x = model.predict(input)
    if x[0] == 1:
        st.error("Malignant condition detected. Please seek medical attention.")
    else:
        st.success("Benign condition detected. Regular check-ups are still recommended.")