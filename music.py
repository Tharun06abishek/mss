import streamlit as st
import tidalapi

# Initialize the TIDAL session
def initialize_session():
    session = tidalapi.Session()
    st.write("Please authenticate through your Tidal account.")
    session.login_oauth_simple()  # Opens a browser window for user login
    return session

# Streamlit UI
st.title("Tidal API Interface")

# Button to initialize TIDAL session
if st.button("Connect to TIDAL"):
    session = initialize_session()
    if session.check_login():
        st.success("Successfully connected to Tidal!")

# Search for artists
artist_name = st.text_input("Enter artist name:")
if artist_name:
    try:
        search_results = session.search('artists', artist_name)
        if search_results:
            st.write(f"Top result: {search_results[0].name}")
        else:
            st.write("No artists found.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
