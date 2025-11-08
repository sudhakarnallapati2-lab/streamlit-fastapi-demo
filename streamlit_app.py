import requests
import streamlit as st

API_URL = "http://localhost:8000"

st.title("User Viewer (FastAPI + Streamlit)")

if st.button("Load Users"):
    response = requests.get(f"{API_URL}/users")
    if response.status_code == 200:
        users = response.json()
        st.table(users)
    else:
        st.error("Failed to fetch users")

st.subheader("Add New User")

name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Add User"):
    payload = {"name": name, "email": email}
    response = requests.post(f"{API_URL}/add_user", json=payload)

    if response.status_code == 200:
        st.success("User added successfully!")
    else:
        st.error("User creation failed")
