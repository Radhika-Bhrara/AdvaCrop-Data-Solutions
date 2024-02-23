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

    # Team members' information with emojis
    team_members_info = [
        {
            "name": "**Radhika** 👩‍💼",
            "description": "  The Visionary Maestro \n",
            "responsibilities": "\n**Responsibilities:** As the team leader, Radhika orchestrates the team's success by overseeing various critical aspects. From ensuring a sleek and user-friendly Graphical User Interface (GUI) to meticulously collecting and managing code, maintaining Git tickets, and curating an organized repository, Radhika is the backbone of the development process. Not stopping there, she delves into extensive research and documentation, laying the foundation for innovation.\n",
            "url": "https://www.linkedin.com/in/radhika-bhrara/",
        },
        {
            "name": "\n\n\n**Sushant** 👨‍💻",
            "description": "  The Product Sage\n",
            "responsibilities": "\n**Responsibilities:** Sushant, the Product Sage, brings a keen eye for detail and innovation to the team. He spearheads product research, meticulously finalizes different attributes and parameters, and selects features that not only meet but exceed expectations. With a passion for excellence, Sushant is the driving force behind the product's evolution and its alignment with user needs.\n",
            "url": "https://www.linkedin.com/in/sushant-thombre-050ab8154/",
        },
        {
            "name": "\n\n\n**Muzaffar** 🤖",
            "description": "  The Techno-Artisan\n",
            "responsibilities": "\n**Responsibilities:** Muzaffar, the Techno-Artisan, is the team's tech image guru. With an exceptional eye for detail, he excels as the code reviewer and merger, ensuring that the team's work is not only efficient but also elegant. His expertise extends to crop classification, where he utilizes his technical prowess to enhance the precision and reliability of the algorithms at play.\n",
            "url": "https://www.linkedin.com/in/muzaffar-tasgoankar/",
        },
        {
            "name": "\n\n\n**Priyanshu** 🔧",
            "description": "  The Integration Alchemist\n",
            "responsibilities": "\n**Responsibilities:** Priyanshu, the Integration Alchemist, is the maestro behind seamless API integration and expertly navigates the realms of web scraping. His tireless research efforts ensure that the team is always on the cutting edge of data acquisition. With a penchant for detail, Priyanshu ensures that data flows seamlessly into the system, supporting the team's goals.\n",
            "url": "https://www.linkedin.com/in/08-priyanshu-jangir/",
        },
        {
            "name": "\n\n\n**Pavan** 📊",
            "description": "  The Model Maestro\n",
            "responsibilities": "\n**Responsibilities:** Pavan, the Model Maestro, takes center stage in the intricate world of model loading, training, and the classification of parameters. His expertise is crucial in ensuring that the algorithms employed are not only cutting-edge but also finely tuned to deliver precise results. Pavan's dedication to model excellence is the heartbeat of the team's success.\n",
            "url": "https://www.linkedin.com/in/pawan-balijireddi/",
        },
        {
            "name": "\n\n\n**Geethan** 🧑‍🔬",
            "description": "  The Tools Explorer\n",
            "responsibilities": "\n**Responsibilities:** Geethan, the Tools Explorer, embarks on a journey of extensive research and comparison to identify the most effective tools and approaches. His analytical mind is the team's compass, guiding them through the labyrinth of options. From data extraction methods to evaluating tools, Geethan's insights shape the team's strategic decisions and technological advancements.\n",
            "url": "https://www.linkedin.com/in/geethan-b-899b1a233/",
        },
    ]

    # Display team members' information with emojis
    for member_info in team_members_info:
        st.write(f"# {member_info['name']}\n##{member_info['description']}{member_info['responsibilities']}\n[LinkedIn Profile]({member_info['url']})")

    st.write("\n\n\n\n\n Together, these diverse talents form the Algorithmic Alchemists - a team that transcends conventional boundaries, blending innovation, expertise, and passion to create a groundbreaking solution in the realm of AdvaCrop Data Solutions. Each member brings a unique skill set, contributing to the team's collective brilliance and propelling them toward unprecedented success.")
