import streamlit as st
import requests

# Conversation history
conversation = []

# Fetch random motivational thought from an open-source API
def get_motivational_thought():
    try:
        response = requests.get("https://api.quotable.io/random")
        response.raise_for_status()
        return response.json()["content"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching motivational thought: {e}")
        return "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle."

def get_spiritual_image():
    try:
        response = requests.get("https://picsum.photos/200/300")
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching spiritual image: {e}")
        return None

def get_response(message):
    # Here you would implement your chatbot logic or integrate with an external API
    # For this example, we'll just return a simple hardcoded response
    return "Hello! I'm a chatbot created with Streamlit. How can I assist you today?"

# Streamlit app
def app():
    st.set_page_config(page_title="myKrishna")
    st.markdown("""
    <style>
    .main {
        background-color: #2B155C;
        color: #2C3E50;
    }
    .sidebar .sidebar-content {
        background-color: #E6F0FF;
        color: #2C3E50;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("myKrishna")

    # Display motivational thought
    motivational_thought = get_motivational_thought()
    st.sidebar.markdown(f"**Motivational Thought:** {motivational_thought}")

    # Display spiritual image
    spiritual_image = get_spiritual_image()
    if spiritual_image:
        st.sidebar.image(spiritual_image, use_column_width=True)

    # Display conversation history
    for sender, message in conversation:
        if sender == "user":
            st.markdown(f"<div style='background-color: #D6EAF8; border-radius: 5px; padding: 10px; margin-bottom: 10px; text-align: right;'>{message}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='background-color: #AED6F1; border-radius: 5px; padding: 10px; margin-bottom: 10px;'>{message}</div>", unsafe_allow_html=True)

    # Get user input
    user_input = st.text_input("You:", "", key="user_input")
    send_button = st.button("Send", key="send_button")

    # Send user input to chatbot and get response
    if send_button and user_input:
        response = get_response(user_input)
        conversation.append(("user", user_input))
        conversation.append(("bot", response))
        st.text_area("Conversation", value="", height=300, max_chars=None, key="conversation")

# Run the app
if __name__ == "__main__":
    app()