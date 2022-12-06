# various imports for data manipulation and visualizations
import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 
from pathlib import Path
from PIL import Image


st.title("Pineapple Distribution data FOR CALUAN")



    
with st.sidebar:
    st.subheader("Welcome!")
    st.write("| click below to navigate page view |")
    page_view = st.radio("What would you like to see?", ("About", "See All OF Data", "Compare to toher city", "FARM loss ", "Farm Data Analysis", "See Raw Data"))



#about section#
if page_view == ("About"):
    st.header("Welcome.")
    st.write("This interactive web application serves as a visual data analysis for reported Pineapple distribution to Calaun")
    st.subheader('How to use:')
    st.write("Interact with the sidebar on the left to choose which data you would like to be displayed.")
    st.subheader("About:")
    st.write("The pineaplle distrbibutin  data used for this analysis was compiled and provided to the public by  farmer to show  " "  ") 
    st.write('The Farmer  which are motivated in whole or in part by local Goverment to Provide more quality gooods.')
    st.write('For a complete project description, please see visit site [HERE]("https://github.com/scdone/us_hate_crime_analysis_1991-2020").')
    st.subheader('OUR SOURCE:')
    st.write("Data for this analysis was colecting from (, [P.H. Census data](https://psa.gov.ph/fruits-crops-bulletin/pineapple), and data from the [Farming Guide](https://www.agrifarming.in/pineapple-farming). To see all data wrangling and cleaning efforts, FEEBACK US [here](https://docs.google.com/forms/d/e/1FAIpQLSfuBzMjnys2M_siQuydKuKI-bk9SokaInYqfTxYp_7hYqQzDQ/viewform?usp=sf_link).")
    st.subheader("Limitations:")
    st.write("This data is collected by the researcher  through local agriculture  agencies. It must be understood by anyone analyzing or looking at the analysis of the data that the data does represent farmers and local Govermnet action is working. In addition, different city' local farmer, had different levels of participation in the Uniform Distributing Report over time.") 
    st.write("In addition, it is important to remember that pineapple farming is very difficult, so let's not abuse them and help them to produce a better harvest.")




if page_view == ("See All OF Data"):
    st.subheader("Total Pineapple Distribute year")
    st.subheader("Total Distributed Pineapple in  Calaun 2021-2022")
    st.caption("(Per capita values are shown per 100,000 per farm")
def my_cached_func(a, b):
    if page_view == ("Compare to toher city"):
        st.subheader("Compare State Trends - Number of Hate Crimes Per Capita")
    st.caption("(Per capita values are shown per 100,000 people. Data for Hawaii and U.S. territories not available).")

    
if page_view == ("Farm Data Analysis"):
    st.subheader('See raw data for total incidents by state')
    st.caption('(Per capita values are shown per 100,000 people)')
    st.caption('Hint: Once the dataset is selected, click the column name to sort by ascending or descending values')
 


if page_view == ("See Raw Data"):
    st.subheader('See raw data for total incidents by state')
    st.caption('(Per capita values are shown per 100,000 people)')
    st.caption('Hint: Once the dataset is selected, click the column name to sort by ascending or descending values')