import streamlit as st

st.header("About Us")

# Create a layout with each person's information stacked vertically
col1, col2 = st.columns([1, 3])  # Adjust the column width ratio as needed

# First person
with col1:
    st.image("Assets/Adi.png", width=150)

with col2:
    st.title("Aadithya Vinod")
    st.write("Machine Learning Researcher")

    st.subheader("Role Description")
    st.write("Collects questions from the end users that need to be answered, looks for the answers to those questions, and then prepares a report that will be passed to the project leader")

# Second person
col1, col2 = st.columns([1, 3])  # Adjust the column width ratio as needed

with col1:
    st.image("Assets/Niru.png", width=150)

with col2:
    st.title("Niranjan Aravindan")
    st.write("Algorithm Designer")

    st.subheader("Role Description")
    st.write("Works to build the algorithm, and train it followed by testing the efficiency and accuracy of the model")

# Third person
col1, col2 = st.columns([1, 3])

with col1:
    st.image("Assets/Abhi.png", width=150)

with col2:
    st.title("Abhishek Menon")
    st.write("Data Analyst")

    st.subheader("Role Description")
    st.write("Decides upon the data required and the type of data for training the model, collects the data, ensures the type of data and its authenticity")

# Fourth person
col1, col2 = st.columns([1, 3])

with col1:
    st.image("Assets/kailas.png", width=150)

with col2:
    st.title("Kailas Balakrishnan")
    st.write("Leader, Developer")

    st.subheader("Role Description")
    st.write("Schedules the tasks among the team members and builds the model, ensures the task is completed on time, resolves doubts (if any) and is one source of contact")




