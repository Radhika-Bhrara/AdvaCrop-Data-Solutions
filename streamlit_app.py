import streamlit as st
import pymysql
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="AdvaCrop Data Solutions", initial_sidebar_state="auto")

# Add a logo and title using HTML
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Extend the layout to the whole page
st.markdown("""
    <style>
        .reportview-container {
            flex-direction: row;
        }
        header > .toolbar {
            flex-direction: row;
            left: 2rem;
            right: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Add an image to the layout
image_url = "main.jpeg"  # Replace with the actual URL of your image
st.image(image_url, caption='AdvaCrop Data Solutions', use_column_width=True)
st.title('AdvaCrop Data Solutions')
# Your Streamlit app logic can continue from here
# For example, you can add input widgets, data processing, and visualizations

