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



# Sidebar with radio buttons
selection = st.sidebar.radio("Select an Option", ["Home", "Use Case Description", "Demonstration", "Team Description"])

# Display content based on the selected radio button
if selection =="Home":
       # Title for the app
       st.title('AdvaCrop Data Solutions')
       # Add an image to the layout with adjusted size
       image_url = "main.jpeg"  # Replace with the actual URL or path of your image
       st.image(image_url, caption='AdvaCrop Data Solutions', use_column_width=100)

elif selection == "Use Case Description":
    st.header("Use Case Description")
    st.write("Provide detailed information on the use cases of AdvaCrop Data Solutions.")
    # Add more content specific to the use case description

elif selection == "Demonstration":
    st.header("Demonstration")
    st.write("Demonstrate the functionality and features of AdvaCrop Data Solutions.")
    # Add more content specific to the demonstration

elif selection == "Team Description":
    st.header("Team Description - Algorithmic Alchemists 🚀")
    
    # Define team members with linked URLs and emojis
    team_members = {
        "Radhika (Team Leader)": {"link": "https://www.linkedin.com/in/radhika-bhrara/", "emoji": "👩‍💼"},
        "Sushant": {"link": "insert_link_for_Sushant_here", "emoji": "👨‍💻"},
        "Muzaffar": {"link": "insert_link_for_Muzaffar_here", "emoji": "🤖"},
        "Pavan": {"link": "insert_link_for_Pavan_here", "emoji": "📊"},
        "Priyanshu": {"link": "insert_link_for_Priyanshu_here", "emoji": "🔧"},
        "Geethan": {"link": "insert_link_for_Geethan_here", "emoji": "🧑‍🔬"},
    }
    
    # Display team members with linked URLs and emojis
    for member, details in team_members.items():
        st.write(f"{details['emoji']} [{member}]({details['link']})")

    # Add more content specific to the team description

# Your Streamlit app logic can continue from here
